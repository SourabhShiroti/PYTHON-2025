marks=int(input("Enter your Marks: "))
if(marks>90 and marks<=100):
    print("A")
elif(marks>80 and marks<=90):
    print("B")
elif(marks>60 and marks<=80):
    print("C")
elif(marks>32 and marks<=50):
    print("D")
elif(marks>0 and marks<=32):
    print("F")    
else:
    print("Invalid number")      