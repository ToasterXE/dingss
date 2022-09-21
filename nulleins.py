import random
counter = 0
string="0"
while counter < 1000:
    string += str(random.randint(0,1))
    counter += 1
print (string)