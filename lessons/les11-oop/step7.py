class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def __str__(self):
        return f'Книга {self.title}, автора {self.author}'


book = Book('Война и Мир', 'Лев Толстой', 1225)
print(f'Книга {book.get_title()}, автора {book.get_author()}, имеет {book.pages} страниц')

print(book.title, book.author, book.pages)

print(book)