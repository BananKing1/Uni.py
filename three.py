# Eligibility

def main():

    #declare age
    age = eval(input("Input age: "))
    # declare years been a citizen
    citizen = eval(input("Years been a US citizen: "))


    # Check if age is 30 or older and years been citizen is 9 or more
    # Print either eligible or not
    if age >= 30 and citizen >= 9:
        print("Eligable for senate: yes")
    else:
        print("Eligable for senate: no")

    # Check if age is 25 or older and years been citizen is 7 or more
    # Print either eligible or not
    if age >= 25 and citizen >= 7:
        print("Eligable for The House: yes")
    else:
        print("Eligable for The House: no")

    # Works even for negative numbers!

main()
