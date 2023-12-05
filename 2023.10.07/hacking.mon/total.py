
LIST=[0,1,2,3,4,5]

def addup(numbers):
    print( f"list to addup: {numbers}" )
    total=0
    print( f"Starting total is: [{total}]" )
    for item in LIST:
        total += item
        print( f"item is {item}. Total is [{total}]" )
    print( "--addup()" )


