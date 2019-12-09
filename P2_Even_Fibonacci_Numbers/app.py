upBound = 4000000
sum = 2

n_0 = 1
n_1 = 2

new_n = n_0 + n_1

while new_n < upBound:

	if new_n%2 == 0:
		sum += new_n

	n_0 = n_1
	n_1 = new_n

	new_n = n_0 + n_1

print(sum)
	