student={
    "Name" : "Sourabh Shiroti",
    "Roll no." : 1,
    "Class" : "XII", 
    #Nested Dictionary
    "Subjects" : {
        "Physics" : 90,
        "Chemistry" : 85,
        "Mathematics" : 95,
        "Biology" : 88,
    },
}
print("Your Name : ", student["Name"])
print("Your Roll No. : ", student["Roll no."])
print("Your Class : ", student["Class"])
print("Your Subjects : ", student["Subjects"])
print("Your Physics Marks : ", student["Subjects"]["Physics"])
print("Your Chemistry Marks : ", student["Subjects"]["Chemistry"])
print("Your Mathematics Marks : ", student["Subjects"]["Mathematics"])
print("Your Biology Marks : ", student["Subjects"]["Biology"])
print("All abouts student dictionary : ", student)