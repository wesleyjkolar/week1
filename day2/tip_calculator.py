amount= float(input("Please enter meal total:"))
tip= float(input("Please enter tip amount:"))
def calculate_tip(amount,tip):
    return amount * (tip/100)
    
result= calculate_tip(amount,tip)
print(f"Your tip amount is {result}")
        