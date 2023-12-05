SAVE=f"\033[s"
RESTORE=f"\033[u"
CLEAR=f"\u001b[2J"

class Robot: pass
PAPER=Robot()
PAPER.row=0
PAPER.col=0
PAPER.ch='P'
PAPER.name="Paper"
def _about(rob):
    for item in rob.__dict__.items():
        print(item)
def _setrc(rob,row,col):
    rob.row=row
    rob.col=col

def _write(rob):
    r=rob.row
    c=rob.col
    rcwrite(r,c,rob.ch)
def clock():
    #threading.Timer(1.0, clock).start()
    print('\033[0;0H' + time.asctime(time.localtime()))

def rcwrite(row,col,ch):
    MOVE=f'\033[{row};{col}H'
    print(SAVE + MOVE + ch + RESTORE, end="")
    sys.stdout.flush()

def diag():
    print(CLEAR)
    for ii in range(10):
        lcset(ii,ii,"X")
