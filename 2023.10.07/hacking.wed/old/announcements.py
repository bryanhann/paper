import time
import sys
PAPER="Paper the Great!"
BRYAN="Bryan the Magnificent!!!"
BACKUP="\b"*1000


ROBOT="X"
SPACE="----------------------------"

def

def write(x):
    print(x,end="")
    sys.stdout.flush()

def announce():
    for ch in PAPER:
        write(ch)
        time.sleep(0.1)

    numchars=len(PAPER)
    for ii in range(numchars):
        write("\b")
        time.sleep(0.1)


    for ch in BRYAN.upper():
        print( ch, end="" )
        sys.stdout.flush()
        time.sleep(.1)
    time.sleep(3)




def _show():
    backup="\b"*100
    for ii in range(len(paper)+1):
        print( backup + paper[:ii] , end="")
        time.sleep(.1)
        sys.stdout.flush()
    time.sleep(5)
    for ii in range(len(bryan)+1):
        print( backup + bryan[:ii] , end="")
        time.sleep(1)
        sys.stdout.flush()

