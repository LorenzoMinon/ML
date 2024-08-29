import threading
import time

#Two threads. One is going to double a number and the other is going to divide it by 2.

x = 8192
lock = threading.Lock()


def double():
    global x # I have a variable x outside the function and I want to modify it.
    lock.acquire() # I want to lock the variable x, so the other thread can't modify it.
    while x < 16384: # I want to double x until it reaches 16384
        x *= 2 # Double x
        print(x) 
        time.sleep(1) # Sleep for 1 second, so the other thread can run. So it can divide x by 2. And then this thread can double x again.
    print("Reached the maximum value.")
    lock.release() # Release the lock, so the other thread can run.

def halve():
    global x 
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)
    print("Reached the minimum value.")
    lock.release()

t1 = threading.Thread(target=double)
t2 = threading.Thread(target=halve)

t1.start()
t2.start()


#Semaphore
#Semaphore is a synchronization object that controls access by multiple
#processes to a common resource in a parallel programming environment.

semaphore = threading.BoundedSemaphore(value=3) # I want to limit the number of threads that can access the resource to 3.

def access(thread_number):
    print(f"Thread-{thread_number} is trying to acquire the semaphore.")
    semaphore.acquire() # I want to acquire the semaphore.
    print(f"Thread-{thread_number} has acquired the semaphore.")
    time.sleep(10) # Sleep for 5 seconds.
    print(f"Thread-{thread_number} is releasing the semaphore.")
    semaphore.release() # I want to release the semaphore.

for thread_number in range(1,11):
    t = threading.Thread(target=access, args=(thread_number,))
    t.start()
    time.sleep(1) # Sleep for 1 second, so the next thread can start.   

