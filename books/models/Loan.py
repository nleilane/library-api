from django.db import models

class Loan(models.Model):
    def _init_(self, book, dateLoan, dateExpectedReturn, dateReturn):
        self.book = book
        self.dateLoan = dateLoan
        self.dateExpectedReturn = dateExpectedReturn
        self.dateReturn = dateReturn