from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def sort012(arr, n) :

	# write your code here
    # don't return anything 
    lo = 0

    hi = n - 1

    mid = 0

    while mid <= hi:

        if arr[mid] == 0:

            arr[lo], arr[mid] = arr[mid], arr[lo]

            lo = lo + 1

            mid = mid + 1

        elif arr[mid] == 1:

            mid = mid + 1

        else:

            arr[mid], arr[hi] = arr[hi], arr[mid]

            hi = hi - 1

    return arr


#taking inpit using fast I/O
def takeInput() :
	n = int(input().strip())

	if n == 0 :
		return list(), 0

	arr = list(map(int, stdin.readline().strip().split(" ")))

	return arr, n



def printAnswer(arr, n) :
    
    for i in range(n) :
        
        print(arr[i],end=" ")
        
    print()
    
#main

t = int(input().strip())
for i in range(t) :

    arr, n= takeInput()
    sort012(arr, n)
    printAnswer(arr, n)
