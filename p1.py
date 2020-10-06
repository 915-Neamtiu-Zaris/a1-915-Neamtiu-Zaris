#
# Implement the program to solve the problem statement from the first set here
#
# Generate the first prime number larger than a given natural number n.
#

def prim(a):
    if a == 2:
        return 1
    if a < 2:
        return 0
    if a % 2 == 0:
        return 0
    for x in range(3, a, 2):
        if x * x > a:
            break;
        if a % x == 0:
            return 0
    return 1

def largerPrime(a):
    x = a + 1
    while prim(x) == 0:
        x += 1
    return x

if __name__ == "__main__":    
    n = int(input('Type a number: '))
    print("The first prime number larger than n is: " + str(largerPrime(n)))
