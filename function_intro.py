def total(*args):
    sum=0
    for k in args:   #  args -->  (34,21,12)
        sum=sum+k
    print(sum)

total(34,21,12)
total(7,2)


def display(**kwargs):
    print(kwargs)

display(name="Ebin",age=28)
display(name="Akshay",age=21,place="Kottayam")