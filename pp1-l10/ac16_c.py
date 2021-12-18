class Ebook():
    def __init__(self, title, author, number_of_pages, current_page):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.current_page = current_page
        self.is_open = False

    def open_Ebook(self):
        self.is_open = True

    def close_Ebook(self):
        self.is_open = False

    def read_Ebook(self):
        if self.is_open:
            print("Page was read")
    def next_page(self):
        if self.is_open:
            if self.current_page + 1 > self.number_of_pages:
                pass
            else:
                self.current_page += 1

    def previous_page(self):
        if self.is_open:
            if self.current_page - 1 < 0:
                pass
            else:
                self.current_page -= 1


