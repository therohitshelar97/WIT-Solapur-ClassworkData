while True:
    num1=input("Enter the first num: ")
    num2=input("Emter the sec num: ")
    print("Choose the operation")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    choice=input("Enter the choice(1/2/3/4)")
    if choice in ('1','2','3','4'):
        if choice=='1':
            print("Result:",num1+num2)
        elif choice=='2':
            print("Result:",num1-num2)
        elif choice=='3':
            print("Result:",num1 * num2)
        elif choice=='4':
            if num2!=0:
                print("Result:",num1/num2)
        else:
            print("Error!Division by zero not possible")
    next_choice=input("If youwant to continue (yes/no):")
    if next_choice=="no":
        break
else:
    print("You entered the wrong input")
    