from models.Book import Book

titleInput = input("Digite o nome do livro: ")
authorInput = input("Digite o nome do autor: ")
publicationYearInput = input("Digite o ano de publicação: ")
genreInput = input("Digte o gênero do livro: ")
availabilityInput = input("O livro está disponível? (S/N) ")
book = Book(
    id = 1, 
    title = titleInput,
    author = authorInput,
    publicationYear = publicationYearInput, 
    genre = genreInput,
    availability = availabilityInput.lower() == "s"
)
print(book)