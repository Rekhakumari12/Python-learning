
def help_menu():
    print("Add- for addition")
    print("Sub- for substraction")
    print("Mul- for multiplication")
    print("Div- for division")
    print("Quite- for exit ")

def menu():
     return input("\n#A)Add\n#S)Sub\n#M)Mul\n#D)Div\n#P)Print\n#Q)Quite\n#H)Help\n\n")

def main():
    done=False
    while not done:
        choice = menu()

        if choice == 'A' or choice == 'a':
            arg1 = eval(input("Enter num1: "))
            arg2 = eval(input("Enter num2: "))
            result = arg1+arg2
            print("result is ",result)

        elif choice == 'S' or choice == 's':
            arg1 = eval(input("Enter num1: "))
            arg2 = eval(input("Enter num2: "))
            result = arg1-arg2
            print("result is ",result)

        elif choice == 'M' or choice == 'm':
            arg1 = eval(input("Enter num1: "))
            arg2 = eval(input("Enter num2: "))
            result = arg1*arg2
            print("result is ",result)

        elif choice == 'D' or choice == 'd':
            arg1 = eval(input("Enter num1: "))
            arg2 = eval(input("Enter num2: "))
            result = arg1/arg2
            print("result is ",result)

        elif choice == 'P' or choice == 'p':
            print(result)

        elif choice == 'H' or choice == 'h':
             help_menu()

        elif choice == 'Q' or choice == 'q':
             done = True

main()
