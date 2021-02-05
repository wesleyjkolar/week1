input1= float(input("Please enter a number:"))
input2= input("Please input an operand:")
input3= float(input("Please enter another number:"))


def calculateadd(input1,input3):
    return (input1 + input3)
def calculatesub(input1,input3):
    return (input1 - input3)
def calculatemul(input1,input3):
    return (input1 * input3)
def calculatediv(input1,input3):
    return (input1 / input3)



if input2 == "+":
    result = calculateadd(input1,input3)
    
elif input2 == "-":
    result = calculatesub(input1,input3)
    
elif input2 == "*":
    result = calculatemul(input1,input3)
    
elif input2 == "/":
    result = calculatediv(input1,input3)

print(result)
