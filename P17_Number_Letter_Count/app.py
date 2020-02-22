dig = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
ten = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
dec = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
cent = "hundred"

res = len("onethousand")

num_letters_bellow_ten = 0
for n in dig: num_letters_bellow_ten += len(n)

num_letters_bellow_hundred = num_letters_bellow_ten
for n in ten: num_letters_bellow_hundred += len(n)
for n in dec: num_letters_bellow_hundred += len(n) * 10 + num_letters_bellow_ten

res += num_letters_bellow_hundred

for i in range(0, 9):

    res += len(dig[i]) + len(cent)
    res += ( len(dig[i]) + len(cent) + len("and") ) * 99 + num_letters_bellow_hundred

print(res)
