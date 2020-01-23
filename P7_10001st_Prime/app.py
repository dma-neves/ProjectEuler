import math

def isPrime(n):

	if n%2 == 0: 
		return False

	divisor = 3
	while divisor <= math.sqrt(n):
		
		if n % divisor == 0: 
			return False
		divisor += 2

	return True

counter = 0
num = 0

while counter != 10001:

    num += 1
    
    while not isPrime(num):
        num += 1

    counter += 1

print num