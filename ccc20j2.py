import sys
total = int(sys.stdin.readline())
startNumber = int(sys.stdin.readline())
infectedPerDay = int(sys.stdin.readline())

infectedCounter = 0
dayCounter = -1

while infectedCounter <= total:
    infectedCounter += startNumber
    startNumber *= infectedPerDay
    dayCounter += 1
sys.stdout.write(str(dayCounter))
    
    
    
