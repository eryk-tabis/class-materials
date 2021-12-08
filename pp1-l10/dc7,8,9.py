class University():
    def __init__(self):
        self.name = 'CUE'
        self.fullname = "Cracow University of Economics"

    def print_name(self):
        print(self.name)

    def set_name(self, name):
        self.name = name

    def set_fullname(self, fullname):
        self.fullname = fullname

    def print_fullname(self):
        print(self.fullname)


uni = University()
uni.print_name()
uni.print_fullname()
uni.set_name("AGH")
uni.set_fullname("Akademia Górniczo-Hutnicza")
uni.print_name()
uni.print_fullname()
