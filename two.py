# 2.2 Grading scale 2


def main():

    # let user declare score
    score = eval(input("Input student score: "))
    
    #Check if score is in interval of a grade and print the grade 
    if 89< score <101:
        print("Grade: A")
    elif 79 < score < 90:
        print("Grade: B")
    elif 69 < score < 80:
        print("Grade: C")
    elif 59 < score < 70:
        print("Grade: D")
    elif 0 <= score < 60:
        print("Grade: F")

    # If the score doesn't match a grade
    else:
        print("Wrong score!")
    
main()

