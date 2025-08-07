inc=(56,63,65,21,32,45,24,82,67)

target=45
i=0
while (i<len(inc)):
    if (inc[i]==target):
        print("Found the target number",target,"at index",i)
        break
    i+=1
else:
    print("Target number not found in the list")