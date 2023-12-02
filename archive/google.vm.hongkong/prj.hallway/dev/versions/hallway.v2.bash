#!/bin/bash

# https://tldp.org/HOWTO/Bash-Prompt-HOWTO/x329.html

NC='\033[0m'     # No Color
BR='\033[1;31m'  # Bold Red
BG='\033[1;32m'  # Bold Green


function start-hallway-game () {
    # Initize the state of the game.
    export BRYAN=" ${BR}BRYAN${NC} "
    export PAPER=" ${BG}PAPER${NC} "
    export EMPTY=" ----- "
    export BLANK=" ----- "
    export HALL=( $BRYAN $EMPTY $EMPTY $EMPTY $PAPER )
    show 
}

function show () {
    # Print a nicely formatted picture of the game's state.
    echo -n "|"
    for item in ${HALL[@]}; do
	echo -n -e "${item}|"
    done
    echo -n "   (${#HALL[@]} rooms)"
    echo
}


function inspect () {
    # Take a room number; report its occupant.
    [[ $1 -ge 0           ]] || { echo too small; return; }
    [[ $1 -lt ${#HALL[@]} ]] || { echo too large; return; }
    echo Room $1 contains: ${HALL[$1]}
}

function swap () {
    # Take two room numbers and swap their occupants
    local TEMP
    TEMP=${HALL[$1]}
    HALL[$1]=${HALL[$2]}
    HALL[$2]=${TEMP}
    show
}

function step-right () { 
    # Take a room mumber, and move it occupant one room to the right.
    local oldpos
    local newpos
    local item
    oldpos=$1
    newpos=$(( $1 + 1 ))
    # note the occupant of the the given room number.
    item=${HALL[$oldpos]}
        [ "${item}" == "${BLANK}" ] && {
	    echo a blank cannot step right
	    show
	    return
	}   
    echo Occupant ${item} is stepping rifht, from position $oldpos to position $newpos
    # put occupent in the new position,
    HALL[$newpos]=${item}
    # and remove him from the old position.
    HALL[$oldpos]=$BLANK
    show
}

# Initialize the have.

start-hallway-game
