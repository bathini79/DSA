from os import *
from sys import *
from collections import *
from math import *

def minimumParentheses(pattern):

    # Write your code here
    # Return the minimum number of parentheses required.
    openPar=0
    count=0
    for pat in pattern:
        if(pat=="("):
            openPar=openPar+1
        elif(pat==")" and openPar):
            count=count-2
            openPar=openPar-1
        count=count+1
    return count
