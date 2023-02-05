
# TODO написать класс Library

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id = id_  # атрибут идентификатора книги
        self.name = name  # атрибут названия книги
        self.pages = pages  # атрибут количества страниц

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id!r}, name={self.name!r}, pages={self.pages!r})'

class Library:
    def __init__(self, books = []):
        self.books = books #атрибут - список книг

    def get_next_book_id(self):
        return len(self.books)+1  #добавление новой книги в библиотеку

    def get_index_by_book_id(self, id):
        for index, book in enumerate(self.books): # поиск индекса книги
            if book.id == id:
                return self.books.index(book)
        raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1





