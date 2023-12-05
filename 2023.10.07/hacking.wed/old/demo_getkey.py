from getkey import getkey, keys
key = getkey()
if key == keys.LEFT:
    print("LEFT")
"""

if key == keys.UP:
  ...  # Handle the UP key
elif key == keys.DOWN:
  ...  # Handle the DOWN key
elif key == 'a':
  ...  # Handle the `a` key
elif key == 'Y':
  ...  # Handle `shift-y`
import sys, select


i, o, e = select.select( [sys.stdin], [], [], 10 )

print( f"[{i}]" )

"""


