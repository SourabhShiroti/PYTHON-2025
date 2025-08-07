# This program is a simple calculator that performs basic arithmetic operations
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
opr=input("Enter operator :")
if(opr=="+"):
    print("Sum is :",num1+num2)
elif(opr=="-"):
    print("Difference is :",num1-num2)
elif(opr=="*"): 
    print("Multiplication is :",num1*num2)
elif(opr=="/"):
    print("Division is :",num1/num2)
elif(opr=="%"):
    print("Reminder is :",num1%num2)
elif(opr=="**"):
    print("Exponential is :",num1**num2)
elif(opr=="//"):
    print("Double division is :",num1//num2)   
else:
    print("Invalid operator")
