BRYAN="BRYAN"
SARAH="SARAH"
BLANK="-----"
def init():
    global HALL
    HALL = [ BRYAN, BLANK, BLANK, BLANK, SARAH ]
def show():
    wall = "|"
    pic = wall + wall.join(HALL) + wall
    print(pic)
def swap(m,n):
    HALL[m], HALL[n] = HALL[n], HALL[m]
    show()

def rstep(n):
    if HALL[n+1]==BLANK:
        swap(n,n+1)
    else:
        print "Cannot step"
        show()
init()
