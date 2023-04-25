class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author 

    def __str__(self):
        return self.name + ' by ' + self.author

class Library(Book):
    def __init__(self, name=None):
        self.name = name
        self.collections = []
    
    def add_book(self, bookname, bookauthor):
        newbook = Book(bookname, bookauthor)
        self.collections.append(newbook)
        #self.collections.append(Book(bookname, bookauthor))
    
    def __str__(self):
        return self.name
    
    def __len__(self):
        return len(self.collections)

    def __getitem__(self, key):
        return self.collections[key]
    
    def by_author(self, author):
        ans = []
        for book in self.collections:
            if author == book.author:
                ans.append(book)

        #if len(ans) > 0:
        #	return ans
        #else:
        #	print('author does not exist!')

        if not ans:
            raise KeyError('Author does not exist')

        return ans


library = Library()

library.add_book('My First Book', 'Alice')
library.add_book('My First Book', 'Alice')
library.add_book('My Second Book', 'Alice')
library.add_book('A Different Book', 'Bob')

print(len(library))

book = library[2]
print(book)

books = library.by_author('Alice')
for book in books:
    print(book)

#books = library.by_author('Carol')
    