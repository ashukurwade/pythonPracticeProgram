#Python program to explain __init__

class student:
#__init__ is a function or function Object()
#__init__ method is available in all classes
    def __init__(self,st_name,st_class,st_marks):
        self.st_name = st_name
        self.st_class = st_class
        self.st_marks = 40
s1 = student("Ashutosh",10,40)
print(s1.st_name)
print(s1.st_class)
print(s1.st_marks)
