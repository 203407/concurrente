from threading import Thread, Semaphore
from turtle import st
semaforo = Semaphore(1) # Crea la variable semáforo
import requests

def crito(id,url):
    global x;
    x = x + id

    f = open(f'{id}.jpg','wb')
    response = requests.get(url)
    f.write(response.content)
    f.close()
    print("Hilo =" +str(id)+ " =>" + str(x))
    print("donwloaded image")
    x=1

class Hilo(Thread):
    def __init__(self, id, url):
        Thread.__init__(self)
        self.id=id
        self.url=url

    def run(self):
        semaforo.acquire() #Inicializa semáforo , lo adquiere
        crito(self.id, self.url)
        semaforo.release() #Libera un semáforo e incrementa la varibale semáforo


threads_semaphore = [Hilo(1,'https://www.diariotiempo.com.ar/wp-content/uploads/2022/09/7c39aef987d371f20296a470018ad56b5f47c6b6-1920x1080.jpg'), Hilo(2,'https://images.ctfassets.net/rporu91m20dc/7dHtxlgFeEa0UAes80Ss0i/d6ddd7957c71d4bd76fefd62d4e9cdfe/doom-mobile-hero.jpg?q=70'), 
                    Hilo(3,'https://eu-images.contentstack.com/v3/assets/blt95b381df7c12c15d/blt50a903bf10d75db1/6324b2d484a575440c120aef/edge.jpg'),  Hilo(4,'https://as01.epimg.net/meristation/imagenes/2015/06/15/album/1434346020_346020_000001_album_normal.jpg'), 
                    Hilo(5,'https://phantom-marca.unidadeditorial.es/b65977c8cb5f7ce81da2cc7159fb8bfd/crop/152x0/1598x964/resize/1320/f/jpg/assets/multimedia/imagenes/2022/09/13/16630831830322.jpg'),
                    Hilo(7,'https://static1-es.millenium.gg/articles/9/50/13/9/@/274988-edgerunners-amp_main_media-1.jpg'),  Hilo(8,'https://cdn.cloudflare.steamstatic.com/steam/apps/379720/ss_28e126c5530b5f81726501ec73e51c66fd325bc2.1920x1080.jpg?t=1593395083'), 
                    Hilo(9,'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpygM3ISJ4dIkAtbLn1DtSxrPDelvx91hUSQ&usqp=CAU'),  Hilo(10,'https://as01.epimg.net/meristation/imagenes/2020/01/22/noticias/1579694516_593337_1579694561_noticia_normal.jpg')]

x=1;
for t in threads_semaphore:
    t.start()