'''
count=int(input("How many you wish to enter : "))
numbers=[]
for c in range(count):
    num=int(input("Enter the number : "))
    numbers=numbers+[num]

for k in numbers:
    if k%2==0:
        print(k)
    
'''        
'''for k in range(1,6):
    for sp in range(5-k):
        print(" ",end=' ')
    for c in range(1,k+1):
        print("*",end=" ")
    print("")'''

"""
        *
      * *
    * * *
  * * * *
* * * * *

"""

"""

* * * * *
  * * * *
    * * *
      * *
        *

"""

'''for row in range(5):
    print("  "*row,end="")
    print("* "*(5-row))'''
 
'''for r in range(1,6):
    num=r
    for c in range(r):
        print(num,end=" ")
        num+=r
    print("")'''

'''
word_count={}
char=input("Enter your string : ")
for c in char:
    if c in word_count:
        word_count[c]=word_count[c]+1
    else:
        word_count[c]=1

print(word_count)

'''
"""
0 1 1 2 3 5 8 13 21 34

first,second=0,1
count=1
print(first,second,end=" ")
while count<=8:
    third=first+second
    print(third,end=" ")
    first,second=second,third
    count+=1
"""
'''choice=int(input("How many numbers you wish to print : "))
number=0
armstrong_count=0
while armstrong_count<choice:
    n=str(number)
    length=len(n)
    sum=0
    for k in n:
        sum=sum+int(k)**length
    if sum==number:
        print(number,end=" ")
        armstrong_count+=1
    number+=1
    '''
my_list=["Kochi",2,"OneTeam",78,12.45,"Python"]
for k,i in enumerate(my_list,1):
    print(f"{k}. {i}")