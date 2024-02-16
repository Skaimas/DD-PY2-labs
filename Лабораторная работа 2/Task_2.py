from typing import Optional


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(id_, int):
            raise TypeError("Значение аргумента должно иметь тип int")
        if not isinstance(name, str):
            raise TypeError("Значение аргумента должно иметь тип str")
        if not isinstance(pages, int):
            raise TypeError("Значение аргумента должно иметь тип int")
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f"Книга '{self.name}'"

    def __repr__(self):
        return f"Book(id_={self.id_}, name='{self.name}', pages={self.pages})"


class Library:
    def __init__(self, books: Optional[Book] = None):
        self.books = books

    def __str__(self):
        return f"{self.books}"

    def get_next_book_id(self):
        new_number_id = 1
        if self.books is None:
            print(f"id для новой книги = {new_number_id}")
        else:
            for i in self.books:
                new_number_id += 1
            print(f"id для новой книги = {new_number_id}")

    def get_index_by_book_id(self, id__: int):
        ild = 0
        ind = None
        if self.books is None:
            raise ValueError("Книг нет")
        else:
            for i in self.books:
                if i.id_ == id__:
                    ild += 1
                    ind = self.books.index(i)
        if ild == 0:
            raise ValueError("Книги с запрашиваемым идентификатором не существует")
        else:
            print(ind)


booK = Book(1, "Алые паруса", 245)
print(booK)
print(repr(booK))

bookss = [
    {
        "id_": 1,
        "name": "Алые паруса",
        "pages": 245,
    },
    {
        "id_": 3,
        "name": "Вий",
        "pages": 275,
    },
    {
        "id_": 2,
        "name": "Муму",
        "pages": 300,
    }
]

list_books = [Book(id_=book["id_"], name=book["name"], pages=book["pages"]) for book in bookss]

lib = Library(list_books)
print(lib)
lib.get_next_book_id()
lib.get_index_by_book_id(3)
