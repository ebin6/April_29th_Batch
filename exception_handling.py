
try:
    a=int(input('Enter the first number : '))
    b=int(input("Enter the second number : "))
    print(a/b)
except ValueError:
    print("Please enter valid number ")
except ZeroDivisionError:
    print("You cannot divide a number by zero")
except Exception as e:
    print("Error ...",e)
else:
    print("Program completed without raising errors")
finally:
    print("Program completed ....")