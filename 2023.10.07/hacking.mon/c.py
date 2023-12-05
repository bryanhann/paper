NIL = None
def cons(car,cdr): return (car, cdr)
def car(cons): return cons[0]
def cdr(cons): return cons[1]
def nil(cons): return cons is NIL

ZERO=NIL
ONE=cons(NIL,ZERO)
TWO=cons(NIL,ONE)
THREE=cons(NIL,TWO)

def nat(n):
    if n==0: return NIL
    else: return cons(NIL, nat(n-1))

for n in range(5):
    c = nat(n)
    l = aslist(c)
    s = size(c)
    print( n, l, s )

print( 0, ZERO, cons_length(ZERO) )
print( 1, ONE, cons_length(ONE) )
print( 2, TWO, cons_length(TWO) )
print( 3, THREE, cons_length(THREE) )
print( aslist(THREE) )
input('333')
ONE=cons(1,ZERO)
TWO=cons(2,ONE)
def succ(N):
    cons( car(N)+1, N )
THREE=succ(TWO)

print( TWO, cons_length(TWO) )
print( THREE, cons_length(THREE) )
def cons_length(c):
    if nil(c): return 0
    return 1 + cons_length( cdr(c) )

def ordinal(n):
    assert int(n) >= 0
    if n==0:
        return pair(n, NIL )
    else:
        return pair( n, ordinal(n-1) )

def reverse(L):
    if L is None: return L

    return pair( reverse(right(L)), left(L) )
def aslist(L):
    if not L:
        return []
    if L:
        return [left(L)] + aslist(right(L))
five=ordinal(5)
print(five)
print(aslist(five))

def fromList( olist ):
    acc=NIL
    for item in olist:
        acc = pair(item,acc)
    return acc
#print(aslist(reverse(five)))
print(fromList( range(5) ))
print(five)
#print(reverse())
