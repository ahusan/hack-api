from typing import Union
import uvicorn
from fastapi import FastAPI, Path
from fastapi_sqlalchemy import DBSessionMiddleware, db

from schema import Book as SchemaBook
from schema import Author as SchemaAuthor

from models import Book as ModelBook
from models import Author as ModelAuthor

import os
from dotenv import load_dotenv

load_dotenv('.env')


app = FastAPI()

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

@app.get("/")
async def root():
    return {"message": "hello world"}


@app.post('/book/', response_model=SchemaBook)
async def book(book: SchemaBook):
    db_book = ModelBook(
        title=book.title, 
        rating=book.rating, 
        author_id = book.author_id, 
        excerpt = book.excerpt, 
        genre = book.genre, 
        fiction = book.fiction, 
        language = book.language,
        price = book.price,
        ISBN = book.ISBN,
        year = book.ISBN
        )
    db.session.add(db_book)
    db.session.commit()
    return db_book

@app.get('/book/')
async def book():
    book = db.session.query(ModelBook).all()
    return book


  
@app.post('/author/', response_model=SchemaAuthor)
async def author(author:SchemaAuthor):
    db_author = ModelAuthor(name=author.name, age=author.age)
    db.session.add(db_author)
    db.session.commit()
    return db_author

@app.get('/author/')
async def author():
    author = db.session.query(ModelAuthor).all()
    return author

@app.put('/author/{author_id}')
async def update_author(
    *,
    author_id: int = Path(title="ID of the author", ge=0, le=1000),
    name : Union[str, None] = None,
    age: int = None,
    Author: SchemaAuthor
):
    result = {"author_id": author_id}
    if name:
        result.update ({"name": name})
    if age:
        result.update ({"age": age})
    if author:
        result.update ({"author": author})
    db.session
    return result



# To run locally
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)