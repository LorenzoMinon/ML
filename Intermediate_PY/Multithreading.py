import threading


def funcion1():
    for i in range(0,10000):
        print("Hello from funcion1")

def funcion2():
    for i in range(0,10000):
        print("Hello from funcion2")

# Creating threads

t1 = threading.Thread(target=funcion1)
t2 = threading.Thread(target=funcion2)

# Starting threads

t1.start()
t2.start()

#USAR EL METODO JOIN PARA QUE ESPERE A QUE TERMINE EL THREAD.