"""count=1
while count<=10:
    print(count,end=" ")
    count+=1
print("Hello")
print("Completed")"""

while True:
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
    z=input("Do you wish to continue (y/n) ? ")
    if z!="y":
        print("Exiting...")
        break