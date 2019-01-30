# Cholesky
"""
Created on Wed Jan 30 15:41:04 2019

@author: Ednildo Cunha
"""
def transposta(a):
    # Função para transpor uma matriz
    n = len(a)
    transposta = [[0 for i in range(n)] for i in range(n)]
    # itera pelas linhas
    for i in range(n):
        # itera pelas colunas
        for j in range(len(a[0])):
            transposta[j][i] = a[i][j]
    return transposta


def matrizCoef(A):
    n = len(A)
    mC = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(A[i][j])
        mC.append(l)
    return(mC)


def retroSuperior(a, y):
    n = len(a)
    x = [0 for i in range(n)]
    for i in range(n-1,-1,-1):
        soma = y[i]
        for k in range(i+1,n):
            soma = soma - a[i][k]*x[k]
        x[i] = soma/a[i][i]
    return x



def retroInferior(a, b):
    #Recebe como entrada uma matriz triangular inferior e um vetor B , retorna um vetor y
    n = len(a)
    y = [0 for i in range(n)]
    for i in range(0,n,1):
        y[i] = b[i]
        for k in range(0,i,1):
            y[i] -= y[k]*a[i][k]
        y[i] = y[i]/float(a[i][i])
    return y
    

c1 = [[4,12,-16,1],
     [12,37,-43,2],
     [-16,-43,98,3]
     ]


def choleskyX(a):
    #Função que recebe uma matriz aumentada, faz a fatoração de cholesky e retorna o vetor solução X

    #Calcula matriz dos coeficientes
    mC = matrizCoef(a)

    #Extrai o vetor b
    b = [0 for i in range(len(a))]
    for i in range(0,len(a)):
        b[i]=a[i][len(a)]
    n = len(mC)
    g = [[0 for i in range(n)] for i in range(n)]
    for k in range(0,n):
        soma = 0
        #Calcula gkk ou elemento da diagonal
        for j in range(0, k):
            soma = soma + (g[k][j])**2
        r = mC[k][k] - soma
        g[k][k] = (r)**(1/2)
        #Calcula elementos abaixo da diagonal ou gik
        for i in range(k+1, n):
            soma = 0
            for j in range (0, k):
                soma = soma + g[i][j]*g[k][j]
            g[i][k] = (mC[i][k] - soma)/g[k][k]

    print("Matriz G")
    for i in range(n):
        print(g[i])
    #Descobre o vetor Y através de G*Y = b
    y = retroInferior(g,b)
    #Descobre o vetor X atravé de gT*X = y
    gT = transposta(g)
    x = retroSuperior(gT,y)
    print("Vetor solução X:")
    print(x)