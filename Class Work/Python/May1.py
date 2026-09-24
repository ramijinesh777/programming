""" OOPS : Object Oriented Programming System """
# There are 5 Pillers:
    # 1) class-object
    # 2) inheritence
    # 3) polymorphisam
    # 4) encapsulation
    # 5) abstraction

"""(1) class 
                     Class ia a collection of data menber and member functions """
"""(2) object
                     Instance of class through the object we can access all the properties class"""


# class Myclass:
#     def fun1(self):
#         pass

# obj = Mycalss()
# obj.fun1()
# obj.fun2()

#################################

class Myclass:

    def fun1(self):
        print("Method 1!!")

class Myclass1:

    def fun2(self):
        print("Method 2!!")

obj = Myclass1()
obj.fun1()
obj.fun2()

class Myclass2(Myclass,Myclass1):

    def fun3(self):
        print("Method 3!!")

obj = Myclass1()
obj.fun1()
obj.fun2()





