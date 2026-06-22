# class student:

#   # Constructor

#   def _init_(self, name, age):
#     self.name = name
#     self.age = age

#   def display(self):
#     print('Name: ', self.name)
#     print('Age: ', self.age)

# a = student('John', 21)

# # print(a.name)
# # print(a.age)

# a.display()

class complex:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        a=self.x+other.x
        b=self.y+other.y
        result=complex(a,b)
        return result
def display(self):
    print(self.x,'+',self.y)