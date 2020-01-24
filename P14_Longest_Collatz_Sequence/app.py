res_num = 0
res_length = 0
num = 1
threshold = 1000000

lengths = [-1] * threshold

def chainLength(n, length):

    num = int(n)

    if num < threshold and lengths[num] != -1: 
        length += lengths[num]

    else:
        if num == 1:
            length = 1

        elif num % 2 == 0:
            length = 1 + chainLength(num/2, length)
        
        else:
            length = 1 + chainLength(3*num + 1, length)

    if num < threshold:
        lengths[num] = length

    return length


while num < threshold:

    if lengths[num] == -1:
        cl = chainLength(num, 0)
        if cl > res_length:
            res_length = cl
            res_num = num

    num += 1

print(res_num)



