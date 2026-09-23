from django.db import models

class Book(models.Model):
    def _init_(self,title, author, publication_date, genre, availability):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.genre = genre
        self.availability = availability