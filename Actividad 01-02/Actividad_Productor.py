import threading
import queue
import time

cond = threading.Condition()

class Consumidor(threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.id=id
    
    def run(self):
        global cola;

        while True:

            cond.acquire()
            cond.wait()
            
            if cola.full():
                while cola.qsize() != 0:                    
                    print(f'\nEl Consumidor {self.id} esta consumiendo {cola.get()}')
                    time.sleep(1)
                    cola.get()
            cond.notify()
            cond.release()


class Productor (threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)        
        self.id=id

    def run(self):
        global cola;

        while True:

            cond.acquire()

            if cola.full():
                print(f'Productor {self.id} ha dejado de producir')
                cond.wait()            

            cola.put(1)
            print(f'Productor {self.id} esta produciendo')

            time.sleep(1.5)
            cond.notify()
            cond.release()



if __name__ == '__main__':
    cola = queue.Queue(10)      

    for x in range(0,5):        
        consumidor = Consumidor(x)
        productor = Productor(x)

        consumidor.start()
        productor.start()        
    