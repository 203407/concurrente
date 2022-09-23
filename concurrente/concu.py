import requests
import time
import psycopg2

#investigar libreria threading
#live shares

def get_service():
    res = requests.get('https://jsonplaceholder.typicode.com/photos')
    res = res.json()
    

    try:
        connnection = psycopg2.connect(
            host = 'localhost',
            user = 'postgres',
            password = '',
            database = ''
        )
        
        con = connnection.cursor()
        

        for x in res:   
            write_db(con,x['title'],connnection) 

    
    except Exception as ex:
        print(ex)

    finally:
        connnection.close()
        print("conexion cerrada")


def write_db(con, dataname,connnection):
    
    
        que = f"INSERT INTO dta (name) VALUES ('{dataname}')"        

        if con.execute(que) == None:
            connnection.commit()

        print("GG")


if __name__  == "__main__":
    init_time = time.time()

    get_service()

    end_time = time.time() - init_time

    print(end_time)