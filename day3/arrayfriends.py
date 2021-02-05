#friends=["noah", "nate", "arlo", "aubrianna", "daniel"]

#for index in friends:
#    print(index)

#reverse loop

#numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#for index in range(10,0,-1):
#    print(index)

# assignments1-3

print("Assignment 1, Day 3")

number= int(input("Please enter a number:"))

factorial = 1

if number < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif number == 0:
   print("The factorial of 0 is 1")
else:
    for index in range(1,number + 1):
        factorial = factorial*index
print("The factorial of",number,"is",factorial)

print("Assignment 2, Day3")

word= input("Please enter a palandrome:")
 
pala = ""

for index in word:   
    pala = index + pala

if (pala == word):
    print("Your word is a correct palandrome!")
else:
    print("That word is not a palandrome, sorry.")


print("Assignment 3, Day 3")

number= int(input("Please enter a number:"))

if number > 1:
 
    for index in range(2, number):       
        if (number % index) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")
 
else:
    print(number, "is not a prime number")
 







