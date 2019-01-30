import sympy as sp
from scipy.integrate import quad
import numpy as np

x = sp.symbols('x')
def g1(x):
    return 1
def g2(x):
    return x
intervalo = (x,0,1)
def f(x):
    return 4*(x)**3
    
def minimoContinuo(f, g1,g2, i1, i2):
    def a1(x):
        return g1(x)*g1(x)
    a11 = float(quad(a1, i1, i2)[0])
    def a2(x):
        return g1(x)*g2(x)
    a12 = float(quad(a2, i1, i2)[0])
    a21 = a12
    def a3(x):
        return g2(x)*g2(x)
    a22 = float(quad(a3, i1, i2)[0])
    def b(x):
        return f(x)*g1(x)
    b1 = float(quad(b, i1, i2)[0])
    def b3(x):
        return f(x)*g2(x)
    b2 = float(quad(b3, i1, i2)[0])

    A = [[a11, a12],
         [a21,a22]]
    B = [b1,b2]

    a0, a1 = np.linalg.solve(A,B)
    print("Os alfas são: ")
    print("a0: ",round(a0,2),"a1: ",round(a1,2))
    print("f(x) = {}x {}".format(round(a1,2),round(a0,2)))

#Exemplo5 Ruggiero pag281 pdf294
minimoContinuo(f, g1,g2,0,1)
