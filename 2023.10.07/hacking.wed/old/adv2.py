PAPER={}
PAPER['name']="Paper"
PAPER['role']="Warrier"

def describe_player():
    name=PAPER['name']
    role=PAPER['role']
    print( f"{name} is a {role}." )

#Another player?
BRYAN={}
BRYAN['name']="Bryan"
BRYAN['role']="Cleric"

def describe_player2():
    name=BRYAN['name']
    role=BRYAN['role']
    print( f"{name} is a {role}." )

describe_player()
describe_player2()

