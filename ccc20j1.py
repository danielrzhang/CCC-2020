import sys
s = int(sys.stdin.readline())
m = int(sys.stdin.readline())
l = int(sys.stdin.readline())
t = 3 * l + 2 * m + s

if t >= 10:
    r = "happy"
else:
    r = "sad"
sys.stdout.write(r)
