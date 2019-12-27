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

#tests:
assert( 285 == forall(range(10)) >> (lambda x:[i**2 for i in x]) >>sum >> result)
