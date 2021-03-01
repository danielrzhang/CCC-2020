import sys
longString = sys.stdin.readline()
shortString = list(sys.stdin.readline())

shortString.pop()
for i in shortString:
    shortString.insert(0, shortString[-1])
    shortString.pop()
    print(shortString)
    result = ''.join(shortString)
    if result in longString:
        answer = "yes"
        break
    else:
        answer = "no"

sys.stdout.write(answer)
    
    
