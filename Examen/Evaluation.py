import threading
import time
import concurrent.futures

palijos = [threading.Lock(),threading.Lock(),threading.Lock(),threading.Lock(),
           threading.Lock(),threading.Lock(),threading.Lock(),threading.Lock()]

mutex = threading.Lock()
cont = 0

def liberar(id):

    if id != len(palijos)-1:
         if id == 0:
            palijos[id].release()
         if "locked _thread.lock" in str(palijos[id+1]):  
            palijos[id+1].release()
    else:
       if "locked _thread.lock" in str(palijos[0]):  
            palijos[0].release()   


def agarrarizq(id):
    if "unlocked _thread.lock" in str(palijos[id]): 
        palijos[id].acquire()    

        print(f'\nobtuvo palillo izquierdo: {id}')
        if id != len(palijos)-1:

            if "unlocked _thread.lock" in str(palijos[id+1]):
                palijos[id+1].acquire()
                print(f'Obtuvo los 2 palillos {id}')
                return 1
        else:
            if "unlocked _thread.lock" in str(palijos[0]):
                palijos[0].acquire()
                print(f'Obtuvo los 2 palillos {id}')
                return 1            
   

def comiendo(id):
    
    check = agarrarizq(id)
    
    if check == 1:
        print(f'comiendo {id}')
        time.sleep(2)
        print(f'termino de comer {id}')
        liberar(id)



class Comensal(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id=id

    def run(self):
        mutex.acquire()
        
        check = agarrarizq(self.id)
    
        if check == 1:
            print(f'comiendo {self.id}')
            time.sleep(2)
            print(f'termino de comer {self.id}')
            liberar(self.id)


        mutex.release()


if __name__=="__main__": 

    for x in range(0,8):
        com = Comensal(x)
        com.start()

 