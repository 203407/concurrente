import requests
import threading 
import time
import pytube 
import json
import psycopg2
import concurrent.futures
from configparser import ConfigParser

#DEFAULT SERVICE

def get_services():   
   response = requests.get('https://randomuser.me/api/')
   if response.status_code == 200:
       results = response.json().get('results')
       name = results[0].get('name').get('first')
       print(name)

#dOWNLOAD VIDEOS

def down_video(URL):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(get_down, URL) 

def get_down(url):
    v1 = pytube.YouTube(url)
    v1.streams.first().download("/Users/ACarc/Documentos")
    print("done")

#DATA BASE WRITER
 
def config(archivo='base_de_datos.ini', seccion='postgresql'):
    # Crear el parser y leer el archivo
    parser = ConfigParser()
    parser.read(archivo)
 
    # Obtener la sección de conexión a la base de datos
    db = {}
    if parser.has_section(seccion):
        params = parser.items(seccion)
        for param in params:
            db[param[0]] = param[1]
        return db
    else:
        raise Exception('Secccion {0} no encontrada en el archivo {1}'.format(seccion, archivo))


def get_db():
    res = requests.get('https://jsonplaceholder.typicode.com/photos')
    res = res.json()
    
    connnection = None

    try:
        
        params = config()
        connnection = psycopg2.connect(**params)        
        con = connnection.cursor()
        
        for x in res:   
            write_db(con,x['title'],connnection) 


    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connnection is not None:
            connnection.close()
            print('Conexión finalizada.')


def write_db(con, dataname,connnection):
    
    
        que = f"INSERT INTO dta (name) VALUES ('{dataname}')"        

        if con.execute(que) == None:
            connnection.commit()

        print("add register")


if __name__ == '__main__':
    
   URL = ['https://www.youtube.com/watch?v=bo9Z_pgByQY',
        'https://www.youtube.com/watch?v=O91DT1pR1ew',
        'https://www.youtube.com/watch?v=h3EJICKwITw',
        'https://www.youtube.com/watch?v=4TwAKGvz6T8',
        'https://www.youtube.com/watch?v=qwzQPh7dW_4',]
    
   th2 =  threading.Thread(target=down_video,args=[URL])
   th2.start()
   
   for x in range(0,50):
    th1 = threading.Thread(target=get_services)
    th1.start()
   
   th3 = threading.Thread(target=get_db)
   th3.start()