# Prime number

import math

def main():
    # declare n as input
    n = int(input("Input a number (whole numbers): "))
    # assume n is prime
    is_prime = True


    # for loop will only work is n is 4 or more
    # example: range(2, 1) will not work same with range(2, 2)
    if n>=4:
        # to ensure it runs though all i add +1
        # example sqrt(9)=3, will not check  range(2, 3) but range(2, 2)
        for i in range(2, int(math.sqrt(n))+1):
            # check if divisable by sqrt(n)
            if n%i == 0:
                is_prime = False

    # because n cannot be smaller than 4 because the range will work
    # we know every positive number less than 4 are prime numbers 
    elif 0 < n < 4:
        is_prime = True

    # case for neg. input
    else:
        print("Please write positive number. ")
        is_prime = False


    # output if n is prime or not
    if is_prime == True:
        print(n, "is prime")
    elif is_prime == False:
        print(n, "is not prime")


main()
