# Método da Bissecção
"""
Created on Mon Jan 14 16:30:44 2019

@author: Ednildo Cunha
"""
import math
def Bissec(f):
    a = float(input("Ponto mínimo do intervalo: "))
    b = float(input("Ponto máximo do intervalo: "))    
    E = float(input("Erro (em forma decimal): "))
    n = int(input("Número máximo de iterações: "))
    i=1
    M = f(a)
    while i <= n:
        xi =(a+b)/2   #Calcular Xi
        fx = f(xi)
        if ((fx==0) or ((a-b) < E)):
            print (xi," O procedimento foi bem sucedido")
            break
        i=i + 1
        if M*fx<0:
            b=xi #calcula ai, bi
        else:
            a=xi
            M=fx
            print ("O método falhou após ",n," iterações.")           
            break
f= lambda x: ((x**2)-1)
Bissec(f)#Intervalo: [0 , 100]