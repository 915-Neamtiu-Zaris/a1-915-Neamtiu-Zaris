#
# Implement the program to solve the problem statement from the third set here
#

def perfect(n):
    s = 0
    
    for x in range(1, n):
        if(n % x == 0):
            s += x

    if n == s:
        return 1
    else:
        return 0


def solve(n):
    exists = 0

    for x in range(n - 1, 0, -1):
        if(perfect(x)):
            print("The largest perfect number smaller than " + str(n) + " is: " + str(x))
            exists = 1
            break

    if(exists == 0):
        print("There is no pefect number smaller than " + str(n))

   
if __name__ == "__main__":
    n = int(input("Type a pozitive, whole number: "))
    solve(n)

    
    
