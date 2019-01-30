# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 18:44:46 2019

@author: Ednildo Cunha
"""

x = [1.0, 1.3, 1.6, 1.9, 2.2]
y = [ 0.7651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623]
p = 1.5 #ponto para interpolar


def neville(x, y, p):
    """Entrada: lista com Xs e Ys
       Saída: Tabela e F(x) no ponto dado"""
    n = len(y)
    Q = [[0 for i in range(n)] for j in range(n)]
    for i, el in enumerate(y):
        Q[i][0] = el

    for i in range(n):
        for j in range(i):
            j+=1
            Q[i][j] = ((p-x[i-j]) * Q[i][j-1] - (p-x[i]) * Q[i-1][j-1])/(x[i] - x[i-j])
            
    return Q, Q[-1][-1]

Qs, Qnn = neville(x,y,p)


for i in Qs:
    print(i)

print(Qs)

print("Qnn: ",Qnn)