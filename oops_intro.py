class Students:
    institute="OneTeam"
    def __init__(self,n,p):
        self.name=n
        self.place=p
    def display(self):
        print(f"Hello {self.name} you are from {self.place}")


class PythonStudents(Students):
    def __init__(self,c, n, p):
        self.course=c
        super().__init__(n,p)

pstd1=PythonStudents("Python FullStack","Akshay","Kochi")
pstd1.display()