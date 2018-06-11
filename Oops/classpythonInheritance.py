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
    perc_rise = 1.10

    def __init__(self, firstname, lastname, marks, prog_lang):
        super().__init__(firstname, lastname, marks)
        self.prog_lang = prog_lang


std_1 = Dumb('Enrique', 'Abiel', 60, 'Python')
print(std_1.prog_lang)
