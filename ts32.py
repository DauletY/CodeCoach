# where's the book?

books = {
    "Life of Pi": "Adventure Fiction", 
    "The Three Musketeers": "Historical Adventure",
    "Watchmen": "Comics", 
    "Bird Box": "Horror",
    "Harry Potter":"Fantasy Fiction",
    "Good Omens": "Comedy"
}

book = input()

#change this part to use the .get() method
if(books.get(book)):
    print(books[book])
else:
    print("Book not Found")
