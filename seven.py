# Investment

def main():
    # declare interest rate and starting fund
    initial = int(input("What is the interest rate? "))/100+1
    fund = eval(input("How much do you want to invest? "))
    print("Your interest: ", initial, "\n")

    # declare a start year and base interest
    year = 1
    interest = initial

    # indefinite loop, checks if interest has doubled
    while interest < 2:
        interest = interest*initial
        year += 1

    # calculations and outputs
    fund = fund*interest
    print("It will take", year, "year(s) to double your investment.")
    print("Total investment: ", fund)


main()

# No the initial investment does not matter because we only check if the value is doubled
