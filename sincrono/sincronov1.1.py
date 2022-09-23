import requests
import time
import psycopg2

#investigar libreria threading
#live shares

from configparser import ConfigParser
 
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


def get_service():
    res = requests.get('https://jsonplaceholder.typicode.com/photos')
    res = res.json()
    
    for x in res:   
        write_db(x['title']) 




def write_db(dataname):
    
    connnection = None

    try:

        params = config()

        connnection = psycopg2.connect(**params)
        
        
        con = connnection.cursor()

        que = f"INSERT INTO dta (name) VALUES ('{dataname}')"        

        if con.execute(que) == None:
            connnection.commit()


    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connnection is not None:
            connnection.close()
            print('Conexión finalizada.')



    
if __name__  == "__main__":
    init_time = time.time()

    get_service()

    end_time = time.time() - init_time

    print(end_time)