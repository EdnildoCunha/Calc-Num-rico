from LinearAlg import gauss, retrosubs


#Xi = [1,3,4,6,8,9,11,14]
#Yi = [1,2,4,4,5,7,8,9]

Xi=[1,2,3,4,5,6,7,8]
Yi=[0.5,0.6,0.9,0.8,1.2,1.5,1.7,2.0]

def ponto(a0, a1, x):
    y = a1*x + a0
    return y

def MinimosDiscretoLinear(Xi, Yi):
      # Entrada: Xi, Yi, é montado uma tabela com os seguintes valores
      # Xi, Yi, Xi², Xi*Yi e seus somatórios para encontrar o alfa da equação
      # Saída:  os Alfas e a expressão
    n = len(Xi)
    tabela = [[0 for i in range(n+1)] for i in range(4)]
    listaSoma = [0 for i in range(4)]
    for i in range(n):
         tabela[0][i] = Xi[i]
         tabela[1][i] = Yi[i]
         tabela[2][i] = Xi[i]**2
         tabela[3][i] = Xi[i]*Yi[i]
    for i in range(4):
        soma = 0
        for j in range(n):
            soma += tabela[i][j]
        tabela[i][-1] = soma
    for i in tabela:
        print(i)
    a0 = (tabela[2][-1]*tabela[1][-1]-tabela[3][-1]*tabela[0][-1])/(n*tabela[2][-1]-(tabela[0][-1])**2)
    a1 = (n*tabela[3][-1]-tabela[0][-1]*tabela[1][-1])/(n*tabela[2][-1]-(tabela[0][-1]**2))
    print("os alfas são: ")
    print("a0: ", a0)
    print("a1: ", a1)
    if a0>0:
        print("f(x) = {}x + {}".format(a1, a0))
    else:
        print("f(x) = {}x{}".format(a1, a0))

        
    
MinimosDiscretoLinear(Xi,Yi)


#x = [0.4,0.5,0.6,0.7,0.8]
#y = [1.75,1.34,1.00,0.74,0.56]
x=[1,2,3,4,5,6,7,8]
y=[0.5,0.6,0.9,0.8,1.2,1.5,1.7,2.0]
def somatorio(Xi, n, Yi=None):
    if Yi == None:
        return sum(pow(x,n) for x in Xi)
    return sum(y*pow(x,n) for y,x in zip(Yi, Xi))
               
def MinimosDiscretosPoli(Xi, Yi, n):
    #Entradas: Xi, Yi sao pontos e n é o grau da equação polinomial
    #Saídas = Os alfas da equação, caso a equação seja de segundo grau, imprime-se a expressão
    m = len(Xi)
    A = [[0 for i in range(n+1)] for i in range(n+1)]
    for j in range(n+1):
        for i in range(n+1):
            A[i][j] = somatorio(Xi, i+j)
    B = [somatorio(Xi, i, Yi) for i in range(n+1)]
    Aum = [[0 for i in range(n+2)] for i in range(n+1)]
    Aum = A[:]
    for i in range(n+1):
        Aum[i].append(B[i])
    print("-----------------------")
    alfas = retrosubs(gauss(Aum))
    print("os alfas são: ")
    for i, alfa in enumerate(alfas):
        print("a{} = ".format(i), alfa)
    if n==2:
        print("f(x) = {}x² +{}x + {}".format(alfas[2], alfas[1], alfas[0]))
    
MinimosDiscretosPoli(x, y,2)