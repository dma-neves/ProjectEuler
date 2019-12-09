sum = 0
upBound = 1000

n = 3
while n < upBound:
	sum += n
	n += 3

n = 5
while n < upBound:
	if n%3 != 0:
		sum += n
	n += 5

print(sum)