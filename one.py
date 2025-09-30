# 2.1 Grading scale


def main():
    
    # let user declare score
    score = eval(input("Input student score: ")) 

    #Check if score is equivalent to a grade and print the grade 
    if score == 5:
        print("Grade: A")
    elif score == 4:
        print("Grade: B")
    elif score == 3:
        print("Grade: C")
    elif score == 2:
        print("Grade: D")
    elif score == 1 or score == 0:
        print("Grade: F")

    # If the score doesn't match a grade
    else:
        print("Wrong score!")
    
main()

