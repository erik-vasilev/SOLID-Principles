from abc import ABC, abstractmethod


class Book:
    def __init__(self, content: str, pages=100):
        self.content = content
        self.pages = pages


class BaseFormatter(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        pass


class MobileFormatter(BaseFormatter):
    def format(self, book: Book):
        return book.content[:20]


class DesktopFormatter():
    def format(self, book: Book) -> str:
        return book.content[:100]


class Printer:
    def get_book(self, book: Book, formatter):
        print('Print...')
        return formatter.format(book)


printer = Printer()
book = Book('Hello there myWorld 123456789')
mobile_formatter = MobileFormatter()
desktop_formatter = DesktopFormatter()

print(printer.get_book(book, desktop_formatter))
print(printer.get_book(book, mobile_formatter))
