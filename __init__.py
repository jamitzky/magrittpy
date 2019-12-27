class forall:
    def __init__(self,*args):
        self.args=args
    def __rshift__(self,other):
        if other == result:
            return self.args[0]
        elif callable(other):
            return forall(other(*self.args))

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

m1 =\ 
forall(10)>>\ 
    range >>\
    flatmap(lambda x:x**2) >>\
    (sum|div|len) >>\ 
    result
