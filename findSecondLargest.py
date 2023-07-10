from os import *
from sys import *
from collections import *
from math import *

from sys import stdin
import sys

def findSecondLargest(sequenceOfNumbers):
    # Write your code here.
    max1=-9999999
    for i in range(len(sequenceOfNumbers)):
        if(sequenceOfNumbers[i]>max1):
            max1=sequenceOfNumbers[i]
    max2=-9999999
    for k in range(len(sequenceOfNumbers)):
        if(sequenceOfNumbers[k]>max2 and sequenceOfNumbers[k]!=max1 ):
            max2=sequenceOfNumbers[k]
    # print("ll",max2)

    if max2 == -9999999:
        return -1
    else:
        return max2
# Taking input using fast I/O.
def takeInput():
    n = int(input())

    sequenceOfNumbers = list(map(int, input().strip().split(" ")))

    return sequenceOfNumbers, n

# Main.
t = int(input())
while t:
    sequenceOfNumbers, n = takeInput()
    print(findSecondLargest(sequenceOfNumbers))
    t = t-1
