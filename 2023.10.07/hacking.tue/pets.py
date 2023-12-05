
SECRET=42

def max2( x, y ):
    if x > y:
        return x
    else:
        return y

def max3( x, y, z ):
    if x > y and x > z:
        return x
    elif y > z:
        return y
    else:
        return z

def max4( x, y, z, w ):
    if x > y and x > z and x > w:
        return x
    elif y > z and y > w:
        return y
    elif z > w:
        return z
    else:
        return w

def max4a( x, y, z, w ):
    a = max2(x,y)
    b = max2(z,y)
    return max(a,b)


def maxList( olist ):
    # "biggest" means biggist seen so far
    biggest=olist[0]
    for item in olist:
        if item > biggest:
            biggest = item
    return biggest
