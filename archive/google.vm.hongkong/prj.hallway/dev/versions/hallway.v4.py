#!/usr/bin/env python3
if 1:
    BRYAN="BRYAN"
    PAPER="PAPER"
    BLANK="....."
    HALL=[ BRYAN, BLANK, BLANK, BLANK, PAPER ]

def init():
    global HALL
    HALL=[ BRYAN, BLANK, BLANK, BLANK, PAPER ]

def show ():
    # Print a nicely formatted picture of the game's state.
    print( '[' + '|'.join(HALL) + ']')


def inspect (n):
    # Take a room number; report its occupant.
    try:
        occupant=HALL[n]
    except IndexError:
        print("Bad room number" )
        return
    print( f"Room {n} contains {occupant}" )

def swap (m,n):
    # Take two room numbers and swap their occupants
    global HALL
    try:
        HALL[m], HALL[n] = HALL[n], HALL[m]
    except IndexError:
        print("Bad room numbers" )
        return
    show()

def step_right (n):
    # Take a room mumber, and move it occupant one room to the right.
    global HALL
    try:
        occupant = HALL[n]
        if occupant == BLANK:
	        print( "a blank cannot step right")
        else:
            HALL[n], HALL[n+1] = BLANK, occupant
            print( f"{occupant} has stepped right from room {n} to room {n+1}" )
    except IndexError:
        print("Bad room numbers" )
    show()
show()

