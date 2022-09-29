class Course:
    courses = []
    def __init__(self, id, name, size):
        self.id = id
        self.name = name
        self.size = size

        Course.courses.append(self)

    def changeSize(self, newsize):
        self.size = newsize

    def getID(self):
        return self.id

    def __str__(self):
        return self.name

bio = Course("BIO101", "Introduction to biology", 20)
math = Course("MATH101", "Introduction to algebra", 10)

bio.id = "BIO205"
bio.name = "Micro biology"
bio.changeSize(15)
bio.size = 15

print(bio)
