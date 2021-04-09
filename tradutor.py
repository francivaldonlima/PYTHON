#coding: utf-8
# um tradutor usando do tradutor do linux translate-shell
#https://www.soimort.org/translate-shell/
import os

lista = ["through", "Learn", " their" , "shortest"]

for i in range(len(lista)):
    print(lista[i])
    a=lista[i]
    b="trans -b "
    x=b + a
    os.system(x)
    
     


