import random
import matplotlib.pyplot as plt
starting_amount=10000
i=0
l=[]
while i<1000 and starting_amount>=100:
    a=random.randint(1, 37)
    b=random.randint(1, 37)
    if(a==b):
        starting_amount+=360*10
        print(f" {i}: +360 до балансу, Баланс:{starting_amount}")
        l.append(starting_amount)
    else:
        starting_amount-=100
        print(f" {i}: -100 до балансу, Баланс:{starting_amount}")
        l.append(starting_amount)
    i+=1
plt.plot(l)
plt.show()