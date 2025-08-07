l=[78,42,62,12,12,75,63,14,20,99]
print("Print the list using for loop")
for i in range(len(l)):
    print(l[i],end=" ")

print("\n") 
print("Print the reverse of the list using for loop")
for a in range(len(l)-1,-1,-1):
    print(l[a],end=" ")

print("\n")
print("Print the length of the list :",len(l))