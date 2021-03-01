import sys
import itertools

width = int(sys.stdin.readline())
length = int(sys.stdin.readline())
entireList = []
gridList = []

for i in range(width):
    numbers = map(int, sys.stdin.readline().split())
    arrayList = []
    
    for j in numbers: # Checking the numbers inside the "numbers" tuple
        emptyList = []
        newList = []
        arrayList.append(j)
        
        for k in range(1, j + 1): # Finding the factors of each number on the board
            if (j % k == 0) and (k <= length) and (k <= width):
                emptyList.append(k)
        thing = itertools.permutations(emptyList, 2) # Finding all permutations of coordinates of factors
        
        for i in thing: # Putting all permutations in separate lists
            newList.append(i)
        entireList.append(newList)
                
    gridList.append(arrayList)

startingPoint = gridList[0][0]
running = True

print(entireList)
print(gridList)

"""
while running:
    for i in entireList[0]:
        x, y = i
        newNumber = gridList[x-1][y-1]
        print(newNumber)
"""


        
        


        













        
        
