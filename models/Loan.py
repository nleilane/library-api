from models.Book import Book
from models.User import User

class Loan:
    def __init__(self, id: int,  book: Book, date_loan: str, date_expected_return: str, date_return: str):
        self.id = id
        self.book = book
        self.dateLoan = date_loan
        self.dateExpectedReturn = date_expected_return
        self.dateReturn = date_return

    def __str__(self):
        return f"id: {self.id}, book: {self.book}, dateLoan: {self.dateLoan}, dateExpectedReturn: {self.dateExpectedReturn}, dateReturn: {self.dateReturn}"