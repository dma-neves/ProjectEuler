def evenDiv(num, maxDiv):

    isEvenDiv = True

    for i in range(1, maxDiv+1):

        if num % i != 0:
            isEvenDiv = False
            break


    return isEvenDiv

res = 2520

while not evenDiv(res, 20):
    res += 20

print res
