
def rect(base,height):
    NEWLINE="\n"
    BRICK='#'
    FLOOR=BRICK*base
    FLOORS=[FLOOR]*height
    print(FLOORS)
    rect = NEWLINE.join(FLOORS)
    return rect
