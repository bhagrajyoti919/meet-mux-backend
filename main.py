import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date, datetime, time
from motor.motor_asyncio import AsyncIOMotorClient

# Load environment variables from .env
load_dotenv()

app = FastAPI(
    title="Meet Mux API",
    description="FastAPI Swagger UI demo for Meet Mux backend",
    version="1.0.0",
)


class User(BaseModel):
    name: str
    age: int | None = None


class Book(BaseModel):
    title: str
    author: str
    genre: str
    publishedDate: date


# MongoDB setup
mongo_client: AsyncIOMotorClient | None = None
books_collection = None

def get_mongo_uri() -> str:
    # Use env var or fallback to local DB like Node app
    return os.getenv("mongodb_uri", "mongodb://127.0.0.1:27017/meet-mux")


@app.on_event("startup")
async def startup_event():
    global mongo_client, books_collection
    mongo_client = AsyncIOMotorClient(get_mongo_uri())
    # If database name not in URI, default to 'meet-mux'
    db_name = (mongo_client.get_default_database().name
               if mongo_client.get_default_database() is not None
               else "meet-mux")
    db = mongo_client[db_name]
    books_collection = db["books"]


@app.on_event("shutdown")
async def shutdown_event():
    if mongo_client:
        mongo_client.close()


@app.get("/")
def read_root():
    return {"message": "Welcome to Meet Mux! The app is loading..."}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/users")
def create_user(user: User):
    return {"created": True, "user": user}


def _book_doc(book: Book) -> dict:
    # Align fields with Mongoose defaults (available, timestamps)
    doc = {
        "title": book.title,
        "author": book.author,
        "genre": book.genre,
        # store as datetime for MongoDB consistency
        "publishedDate": datetime.combine(book.publishedDate, time()),
        "available": True,
        "createdAt": datetime.utcnow(),
        "updatedAt": datetime.utcnow(),
    }
    return doc


@app.post("/books/add", status_code=201)
async def add_book(book: Book):
    doc = _book_doc(book)
    await books_collection.insert_one(doc)
    return {"message": "Book added successfully!"}


@app.post("/api/books/add", status_code=201)
async def add_book_api(book: Book):
    doc = _book_doc(book)
    await books_collection.insert_one(doc)
    return {"message": "Book added successfully!"}


@app.get("/books")
async def list_books():
    cursor = books_collection.find().sort("createdAt", -1)
    books = await cursor.to_list(length=1000)
    # Convert ObjectId to string for JSON response
    for b in books:
        if "_id" in b:
            b["_id"] = str(b["_id"])
    return books


@app.get("/api/books")
async def list_books_api():
    cursor = books_collection.find().sort("createdAt", -1)
    books = await cursor.to_list(length=1000)
    for b in books:
        if "_id" in b:
            b["_id"] = str(b["_id"])
    return books


def get_port() -> int:
    # Prefer uppercase PORT, but support lowercase port as in the Node app
    return int(os.getenv("PORT", os.getenv("port", "8000")))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=get_port(),
        reload=True,
    )