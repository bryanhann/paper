RED="\x1b[31m"
NORMAL="\x1b[0m"
#print("\x1b[31m\"red\"\x1b[0m#")
#print("\x1b[32m\"red\"\x1b[0m")
#print("\x1b[33m\"red\"\x1b[0m")
#print( RED+"hello" + NORMAL )


def nat(n):
    assert n >= 0
    return list(range(n))
def isempty(x):
    assert type(x) == type( [] )
    return x==[]
def head(mylist): return mylist[0]
def tail(mylist): return mylist[1:]
def size(x):
    if isempty(x):
        return 0
    return 1 + length(tail(x))
def reverse(x):
    if isempty(x):
        return []
    return reverse( tail(x) ) + [head(x)]
def lsum( x ):
    if isempty(x):
        return 0
    else:
        return head(x) + lsum(tail(x))

assert length( [] ) == 0
assert length( [None] ) == 1
assert length( [None]*2 ) == 2

assert lsum( []  ) == 0
assert lsum( [0] ) == 0
assert lsum( [2,3] ) == 5
assert lsum( [2,-7,3] ) == -2
assert reverse( [0,1,2,3] ) == [3,2,1,0]
