class forall:
    def __init__(self,*args):
        self.args=args
    def __rshift__(self,other):
        if other == result:
            return self.args[0]
        elif callable(other):
            return forall(other(*self.args))
    def __call__(self,other):
        return self >> other

class result:
    pass

class op:
    def __init__(self,func):
        self.func=func
    def __ror__(self,other):
        self.op1=other
        return self
    def __or__(self,other):
        self.op2=other
        return self
    def __call__(self,x):
        return self.func(self.op1(x),self.op2(x))

div=op(lambda x,y:x/y)

def flatmap(f):
    return lambda x,f=f:[f(i) for i in x]

#tests:
forall(10)>>\ 
    range >>\
    flatmap(lambda x:x**2) >>\
    (sum|div|len) >>\ 
    print

m1 = forall(10) >> range >> flatmap(lambda x:x**2) >> (sum|div|len) >> result
m2=forall(10)(range)(sum)(result)

"""
import numpy
import math
from magrittpy import *
from sympy import *
x,y,z=symbols("x y z")

def lamn(expr):
    return lambdify(x,expr,"numpy")
def lamm(expr):
    return lambdify(x,expr,"math")

In [22]: %timeit forall(1000000) >> numpy.arange >> lamn(sin(x)) >> sum >> result
634 ms ± 21.3 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

In [23]: %timeit forall(1000000) >> range >> flatmap(lamn(sin(x))) >> sum >> result
3.39 s ± 765 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

In [24]: %timeit numpy.sum(numpy.sin(numpy.arange(1000000)))
91.5 ms ± 17.9 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

In [25]: %timeit forall(1000000) >> numpy.arange >> numpy.sin >> numpy.sum >> result
102 ms ± 15 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

In [27]: %timeit forall(1000000) >> range >> flatmap(lamm(sin(x))) >> sum >> result
743 ms ± 8.22 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

In [28]: %timeit sum(math.sin(x) for x in range(1000000))
597 ms ± 74.2 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

In [29]: %timeit forall(1000000) >> range >> flatmap(math.sin) >> sum >> result
442 ms ± 37.5 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

In [30]: %timeit sum([math.sin(x) for x in range(1000000)])
398 ms ± 116 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
"""
