#coding: utf-8
import random
for item in range(30):
    #list=[random.randint(0, 10) for _ in range(4)]
    list = random.sample(range(1,30), 10)
    list.sort()
    print(list)
