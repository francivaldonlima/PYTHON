#coding: utf-8
import time
import random 

numeros = []
megasena = 5
numeros_sorteados = 1

while (megasena >= len(numeros)):
    n = random.sample(range(1,60), 1)
    
    print ("O" , numeros_sorteados,"° NÚMERO FOI " , n)
    
    if (n in numeros):
        print("O" , numeros_sorteados ,"° NÚMERO ESTA REPETIDO " , n)

    if (n not in numeros):
        numeros.append(n)
           
    numeros_sorteados = numeros_sorteados + 1
    time.sleep(1)
    
print("OS NÚMEROS SORTEADOS NA ORDEM DE SORTEIO SÃO :" , numeros)
numeros.sort()
print("OS NÚMEROS SORTEADOS NA ORDEM CRECENTE SÃO :" , numeros)
