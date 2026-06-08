"""
if condition:
    statements


"""
'''
age=int(input("Enter you age : "))
if age>=18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

'''

"""
if condition:
    statements

elif condition:
    statements

elif condition:
    statements
else:
    statements
"""

a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
print("1.Addition\n2.Substract\n3.Multiply\n4.Divide")
choice=int(input("Enter your choice : "))
if choice==1:
    print("Sum = ",a+b)
elif choice==2:
    print("Difference = ",a-b)
elif choice==3:
    print(f"{a} * {b} = {a*b}")
elif choice==4:
    print(f"{a}/{b}={a/b}")
else:
    print("Please enter valid input 1 ,2 , 3 ,4")