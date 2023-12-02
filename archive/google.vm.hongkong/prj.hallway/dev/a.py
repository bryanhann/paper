#!/usr/bin/env python3

import sys
import time
import colorama
from colorama import init, Fore, Back
init()
 
 # Fore changes the text's foreground color
print(Fore.BLUE + "Blue Letters")
  
 #Back changes the text's background color
print(Back.WHITE + "White Background")


def bar(length):
    body='#'*ii
    head=f"[{ii}]"
    line = body + head
    sys.stdout.write(line + '\b' * len(line))
    sys.stdout.flush()

for ii in range(20):
    bar(ii)
    time.sleep(.2)
print()
