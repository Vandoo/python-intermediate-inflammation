class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return self.name + ' by ' + self.author


alice = Book('A book', 'Me')
print(alice)
