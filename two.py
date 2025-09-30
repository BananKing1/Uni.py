# 2.2 Grading scale 2


def main():

    # let user declare score
    score = eval(input("Input student score: "))
    
    #Check if score is in interval of a grade and print the grade 
    if 90< score <100:
        print("Grade: A")
    elif 80 < score < 89:
        print("Grade: B")
    elif 70 < score < 79:
        print("Grade: C")
    elif 60 < score < 69:
        print("Grade: D")
    elif 0 < score < 60:
        print("Grade: F")

    # If the score doesn't match a grade
    else:
        print("Wrong score!")
    
main()

