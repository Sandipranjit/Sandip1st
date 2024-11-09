class Publication:
    def __init__(self, name):
        self.name = name

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine: {self.name}")
        print(f" - Chief Editor: {self.chief_editor}")

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self): #Over-riding method
        print(f"Book: {self.name}")
        print(f" - Author: {self.author}")
        print(f" - Total number of pages: {self.page_count}")

magazine = Magazine("Donald Duck", "Aki Hyyppä")
book = Book("Compartment No. 6", "Rosa Liksom", 192)

pub_list = [magazine, book]

for item in pub_list:
    item.print_information()

