# Creating class in python
class student:
    # Calss Variable
    perc_rise = 1.05

    '''Using __init__() Initailze Method or Constructor method'''

    def __init__(self, firstname, lastname, marks):
        '''self is a instance'''
        self.firstname = firstname
        self.lastname = lastname
        self.marks = marks
        self.email = firstname + '.' + lastname + '@gmail.com'

    '''Creating a Method/Function of a class'''

    def fullname(self):
        return ('{} {}'.format(self.firstname, self.lastname))

    def apply_raise(self):
        self.marks = int(self.marks * 1.05)


class Dumb(student):
    pass


std_1 = Dumb('Goldy', 'Kummari', 90)

print(std_1.email)

print(help(Dumb))

std_2 = student('Jessica', 'Kummari', 80)

print(std_2.email)

"""
== RESTART: C:/Users/Jessicah Princess/Desktop/ClassInPythonInheritance.py ==
Goldy.Kummari@gmail.com
Help on class Dumb in module __main__:
class Dumb(student)
 |  Method resolution order:
 |      Dumb
 |      student
 |      builtins.object
 |  
 |  Methods inherited from student:
 |  
 |  __init__(self, firstname, lastname, marks)
 |      self is a instance
 |  
 |  apply_raise(self)
 |  
 |  fullname(self)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from student:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from student:
 |  
 |  perc_rise = 1.05
None
Jessica.Kummari@gmail.com
"""
