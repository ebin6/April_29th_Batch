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


word_count={}
char=input("Enter your string : ")
for c in char:
    if c in word_count:
        word_count[c]=word_count[c]+1
    else:
        word_count[c]=1

print(word_count)