class Phone(object):
    def __init__(self, number):
        self.number = number
        self.is_on = False

    def get_number(self):
        return self.number

    def show_is_on(self):
        if self.is_on:
            return "Phone is on"
        else:
            return "Phone is off"

    def change_is_on(self):
        if self.is_on:
            self.is_on = False
        else:
            self.is_on = True

p1 = Phone(222333444)
p2 = Phone(333444555)

