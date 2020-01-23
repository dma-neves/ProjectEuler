import math

def isPrime(n):

	if n%2 == 0: 
		return False

	divisor = 3
	while divisor <= math.sqrt(n):
		
		if n%divisor == 0: 
			return False
		divisor += 2

	return True

threshold = 2000000
sum = 2
i = 3
while i < threshold:

    if isPrime(i):
        sum += i
    i += 2

print(sum)