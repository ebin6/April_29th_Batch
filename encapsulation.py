class Student:
    def __init__(self):
        self.name="Ebin"
        self._place="Kochi"
        self.__age=28

std=Student()
print(std._place)
print(std._Student__age)