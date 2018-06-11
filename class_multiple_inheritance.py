#!/usr/bin/python
class Father():
    def gardening(self):
        print("I enjoy gardening")

class Mother():
    def cooking(self):
        print("I love cooking")

class Child(Father,Mother):
    def sports(self):
        print("I enjoy sports")

c = Child()     # Calling Child class
c.gardening()   # Calling the method from Father class
c.cooking()     # Calling the method from Mother class
c.sports()      # Calling the method from Child class

print("**********************************")
print(" ")
print("**********************************")



