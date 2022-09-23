import pytube 
import requests
from pprint import pprint
import json
import psycopg2
import time
import threading
import concurrent.futures

threading_local = threading.local()

def service(url1, url2, url3, url4, url5):

    v1 = pytube.YouTube(url1)
    v1.streams.first().download("/Users/ACarc/Documentos")
    print("done")

    v2 = pytube.YouTube(url2)
    v2.streams.first().download("/Users/ACarc/Documentos")
    print("done")

    v3 = pytube.YouTube(url3)
    v3.streams.first().download("/Users/ACarc/Documentos")
    print("done")

    v4 = pytube.YouTube(url4)
    v4.streams.first().download("/Users/ACarc/Documentos")
    print("done")

    v5 = pytube.YouTube(url5)
    v5.streams.first().download("/Users/ACarc/Documentoso")
    print("done")

if __name__ == "__main__":


    url1 = "https://www.youtube.com/watch?v=fk4BbF7B29w"
    url2 = "https://www.youtube.com/watch?v=niG3YMU6jFk"
    url3 = "https://www.youtube.com/watch?v=cii6ruuycQA"
    url4 = "https://www.youtube.com/watch?v=gBRi6aZJGj4"
    url5 = "https://www.youtube.com/watch?v=bo9Z_pgByQY"

    init_time = time.time()

    service(url1, url2, url3, url4, url5)

    end_time = time.time() - init_time
    print(end_time)
