import math

def numDivisors(num):

    res = 0
    for i in range(1, (int)(math.sqrt(num))):
        if (num % i) == 0:
            res += 2

    return res


triangleNum = 0
counter = 0
found = False
threshold = 500

while not found:

    counter += 1
    triangleNum += counter

    if numDivisors(triangleNum) >= threshold:
        found = True

print(triangleNum)

