class A:
    def greet(self):
        print("Hello")

class B(A):
    def greet(self):
        print("Hello from B")

ob=B()
ob.greet()


