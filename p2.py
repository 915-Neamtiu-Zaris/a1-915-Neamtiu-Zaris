#
# Implement the program to solve the problem statement from the second set here
#

def solve(dayNumber, yearNumber, lDays, lSumDays):
    print(l2)

def binarySearch(lSumDays, dayIndex):
    indr = len(lSumDays)
    indl = 0
    rez = 0
    indrez = -1

    while(indl <= indr):
        m = int((indr + indl) / 2)

        if lSumDays[m] < dayIndex:
            rez = lSumDays[m]
            indrez = m
            indl = m + 1
        else:
            indr = m - 1;

    lRez = [rez, indrez]

    return lRez

def solve(dayNumber, yearNumber):
    lDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    lSumDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    lMonths = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    if (yearNumber % 4 == 0 and yearNumber % 100 != 0) or (yearNumber % 100 == 0 and yearNumber % 400 == 0):
        lDays[1] = 29

    length = len(lDays)

    for ind in range(1, length):
        lSumDays[ind] = lSumDays[ind - 1] + lDays[ind]

    lResults = binarySearch(lSumDays, dayNumber)
    
    indexMonth = lResults[1] + 1

    if dayNumber > lSumDays[lResults[1]]:
        indexDay = dayNumber - lSumDays[lResults[1]]
    else:
        indexDay = dayNumber

    print("The date you have entered is " + lMonths[indexMonth] + " " + str(indexDay) + " of " + str(yearNumber))
    

if __name__ == "__main__":
    dayNumber = int(input("Type the day number: "))
    yearNumber = int(input("Type the year number: "))
    solve(dayNumber, yearNumber)

    
