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

result = 0
number = 600851475143

n = number
while n > 1:
	
	divisor = 2
	while n % divisor != 0:
		divisor += 1

	if(isPrime(divisor) and divisor > result):
		result = divisor

	n = n/divisor

print(str(result))

