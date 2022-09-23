import requests
import time
import psycopg2

#investigar libreria threading
#live shares

def get_service():
    res = requests.get('https://jsonplaceholder.typicode.com/photos')
    
    
    for x in res:   
        write_db(x['title']) 



def write_db(dataname):
    
    try:
        connnection = psycopg2.connect(
            host = 'localhost',
            user = 'postgres',
            password = '',
            database = ''
        )
        
        con = connnection.cursor()

        que = f"INSERT INTO prueba (name) VALUES ('{dataname}')"        

        if con.execute(que) == None:
            connnection.commit()


    except Exception as ex:
        print(ex)

    finally:
        connnection.close()
        print("conexion cerrada")



    
if __name__  == "__main__":
    init_time = time.time()

    get_service()

    end_time = time.time() - init_time

    print(end_time)