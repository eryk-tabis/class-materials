class Contact_List():
    def __init__(self):
        self.array = []

    def add(self, contact):
        self.array.append(list((contact.name, contact.email, contact.telephone)))

    def display(self):
        for i in range(len(self.array)):
            zdanie = ""
            for j in range(len(self.array[i])):
                zdanie += self.array[i][j] + "\t"
            print(zdanie)
