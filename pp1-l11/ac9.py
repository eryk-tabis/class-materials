class Book(object):
    def __init__(self, title, author, date_release):
        self.title = title
        self.author = author
        self.date_release = date_release
    def __str__(self):
        return "Title: {:}, author: {:}, release{:}".format(self.title, self.author, self.date_release)

class traditionalbook(Book):
    def __init__(self, title, author, date_release, n_of_pages):
        Book.__init__(self, title, author, date_release)
        self.n_of_pages = n_of_pages
    def __str__(self):
        return "Title: {:}, author: {:}, release{:}, number_of_pages: {}".format(self.title, self.author, self.date_release, self.n_of_pages)

class eBook(Book):
    def __init__(self, title, author, date_release, name_of_file):
        Book.__init__(self, title, author, date_release)
        self.name_of_file = name_of_file

    def __str__(self):
        return "Title: {:}, author: {:}, release{:}, name of file: {}".format(self.title, self.author, self.date_release, self.name_of_file)

b1 = traditionalbook("test", "test2", "mock3", "333")
print(b1)