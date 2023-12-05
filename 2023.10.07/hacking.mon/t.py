import sys
import random
from COLORS import fore, back, util, bg
for ff in range(8):
    for bb in range(8):
        print( fore(ff) + back(bb) + f"{ff,bb}" )
print(util.reset)
for ii in range(2000):
    ff=random.randrange(8)
    bb=random.randrange(8)

    r=random.randrange(255)
    g=random.randrange(255)
    b=random.randrange(255)
    ch = " "
    rgb=(r,g,b)
    sys.stdout.write( bg.rgb(r,g,b) + repr(rgb) + util.reset )
    continue

for ii in range(256):
    ch=" "
    sys.stdout.write( bg.rgb(ii,ii,ii) + ch )
