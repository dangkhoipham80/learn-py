from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from starlette import status # fastapi built using starlette -> installed with fastapi installed

import datetime

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: float
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

# implementing Pydantics
class BookRequest(BaseModel): # BaseModel is a Pydantics Model
    id: Optional[int] = Field(description='ID is not needed to create', default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    # rating: float = Field(gt=0, lt=5)
    rating: float = Field(ge=0, le=5)
    published_date: int = Field(ge=1900, le=datetime.datetime.now().year)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "Someone",
                "description": "A description of a book",
                "rating": 5,
                "published_date": 1900
            }
        }
    }

BOOKS = [
    Book(1, 'Computer Science Pro', 'Johnny Dang', 'The best book for a beginner in computer science', 4.5, 2023),
    Book(2, 'Data Structures & Algorithms', 'Jane Smith', 'A complete guide to mastering data structures and algorithms.', 4.8, 2019),
    Book(3, 'Machine Learning Basics', 'Andrew Ng', 'A beginner-friendly introduction to machine learning concepts.', 4.7, 1919),
    Book(4, 'Deep Learning with Python', 'Francois Chollet', 'Learn deep learning with hands-on projects and real-world applications.', 4.6, 2004),
    Book(5, 'Python Crash Course', 'Eric Matthes', 'A fast-paced and hands-on guide to learning Python programming.', 4.9, 2004),
    Book(6, 'The Pragmatic Programmer', 'Andrew Hunt & David Thomas', 'A classic book on becoming a better programmer.', 4.8, 1901),
    Book(7, 'Design Patterns', 'Erich Gamma', 'An essential book on reusable object-oriented software design.', 4.7, 1999),
    Book(8, 'Clean Code', 'Robert C. Martin', 'A must-read book on writing maintainable and clean code.', 4.9, 1976),
    Book(9, 'Introduction to the Theory of Computation', 'Michael Sipser', 'A deep dive into the foundations of computer science.', 4.6, 1984),
    Book(10, 'Artificial Intelligence: A Modern Approach', 'Stuart Russell & Peter Norvig', 'The go-to book for AI fundamentals.', 4.7, 2008)
]

@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS

@app.get("/books/{book_id}", status_code=status.HTTP_200_OK) # path parameter
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book_id == book.id:
            return book
    raise HTTPException(status_code=404, detail='Item not found') # 404: Not Found

from typing import Optional

@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_books_by(
    book_rating: Optional[float] = Query(None, ge=0, le=5, description='Filter books by rating [0-5]'),
    book_published_date: Optional[int] = Query((datetime.datetime.now().year), ge=1900, le=datetime.datetime.now().year, description='Filter books by published year[1900-now]')
):
    books_to_return = BOOKS

    if book_rating is not None:
        books_to_return = [book for book in books_to_return if book.rating == book_rating]

    if book_published_date is not None:
        books_to_return = [book for book in books_to_return if book.published_date == book_published_date]

    return books_to_return


@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    print(type(book_request))
    new_book = Book(**book_request.model_dump()) # dict() -> .model_dump()
    # ** operator will pass the key/value from BookRequest() into the Book() constructor
    BOOKS.append(find_book_id(new_book))

def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book

# need id
@app.put("/update-book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(update_book_request: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == update_book_request.id:
            BOOKS[i] = update_book_request
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found')

@app.delete("/delete-book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    book_deleted = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_deleted = True
            break
    if not book_deleted:
        raise HTTPException(status_code=404, detail='Item not found')