import copy

d=[[23,"Python"],['Ebin',45.6]]

new_d=copy.copy(d)

new_d[0][1]="Java"
print(new_d)
print(d)