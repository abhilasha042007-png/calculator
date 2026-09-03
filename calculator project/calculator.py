# PYTHON CALCULATOR 

while True:
    print("---Simple Calculator---")
    print("1,ADD")
    print("2,SUB")
    print("3,MUL")
    print("4,DIVI")
    print("5,EXIT")

    choice = input("Choose potion (1-5):")

    if choice =="5":
        print("calculator closed")
        break

    num1 = float(input("enter first number:")) 
    num2 = float(input("enter second number :")) 

    if choice == "1":
        print("Result =", num1 + num2)

    elif choice =="2":
        print("Result =", num1 - num2)  

    elif choice =="3": 
        print("Result =", num1 * num2)  

    elif choice =="4":
        if num2 != 0:
         print("Result =", num1 / num2)  
        else :
            print("cannot divide by zero")

    else :
        print("invalid choice")