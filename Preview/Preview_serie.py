from time import sleep
import requests
import time

def checkStatus(url):

    for x in url:
        response = requests.head(x)
        if response.status_code == 200:
            print(f'{x} - Estatus: Pagina activa')
        else:
            print(f'{x} - Estatus: Pagina inactiva')

if __name__ == '__main__':
    
    data= ['https://classroom.google.com','https://github.com','https://www.xbox.com/es-MX','https://www.playstation.com/es-mx/',
            'https://twitter.com/','https://www.reddit.com','https://es-la.facebook.com','https://www.youtube.com',
            'https://www.figma.com/sign','https://trello.com/es/login','https://jsonplaceholder.typicode.com','https://my.freenom.com',
            'https://www.w3schools.com','https://support.microsoft.com/','https://www.nvidia.com/es-la/','https://www.am.om/es',
            'https://www.amazon.com.mx','https://mx.msi.com','https://www.minecraft.net/es-es','https://store.steampowered.com/?l=spanish',
            'https://www.epicgas.com/site/es-ES/home','https://playvalorant.com/es-mx/','https://genshin.hoyoverse.com/pc-launcher',
            'https://www.ea.com/es-es/games/apex-legends','https://www.leagueoflegends.com/es-mx/'
            
    ]

    while True:
        checkStatus(data)
        time.sleep(10)