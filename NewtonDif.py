#Exemplo Pagina 121 Burden - Capitulo 3
x = [1.0, 1.3, 1.6, 1.9, 2.2]
y = [ 0.7651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623]
p = 1.5 #ponto para interpolar


def NewtonDiferenca(x, y):
    '''Recebe um vetor x e um vetor y que é f(x)
    retorna a tabela'''
    n = len(y)
    F= [[0 for i in range(n)] for j in range(n)]
    for i, el in enumerate(y):
        F[i][0] = el


    for i in range(n):
        for j in range(i):
            j+=1
            F[i][j] = (F[i][j-1]-F[i-1][j-1])/(x[i]-x[i-j])
    return F

F = NewtonDiferenca(x,y)


def P(F, p, x):
    """Função para encontrar a f(x) no ponto dado"""
    p_x = 0
    for i in range(len(F)):
        prod = 1
        for j in range(i):
            prod *= (p -x[j])
        p_x += F[i][i] * prod
    return p_x

for i in F:
    print(i)

print(P(F, p, x))
