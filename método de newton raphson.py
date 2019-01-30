# Newton- Raphson
"""
Created on Mon Jan 14 16:50:21 2019

@author: Ednildo Cunha
"""

import math

def newton(f):
    p0 = float(input("Chute inicial: "))
    E = float(input("Erro (em forma decimal): "))
    n = int(input("Número máximo de iterações: "))
    k = 1
    while k <= n:
          
        p = p0-f(p0)/df(p0)    # Primeira iteração 
        if abs(p-p0) < E:
            print (p)
            break
        k = k+1
        p = p0        #atualiza o Xi
        
        if k > n:
            print ("O método falhou após ",n," iterações.")           
            break
#Função
f= lambda x: x**2+math.cos(x)
#derivada da função
df= lambda x: 2*x-math.sin(x)

newton(f)