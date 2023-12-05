def lmap(fn,seq): return list(map(fn,seq))

def apply_div3(seq):
    acc=[]
    for item in seq:
        acc.append( item%3==0 )
    return acc

def apply_square(seq):
    acc=[]
    for item in seq:
        acc.append( item*item )
    return acc

def apply_square(seq):
    fn = lambda x : x*x
    acc=[]
    for item in seq:
        acc.append( fn(item))
    return acc

def apply_square(seq, fn=lambda x : x*x ):
    acc=[]
    for item in seq:
        acc.append( fn(item))
    return acc

def square(x):
    """Squares its input"""
    return x*x

def apply_square(seq, fn=square ):
    acc=[]
    for item in seq:
        acc.append( fn(item))
    return acc

def apply_generic(seq, fn):
    acc=[]
    for item in seq:
        acc.append( fn(item))
    return acc

def apply_square(seq):
    return apply_generic(seq,square)

def apply_square(seq):
    return lmap(square,seq)

print( apply_is_even(range(10)) )
print( apply_square(range(10)) )

