import threading
import time

path = "text.txt"
text = ""

# Count time
time1 = time.time()

def readFile():
    global path, text
    with open(path, "r") as file:
        text = file.read()
        print("File read.")
        time.sleep(5)

def printText():
    global text
    for i in range(0, 10):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=readFile, daemon=True)
t2 = threading.Thread(target=printText)

t1.start()
t2.start()

t1.join()  # Wait for t1 to finish
t2.join()  # Wait for t2 to finish

time2 = time.time()
totaltime = time2 - time1
print("Total time: ", totaltime)
