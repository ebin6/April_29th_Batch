'''num=2
count=0
while True:
    total=0
    for k in range(1,num):
        if num%k==0:
            total+=k

    if total==num:
      count+=1
      print(num,end=" ")
    num+=1
    if count==3:
        break
'''
'''

1
2 6
3 7 10
4 8 11 13
5 9 12 14 15

'''
rows=5

for row in range(1,rows+1):
    num=row
    for c in range(1,row+1):
        print(num,end=" ")
        num=num+(rows-c)
       
    print()