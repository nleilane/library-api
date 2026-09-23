class Book:
    def __init__(self, id: int, title: str, author: str, publicationYear: str, genre: str, availability: bool):
        self.id = id
        self.title = title
        self.author = author
        self.publicationYear = publicationYear
        self.genre = genre
        self.availability = availability

    def __str__(self):
        return f"Id: {self.id}, Title: {self.title}, Author: {self.author}, PublicationYear: {self.publicationYear}, Genre: {self.genre}, Availability: {self.availability} " 
    #f significa string formatada, necessario para concatenar com os dados 