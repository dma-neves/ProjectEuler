threshold = 100
sum_square = 0
sum = 0

for i in range(threshold+1):
    sum_square += i*i
    sum += i

print sum*sum - sum_square