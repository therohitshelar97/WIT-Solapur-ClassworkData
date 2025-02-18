f=open("StudentData.txt","a")
name=input("Enter your full name : ")
Class=input("In whcih claa are you studying ? ")
roll=int(input("Enter your roll number : "))
age=int(input("please enter your age : "))

f.write(f" \n Name : {name} \n Class : {Class} \n roll_number : {roll} \n age : {age} \n ==================================== \n")