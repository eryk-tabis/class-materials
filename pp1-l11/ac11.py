class Student(object):
    student_id = 100000
    def __init__(self, name, course):
        self.name = name
        self.course = course
        self.university = "UEK Kraków"
        self.id = Student.student_id
        Student.student_id += 1

    def __str__(self):
        return "{:} ({:}), {:}, {:}".format(self.name, self.id, self.course, self.university)

s1 = Student("Anna MAJ", "Applied Informatics")
s2 = Student("Anna MAJ", "Applied Informatics")
print(s2)
