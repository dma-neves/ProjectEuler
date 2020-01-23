# a^2 + b^2 = c^2
# a < b < c

# a + b + c = 1000 <=> c = 1000 - a - b
# a^2 + b^2 = (1000 - a - b)^2 <=> 1000^2 - 2000a - 2000b + 2ab = 0 

def find_a_b(upperBound):
    for a in range(1, upperBound):
        for b in range(a+1, upperBound):
            # print(str(a) + " " + str(b))
            if 1000*1000 - 2000*a - 2000*b + 2*a*b == 0:
                return (a,b)

    return (0,0)


a,b = find_a_b(99999)
c = 1000 - a - b

print a*b*c



