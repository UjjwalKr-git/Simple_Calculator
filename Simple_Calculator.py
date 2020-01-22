import Notes
import Back_End
import os


def clrscr():
    return os.system("cls")


Notes.Notes()
z = 0
while(z == 0):
    print()
    print("___________________________________________________________________________________________________")
    in1 = input("First Input        : ")
    if in1 == "n" or in1 == "N":
        Notes.Notes()
    else:
        try:
            in1 = float(in1)
            opr = input("Enter The Operator : ")
            if opr == "+" or opr == "-" or opr == "/" or opr == "*" or opr == "^" or opr == "0":
                if in1 != 0 and opr == "0":
                    print(
                        "___________________________________________________________________________________________________")
                    print("\tInvalid Operator...! Please Try Again.")
                    print(
                        "___________________________________________________________________________________________________")
                    continue
                in2 = float(input("Second Input       : "))
                if in1 == 0 and opr == "0" and in2 == 0:
                    break
                elif Back_End.calc(in1, opr, in2) == True:
                    print(
                        "___________________________________________________________________________________________________")
                else:
                    print(
                        "___________________________________________________________________________________________________")
                    print(
                        "\tSomething Went WRONG...! Please Try Again or Contact The Developer.")
                    print(
                        "___________________________________________________________________________________________________")
            else:
                print(
                    "___________________________________________________________________________________________________")
                print("\tInvalid Operator...! Please Try Again.")
                print(
                    "___________________________________________________________________________________________________")
        except ValueError:
            print("___________________________________________________________________________________________________")
            print("\tInvalid Input...! Please Try Again.")
            print("___________________________________________________________________________________________________")
        except ZeroDivisionError:
            print("\tSorry...! \'" + str(in1) +
                  "\' Can't be Divided by \'" + str(int(in2)) + "\'.")
            print("___________________________________________________________________________________________________")
print()
Notes.Foot_Notes()
Stop_Exit = input()
clrscr()
