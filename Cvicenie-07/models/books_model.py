books = [
    {
        'id' : 0,
        'title' : '',
        'author' : '',
        'first' : ''
    }
]

def getBooksAll():
    return books

def get_book_by_id():
    result = []
    for book in books:
        if book['id'] == id:
            result.append(book)
    return ''