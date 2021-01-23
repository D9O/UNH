# Andy Dodd
# Program 1 (to prepare for next lecture)

import sys

def Grade_Print(g):
    print("The grade is {}".format(g))

if __name__=="__main__":
    if len(sys.argv) != 2:
        sys.exit("proper usage: program_01.py <grade value between 80-100>")
    
    if sys.argv[1].isalpha():
        sys.exit("grade value must be an integer")

    grade = int(sys.argv[1])
    if grade < 80 or grade > 100:
        sys.exit("grade value is not between 80 - 100")

    if grade >= 95:
        Grade_Print("A+")
    elif grade >= 90:
        Grade_Print("A")
    elif grade >= 85:
        Grade_Print("B+")
    elif grade >= 80:
        Grade_Print("B")
        
