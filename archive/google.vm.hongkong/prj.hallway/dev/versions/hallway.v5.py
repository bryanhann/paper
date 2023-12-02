#!/usr/bin/env python3

class BOARD:
    def __init__(self, size=10):
        self._size = size
        self._players = []
        self.update()
    def cell4room(self, room):
        cellsize=6
        occupant = self._board[room]
        if occupant is None:
            return "-" * cellsize
        else:
            return occupant.name(cellsize)
            return (occupant._name + ' '*cellsize)[:6]

    def update(self):
        self._board = [None] * self._size
        for player in self._players:
            if player.room() is not None:
                self._board[player.room()]= player


        cells = [ self.cell4room(ii) for ii in range(len(self._board)) ]
        print( '[' + '|'.join(cells) + ']' )
    def add_player(self,player):
        self._players.append(player)


class Player:
    def __init__(self, name, room=None):
        self._name = name
        self._room = room # where I am assigned to be
    def room(self):
        return self._room
    def name(self, n=None):
        if n is None:
            return self._name
        else:
            return self._name[:n].center(n)
Board = BOARD()
Board.add_player( Player( 'Joe', 2 ) )
Board.update()
exit()

'''
def leave_room():
        self._room = None
        update()
    def moveto(room):
        if self._room is not None:
            ROOMS[self._room
    def _enter(self):
        self._spot = self._room
    def _exit(self):
        self._spot = None
    def _write(self):
        # write muself to my room
        HALL[ self.room ] = self
    def _erase(self)
        # erase myself from my room
        HALL[ self.room ] = self
    def _change(self, room):
        """Change to a new roomroom"""
        self.room = room
    def __repr__(self):
        return f"<{self.__class__.__name__} room={self._room} spot={self._spot}"

    def change(self, room):
        """Move myself to a new room"""
        self._erase()
        assert ROOM[ self.exit_room(
        _Insert_Self( player ):
    BOARD[ playergoto(n):
    :
    player_

BRYAN={}
BRYAN.name="BRYAN"
BRYAN.room=0

PAPER={}
PAPER.name="PAPER"
PAPER.room = 4

PLAYERS = [BRYAN, PAPER]
def init():
    global HALL
    HALL=[ BLANK ] * 5
    for player in PLAYERS:
        ROOM
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
'''
