from models.Book import Book
class Loan:
    def __init__(self, id: int,  book: Book, dateLoan: str, dateExpectedReturn: str, dateReturn: str):
        self.id = id
        self.book = book
        self.dateLoan = dateLoan
        self.dateExpectedReturn = dateExpectedReturn
        self.dateReturn = dateReturn