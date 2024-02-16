class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError("Аргумент pages должен иметь тип int")
        self.pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError("Аргумент duration должен иметь тип float")
        self.duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration})"


book = Book("Алые паруса", "Грин А.С.")
print(book)
print(book.name)
print(repr(book))

paper_book = PaperBook("Вий", "Гоголь Н.В.", 300)
print(paper_book)
print(repr(paper_book))

audio_book = AudioBook("Муму", "Тургенев И.С.", 3.5)
print(audio_book)
print(repr(audio_book))

book.name = "S.T.A.L.K.E.R"
