def addition(x, y):
    result = x
    result += y
    return result


def substraction(x, y):
    result = x
    result -= y
    return result


def divisionQ(x, y):
    result = x
    result = int(result / y)
    return result


def divisionR(x, y):
    result = x
    result = int(result % y)
    return result


def divisionA(x, y):
    result = x
    result = result / y
    return result


def multiplication(x, y):
    result = x
    result *= y
    return result


def pow(x, y):
    result = x
    result = result ** y
    return result


def calc(in1, opr, in2):
    if opr == "+" or opr == "-" or opr == "/" or opr == "*" or opr == "^":
        if opr == "+":
            print(
                "___________________________________________________________________________________________________")
            print("\tSum = " + str(addition(in1, in2)))
        elif opr == "-":
            print(
                "___________________________________________________________________________________________________")
            print("\tDifference = " +
                  str(substraction(in1, in2)))
        elif opr == "/":
            print(
                "___________________________________________________________________________________________________")
            print("\tQuotient = " +
                  str(divisionQ(in1, in2)))
            print("\tRemender = " +
                  str(divisionR(in1, in2)))
            print("\tExact Value = " +
                  str(divisionA(in1, in2)))
        elif opr == "*":
            print(
                "___________________________________________________________________________________________________")
            print("\tProduct = " +
                  str(multiplication(in1, in2)))
        elif opr == "^":
            print(
                "___________________________________________________________________________________________________")
            print("\t", in1, "Raised to the Power ", in2, " = " +
                  str(pow(in1, in2)))
    else:
        print(
            "___________________________________________________________________________________________________")
        print("\tInvalid Operator...! Please Try Again.")
    return True
