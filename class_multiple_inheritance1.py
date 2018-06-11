class Father():
    def skills(self):
        print("Listening music,writing code")

class Mother():
    def skills(self):
        print("cooking,art")

class Child(Father,Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Sports")

c = Child()  # Calling Child class
c.skills()   # Calling the skills method