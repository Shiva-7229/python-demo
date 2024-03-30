class person:
    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

class student(person):
    pass

p = student("John", "Smith")
p.printname()