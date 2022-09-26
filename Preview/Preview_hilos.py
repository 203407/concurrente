from threading import Thread
import threading
import time
import requests

def checkStatus(url):
    response = requests.head(url)
    if response.status_code == 200:
        print(f'{url} - Estatus: Pagina activa')
    else:
        print(f'{url} - Estatus: Pagina inactiva')

class Hilo(threading.Thread):
    def __init__(self, id,url):
        Thread.__init__(self)
        self.id=id
        self.url=url

    def run(self):
        checkStatus(self.url)

x=1;
data= ['https://classroom.google.com','https://github.com','https://www.xbox.com/es-MX','https://www.playstation.com/es-mx/',
            'https://twitter.com/','https://www.reddit.com','https://es-la.facebook.com','https://www.youtube.com',
            'https://www.figma.com/signup','https://trello.com/es/login','https://jsonplaceholder.typicode.com','https://my.freenom.com',
            'https://www.w3schools.com','https://support.microsoft.com/','https://www.nvidia.com/es-la/','https://www.amd.com/es',
            'https://www.amazon.com.mx','https://mx.msi.com','https://www.minecraft.net/es-es','https://store.steampowered.com/?l=spanish',
            'https://www.epicgames.com/site/es-ES/home','https://playvalorant.com/es-mx/','https://genshin.hoyoverse.com/pc-launcher',
            'https://www.ea.com/es-es/games/apex-legends','https://www.leagueoflegends.com/es-mx/'
            
    ]


while True:

    for t in data:        
        hilo = Hilo(x,t)
        hilo.start()
        x+=1

    x = 1
    time.sleep(10)
    print('\n')