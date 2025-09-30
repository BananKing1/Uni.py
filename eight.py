# Syracuse

def main():
    # declare the starting value
    n = int(input("Please input whole number: "))

    # while n is not 1
    while n != 1:

        # check if n is even number 
        if n%2 == 0:
            n = int(n/2)
            # with space instead of new line
            print(n, end=" ")

        # else not even number
        else:
            n = int(3*n+1)
            #  with space instead of new line
            print(n, end=" ")
            


main()
