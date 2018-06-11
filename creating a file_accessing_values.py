class AboutPython(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def Details(self):
        for line in self.lyrics:
            print(line)

abc = AboutPython(["Python is a object Oriented Programming",
                   "Can use as procedureal language as well",
                   "Python is for multi purpose"])

print(id(abc))
xyz = AboutPython(["Python 2.x",
                        "Python 3.x"])
print(id(xyz))
abc.Details()
print("")
xyz.Details()