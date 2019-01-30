import math


def a(x):
    return math.exp(x)

def a(x):
    return x*math.log(x)

def b(x):
    return (x**3)*math.exp(x)

def c(x):
    return 2/((x**2)+4)

def d(x):
    return (x**2)*math.cos(x)

def e(x):
    return math.exp(2*x)*math.sin(3*x)

def f(x):
    return x/(x**2 +4)

def g(x):
    return 1/(math.sqrt((x**2)-4))

def h(x):
    return math.tan(x)

    

def trapezioIntegral(n,x0, xn, f):
    if n<0:
        print("Divisão por zero")
    else:
        if n<0:
            print("Intervalo Inválido")
        else:
            h = (xn-x0)/n
            x = x0+h
            soma = 0
            for i in range(n-1):
                soma = soma + f(x)
                x = x + h
            R = h*((f(x0) + f(xn))/2 + soma)
            print("O Resultado da integral da função é", R)

#Execicios pagina 210, Cap 4, questão 1 do Burden. Respostas pag 793

print("letra A")
trapezioIntegral(4, 1,2, a)
print("letra B")
trapezioIntegral(4, -2,2, b)
print("letra C")
trapezioIntegral(6, 0,2, c)
print("letra D")
trapezioIntegral(6, 0,math.pi, d)
print("letra E")
trapezioIntegral(8, 0,2, e)
print("letra F")
trapezioIntegral(8, 1,3, f)
print("letra G")
trapezioIntegral(8, 3,5, g)
print("letra H")
trapezioIntegral(8, 0,3*math.pi/8, h)
