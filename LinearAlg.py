def gauss(mA):
    '''Função realiza a eliminação gaussiana através do pivoteamento parcial, recebe uma lista com uma matriz
    e retorna uma matriz simétrica reduzida'''
    n = len(mA)

    for lin in range (0, n):
        #Encontrar o maior numero dentre as colunas
        maxCol = abs(mA[lin][lin]) #Valor Maximo em uma coluna
        maxLin = lin
        for col in range(lin+1, n):
            if abs(mA[col][lin]) > maxCol:
                maxCol = abs(mA[col][lin])
                maxLin = col
                
        #Troca a linha de valor maximo pela linha atual (coluna por coluna)
        for col in range(lin, n+1):
            tmp = mA[maxLin][col]
            mA[maxLin][col] = mA[lin][col]
            mA[lin][col] = tmp

        #Zerar todas as posicoes abaixo do pivo
        for col in range(lin+1, n):
            multiplicador = -(mA[col][lin])/(mA[lin][lin])
            for j in range(lin, n+1):
                if lin == j:
                    mA[col][j] = 0
                else:
                   mA[col][j] += multiplicador*mA[lin][j]

    #print("Matriz Reduzida")
    #for i in range(n):
    #    print(mA[i])
    return mA


def retrosubs(mT):
    '''Função recebe uma matriz já reduzida e retorna o conjunto solução através do método de retrosubsituição'''
    n = len(mT)
    x = [0 for i in range(n)]
    for lin in range(n-1, -1, -1):
        x[lin] = mT[lin][n]/mT[lin][lin]
        for k in range(lin-1, -1, -1):
            mT[k][n] -= mT[k][lin] * x[lin]
    return x
