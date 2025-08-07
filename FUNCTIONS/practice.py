#Write a function to print the lenght of a list(list is the paramenter)

city=["Tokyo","Paris","London","Newyork","Dubai","Bangkok","Singapore","Hongkong","Seoul","Shanghai"]
movies=["Avengers","Titanic","Avatar","Inception","Interstellar","The Dark Knight","The Godfather","Pulp Fiction","Forrest Gump","The Shawshank Redemption"]

def ran(list):
    print(len(list))
    return len(list)

ran(city)
ran(movies)

#Write a function to print the sum of all the elements in a list(list is the paramenter)

def el(list):
    print(city)
    return city

def ele(list):
    print(movies)
    return movies


el(city)
ele(movies)

#Write a function to find the factorial of n(n is the paramenter)

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)  

print(fact(5))
print(fact(6))
print(fact(8))
print(fact(3))         

#Write a function to convert USD To INR 

def convert(usd):
    inr=usd*83
    print(usd, "USD =",inr, "INR")
    return inr

convert(3)