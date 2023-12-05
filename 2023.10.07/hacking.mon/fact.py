#def assert_nat(n):
from math import factorial


print(factorial(52))

def test(fn):
    # fn should be factorial.
    for n in range(10):
        assert fn(n)==fact(n)
    for n in [-1, 2.0, 'x']:
        try:
            assert fn(n)# ==None
        except ValueError:
            print(f'bad value: {n}')
        except TypeError:
            print(f'bad type: {n}')

test(factorial)
212/0
def isnat(n):
    if not type(n)==type(1): return False
    if n < 0: return False
    return True

def fact(n):
    assert isnat(n)
    if n==0: return 1
    else:    return n * fact(n-1)



def fact_proxy(IN):
    return fact(IN)

def wrapper(fn_original):
    def fn_proxy(arg):
        return fn_original(n)
    return fn_originalfn2
safefact=wrapper(fact)

#def require_nat(fn):
#    def safe_fn(n):




def _facnt(n):
    if n==1: return 1
    if n > 1: return n*fact(n-1)
    return
    if n==2: return 2 * fact(1)
    if n==3: return 3 * fact(2)
    if n==4: return 4 * fact(3)
    #if n==5: return 5 * fact(4)
    if n==5: return n * fact(n-1)
    if n==6: return n * fact(n-1)
    if n > 6: return n * fact(n-1)
for ii in range(10):
    print( ii, fact(ii) )
