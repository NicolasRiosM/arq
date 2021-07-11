import psycopg2

conec = None
cur = None

def conexion():
    try:
        global conec
        global cur
        conec = psycopg2.connect(host="157.245.180.1", database="perros", port='5432', user="alumno", password="alumno")
        print("Conexión con base de datos establecida")
        cur = conec.cursor()
    except:
        print("Error de conexión con base de datos")
    
def consultar(sqlquery):
    cur.execute(sqlquery)
    return cur.fetchall()

def modificar(sqlquery):
    cur.execute(sqlquery) 
    conec.commit()
    conec.close() 
    
def cerrar():
    try:
        cur.close()
        conec.close()
        print("Conexión con base de datos cerrada")
    except:
        print("Error al cerrar conexión")    

def llenado(largo):
    aux = str(largo)
    while len(aux) < 5:
        aux = '0' + aux
    print(aux)
    return aux
def escuchar(sock):
    cant_r = 0
    tamaño = None
    menj = ""
    while True:
        data = sock.recv(4096)
        if cant_r == 0:
            tamaño = int(data[:5].decode())
            nombre = data[5:10].decode()
            menj = menj + data[10:].decode()
            cant_r += len(data)-5
        else:
            menj = menj+data.decode()
            cant_r += len(data)
        if cant_r >= tamaño:
            break
    return nombre, menj
conexion()
