#
# Implement the program to solve the problem statement from the second set here
#
#Determine a calendar date (as year, month, day) starting from two
#integer numbers representing the year and the day number
#inside that year (e.g. day number 32 is February 1st).
#Take into account leap years. Do not use Python's inbuilt date/time functions.
#



#Functie de cautare binara care returneaza cea mai mare valoare mai mica decat
#numarul zilei obtinut din input si indicele acestei valori in lista de sume partiale.
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
    lSumDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]     #Lista a sumelor partiale a numerelor de zile din fiecare luna
    lMonths = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    if (yearNumber % 4 == 0 and yearNumber % 100 != 0) or (yearNumber % 100 == 0 and yearNumber % 400 == 0):
        lDays[1] = 29   #Daca anul e bisect, februarie are 29 de zile

    length = len(lDays)

    for ind in range(1, length):
        lSumDays[ind] = lSumDays[ind - 1] + lDays[ind]  #Generarea sumelor partiale

    lResults = binarySearch(lSumDays, dayNumber)
    
    indexMonth = lResults[1] + 1    #deoarece indrez e initializat cu -1 in algoritmul de cautare binara
                                    #si din cauza naturii algoritmului, se returneaza 'indicele lunii
                                    #cautate' -1, asa ca il incrementam
    print(lSumDays)

    if dayNumber > lSumDays[lResults[1]]:               #daca numarul zilei de la input e mai mare ca rezultatul aflat pe indicele
        indexDay = dayNumber - lSumDays[lResults[1]]    #gasit de algoritm (unde se afla cea mai mare valoare mai mica decat numarul zilei introdus 
    else:                                               #la input, din lista de sume partiale), atunci nu suntem in luna ianuarie
        indexDay = dayNumber                            #(la input s-a citit ceva mai mare de 31), asa ca trebuie sa recalculam ziua

    print("The date you have entered is " + lMonths[indexMonth] + " " + str(indexDay) + " of " + str(yearNumber))
    

if __name__ == "__main__":
    dayNumber = int(input("Type the day number: "))
    yearNumber = int(input("Type the year number: "))
    solve(dayNumber, yearNumber)

    
