import os

lista = ["through", "Learn", "their" , "shortest"]

for i in range(len(lista)):
    print(lista[i])
    a=lista[i]
    f = os.popen('trans -b '+a)
    now = f.read()
    print (now)
