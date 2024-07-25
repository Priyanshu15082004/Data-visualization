# class Student:
#     name="abc"
#     age=0
#     def study (self):
#         print("study 8 hour")
# obj=Student()
# obj.study()
#-------------------------------------------------------------------------------
# def show():
#     print("This is show function outside class")
# class Student:
#     def study (self):
#         self.show()
#         print("this is a study method")
#     def show(self):
#         print("This is show method inside class")
# obj=Student()
# obj.study()
#----------------------------------------------------------------------
# class A:
#     name ="Anant"
#     def show(self):
#        print("This is A class show method")
# class B(A):
#     def demo(self):
#        print("This is demo method")
# class C(B):       
#     pass
# obj=C()
# obj=B()
# obj.demo()
#----------------------------------------------
# class A:
#     name ="Anant"
#     def show(self):
#        print("This is A class show method")
# class B(A):
#     def demo(self):
#        print("This is demo method")
# class C(B):       
#     pass
# obj=C()
# obj=B()
# obj.demo()
#-------------------------------------------------------
#Hybrid Inheritance
# class A:
#     name ="Anant"
#     def show(self):
#        print("This is A class show method")
# class B(A):
#     def demo(self):
#        print("This is demo method")
# class C(A):       
#     pass
# class D(B,C):
#     pass
# obj=D()
# obj.show()
# obj.demo()
#--------------------------------------------------------------------------
# def setData(name,age):
#     print("Name is" ,name)
#     print("Age is " ,age)
# def setData(sid,name,age):
#     print("Name is",name)
#     print("Age is",age)
#     print("Id is",sid)

# #setData("Sanjay",25)
# setData(101,"Anudip",20)        
#---------------------------------------------------------------------
#Polymorphism lets us define methods in the child class that have the same name as
#  the methods in the parent class. In inheritance, the child class inherits the methods from the parent class.
#  However, it is possible to modify a method in a child class that it has inherited from the parent class.
#  This is particularly useful in cases where the method inherited from the parent class doesn't quite fit the child class. 
# In such cases, we re-implement the method in the child class. This process of re-implementing a method in the child class is known as Method Overriding.
#-----------------------------------------------------------------------
#Method over riding
# class Bird:
#     def intro(self):
#         print("There are many types of birds.")
#     def flight(self):
#         print("Most of the bird can fly but some cannot")
# class sparrow(Bird):
#     def flight(self):
#         print("I can fly")
# class ostrich(Bird):
#     pass
# s=sparrow()
# s.flight()

#---------------------------------------------------------------------
# class A:
#     name="Vikas"
#     def show(self):
#         print("This is show method",name)
# class B(A):
#     pass 
# obj=B()
# print(obj.name)       
#---------------------------------------------------------------------
# print("Line 1")
# print("Line 2")
# print("Line 3")
# try:
#     print(100/2)
#     open("abc.txt")
# except ZeroDivisionError as e:
#     print(e)   
# except FileNotFoundError:
#     print("file does not exits")     
# print("Line 5")
# print("Line 6")
# print("Line 7")
#-----------------------------------------------------------------------
# print("Line 1")
# print("Line 2")
# print("Line 3")
# try:
#     print(100/0)
#     print(name)
# except (ZeroDivisionError,NameError):
#     print("something went wrong")     
# print("Line 5")
# print("Line 6")
# print("Line 7")
# #------------------------------------------------------------------------
# print("Line 1")
# print("Line 2")
# print("Line 3")
# try:
#     print(100/0)
#     print(name)
# except:
#     print("something went wrong")     
# else:
#     print("else block")
# finally:
#     print("finally block")    
# print("Line 5")
#--------------------------------------------------------------------------------
# to raise an exception raise statement is used 
def checkAge(age):
    if age>=18:
        print("You are eligible for do anything")
    else:
        raise ValueError ("Your age is greater than 18")
try:    
    checkAge(15)
except ValueError as v:
    print("something went wrong",v)
#-------------------------------------------------------------
# try:
#     age=int(input("enter the age"))
#     if (age>=18):
#         raise ValueError
#     else:
#         print("the age is valid")
# except ValueError:
#     print("the age is not valid")            