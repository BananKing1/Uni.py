# Easter

def main():
    # Will ask user for year until it is in interval
    while True:
        year = eval(input("Input year: "))
        if 1981 < year < 2049:
            break
        else:
            print("Try again")

    # Declaration and calculations
    a=year%19
    b=year%4
    c=year%7
    d=(19*a+24)%30
    e=(2*b+4*c+6*d+5)%7

    # If date is 31 or less, the month is March and the calculated date
    # Then print date
    if (22+d+e) <= 31:
        print("Date: March",(22+d+e))

    # Else the month is April and the calculated date will be the
    # calculated date minus max amount of days in March
    # Then print date
    else:
        print("Date: April",  (22+d+e)-31)



main()
