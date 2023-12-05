from COLORS import fg, bg, util
import time
import sys
def red(x):   return   fg.red   + util.bold + x + util.reset
def green(x): return   fg.green + util.bold + x + util.reset

BRYAN="BRYAN"
SARAH="SARAH"
EMPTY="-----"

PLAYERS=[BRYAN,SARAH]

def init ():
    global HALL
    HALL = [BRYAN,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,SARAH]
    show()

def picture():
    sep = '|'
    numbers = list(range(len(HALL)))
    key = [ repr(x).center(5) for x in numbers ]
    key = sep + sep.join(key) + sep
    print(key)
    return sep + sep.join(HALL) + sep

def show():
    print( picture() )

def swap(m,n):
    HALL[m], HALL[n] = HALL[n], HALL[m]
    #show()

def rstep(n):
    assert HALL[n] in PLAYERS
    assert HALL[n+1] == EMPTY
    swap(n, n+1)

def index(player):
    assert player in PLAYERS
    return HALL.index(player)

def rstep4player(player):
    rstep( index(player) )


def rwalk4player(player):
    print()
    while True:
        print(util.up + picture() )
        time.sleep(1)
        try:
            rstep4player(player)
        except AssertionError:
            break

init()
