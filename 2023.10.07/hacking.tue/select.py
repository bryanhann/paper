from random import randrange

def select_even(seq):
    keep = []
    for item in seq:
        if item%2==0:
            keep.append(item)
    return keep

def select_odd(seq):
    keep = []
    for item in seq:
        if item%2==1:
            keep.append(item)
    return keep

def select_gezero(seq):
    keep = []
    for item in seq:
        if item%2==1:
            keep.append(item)
    return keep


def select_even2(seq):
    def test(item): return item%2==0
    keep = []
    for item in seq:
        if test(item):
            keep.append(item)
    return keep

def select_even3(seq):
    test = lambda item : item%2==0
    keep = []
    for item in seq:
        if test(item):
            keep.append(item)
    return keep

def select_even4(seq, test=lambda item : item%2==0):
    keep = []
    for item in seq:
        if test(item):
            keep.append(item)
    return keep

def select_generic(seq, test):
    keep = []
    for item in seq:
        if test(item):
            keep.append(item)
    return keep

def select_even5(seq):
    return select_generic(seq, lambda x : x%2==0 )

def is_even(x): return x%2==0

def select_even5(seq):
    return select_generic(seq, is_even)


def select_positive_0( mylist ):
    for item in mylist:
        if item > 0:
            print( f"selected {item}" )
        else:
            print( f"rejected {item}")


def select_positive_1( mylist ):
    keep = []
    throw = []
    for item in mylist:
        if item > 0:
            print( f"selected {item}" )
            keep.append(item)
        else:
            print( f"rejected {item}")
            throw.append(item)
    print( f"keep: {keep}" )
    print( f"throw: {throw}" )
    return keep

def select_positive_3( mylist ):
    keep = []
    for item in mylist:
        if item > 0:
            keep.append(item)
    return keep


def select_positive( mylist ):
    return [ item for item in mylist if item > 0 ]

def lfilter(fn,seq): return list(filter(fn,seq))
def lrange(*a,**b):  return list(range(*a,**b))
def demo():
    print( lrange(25))
    print(select_even5( range(20) ))
    print(select_generic( range(20), is_even ))
    print(lfilter(is_even,range(20)))
    example=[]
    while len(example) < 10:
        example.append(  randrange(-10,10) )
    print(example)
    result = select_positive(example)
    print( f"result: {result}" )
