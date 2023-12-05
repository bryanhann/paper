
def make_player(name,role):
    player={}
    player['name']=name
    player['role']=role
    return player

#PAPER={}
#PAPER['name']="Paper"
#PAPER['role']="Warrier"

#BRYAN={}
#BRYAN['name']="Bryan"
#BRYAN['role']="Cleric"

PAPER=make_player(name="Paper", role="Warrier")
BRYAN=make_player(name="Bryan", role="Cleric")

def describe_player(player):
    name=player['name']
    role=player['role']
    print( f"{name} is a {role}." )


describe_player(PAPER)
describe_player(BRYAN)

