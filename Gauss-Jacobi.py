# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 18:47:45 2019

@author: Ednildo Cunha
"""
a1= [[10.0, -1.0, 2.0, 0.0, 6.0],
    [-1.0, 11.0, -1.0, 3.0, 25.0],
    [2.0, -1.0, 10.0, -1.0, -11.0],
    [0.0, 3.0, -1.0, 8.0, 15.0]]



def jacobi(M, erro, iteracao):
    '''
    Entradas: matriz aumentada, erro, e quantidade de iterações. 
    Saídas: Vetor solução do sistema ou mensagem de erro'''
    n = len(M)
    on = True
    cont = 0
    # Extrair o vector b
    b = [0 for i in range(n)]
    for i in range(0,n):
        b[i]=M[i][n]
    #Criar vetor x0
    x0 = [0 for i in range(n)]
    for i in range(n):
        x0[i] = b[i]/M[i][i]
    #Cria vetor x1
    x1 = [0 for i in range(n)]
    while on == True:
        cont+=1
        #Realiza a substituição do sistema
        for i in range(n):
            x1[i] = b[i]
            for j in range(0,n):
                if j!=i:
                    x1[i] -= M[i][j]*x0[j]
            x1[i] = x1[i]/M[i][i]

        print('x1: ', x1)
        #Vetor Diferença X1 -x0
        Vdif = [abs(x1[i] - x0[i]) for i in range(n)]
        #d p/ o criterio de parada
        temp = [abs(x1[i]) for i in range(n)]
        d = max(Vdif)/max(temp)
        if d<erro or cont==iteracao:
            on = False
            print(x1)
            print("Número de iterações: ", cont)
        if cont>iteracao:            
            print("Número de iterações insuficiente para encontrar o conjunto solução")
            break
        x0 = x1[:]


jacobi(a1,10**(-100), 1000)
