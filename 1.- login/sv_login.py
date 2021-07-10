import socket  
from conect import *
import bcrypt
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   

s.connect(("localhost", 5000))
s.send(bytes('00010sinitlogin','utf-8'))

val=0
print("Ingresando a la cuenta de usuario")
while True:
    datos = s.recv(4096)
    if datos.decode('utf-8').find('login'):
        datos = datos[10:]
        target = datos.decode()
        data = target.split()

        consulta = f"select (email, pass) from usuario"
        respuesta = consultar(consulta)
#--------------------------------------------------------------#
        i=0
        print("hola")
        while (i<len(respuesta)):
            comp = respuesta [i][0]
            i=i+1
            mail =[]
            psw = []
            j=0
            k=0
            while (j<len(comp) and comp[j] != ","):
                mail.append(comp[j])
                k = j
                j=j+1
            mail.pop(0)
            email=''.join(mail)
            while (k<len(comp)):
                psw.append(comp[k])
                k=k+1
            psw.pop(0)
            psw.pop(0)
            psw.pop()
            password=''.join(psw)
#-------------------------VALIDANDO--------------------------#
            enchash = password.encode()
            encpass = data[1].encode()
            
            if data[0] == email and bcrypt.checkpw(encpass, enchash):
                val=1
                print("Ha ingresado con éxito a su cuenta")
                dat="ok"
                mens= dat + " "
                aux=llenado(len(mens+'login'))
                mensaje=aux+'login'+mens
                socket.send(bytes(mensaje,'utf-8'))
                break
#--------------------------------------------------------------#
    if (val!=1):
        print("Contraseña incorrecta")
    
    s.close()

