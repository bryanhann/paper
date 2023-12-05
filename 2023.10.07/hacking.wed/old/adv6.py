PAPER={}
PAPER['name']="Paper"
PAPER['role']="Warrier"

def describe_player(player):
    name=player['name']
    role=player['role']
    print( f"{name} is a {role}." )

#Another player?
BRYAN={}
BRYAN['name']="Bryan"
BRYAN['role']="Cleric"

def describe_player2(player):
    name=player['name']
    role=player['role']
    print( f"{name} is a {role}." )

describe_player(PAPER)
describe_player2(BRYAN)

