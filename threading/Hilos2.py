import pytube 
import requests
from pprint import pprint
import json
import psycopg2
import time
import threading
import concurrent.futures

threading_local = threading.local()

def service(URL):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(get_service, URL) 
        
def get_service(url):
    v1 = pytube.YouTube(url)
    v1.streams.first().download("/Users/ACarc/Documentos")
    print("done") 


if __name__ == "__main__":

    URL = ['https://www.youtube.com/watch?v=fk4BbF7B29w',
        'https://www.youtube.com/watch?v=niG3YMU6jFk',
        'https://www.youtube.com/watch?v=cii6ruuycQA',
        'https://www.youtube.com/watch?v=gBRi6aZJGj4',
        'https://www.youtube.com/watch?v=bo9Z_pgByQY',]
  

    init_time = time.time()
    service(URL)
    end_time = time.time() - init_time
    print(end_time)
