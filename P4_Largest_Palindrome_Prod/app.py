res = 0
upBound = 1000

for a in range(upBound):
    for b in range(upBound):
        num = a*b

        str_num = str(num)
        invert_str_num = str_num[::-1]

        if str_num == invert_str_num and num > res:
            res = num

print res