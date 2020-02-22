num_str = str(2 ** 1000)
res = 0

for digit in num_str:

    res += int(digit)

print(res)