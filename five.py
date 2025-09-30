# Day of the year

def main():
    # declaration for day, month and year
    print("Please input whole numbers and real dates (else the program will not work!")
    day = int(input("Input a day: "))
    month = int(input("Input a month: "))
    year = int(input("Input a year: "))


    # formula given for day number
    dayNum= 31*(month-1)+day

    # if it's after febrary
    if month > 2:
        dayNum = dayNum-(4*(month)+23)//10

        # check if not leap year
        if year%400 == 0:
            print(dayNum)

        # check leap year
        elif year%4 == 0:
            dayNum =+ 1
            print(dayNum)

        # if it's not a leap and date after February
        else:
            print(dayNum)
            
    # If no condition is met
    else:
        print(dayNum)
            

main()
