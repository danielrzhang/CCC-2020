import sys
number = int(sys.stdin.readline())
xList = []
yList = []

for i in range(number):
    dropX, dropY = map(int, input().split(","))
    xList.append(dropX)
    yList.append(dropY)

smallX = str(min(xList) - 1)
smallY = str(min(yList) - 1)

largeX = str(max(xList) + 1)
largeY = str(max(yList) + 1)

sys.stdout.write(smallX + "," + smallY + "\n")
sys.stdout.write(largeX + "," + largeY)

    
