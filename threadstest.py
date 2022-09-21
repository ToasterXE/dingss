from threading import Thread
from time import sleep

def f(counter):
    sleep(1)
    print (counter)
Liste = []
counter = 0
for counter in range(0,10):
    t1 = Thread(target = f(counter), name = "t" + str(counter))
    counter += 1
    Liste.append(t1)
for t1 in Liste:
    t1.start()

for t1 in Liste:
    t1.join()

print ("ee")