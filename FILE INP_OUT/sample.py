#Reading to a file
f = open("FILE INP_OUT\demo.txt", "r")
data=f.read()
#data=f.readline()
print(data)
print(type(data))
f.close()

print("=======================================")
#Writing to a file
f = open("FILE INP_OUT\demo.txt", "w")
f.write("4123")
f.close()

print("=======================================")
#Append to a file
f = open("FILE INP_OUT\demo.txt", "a")
f.write("\nHello World 2")
f.close()

f = open("FILE INP_OUT\demo.txt", "r")
data=f.read()
#data=f.readline()
print(data)
print(type(data))
f.close()