from fastapi.testclient import TestClient
from main import app


def main():
    # Use context manager to ensure startup/shutdown events run
    with TestClient(app) as client:
        sample_book = {
            "title": "Test Book",
            "author": "FastAPI Tester",
            "genre": "Testing",
            "publishedDate": "2025-01-01",
        }

        # POST /books/add
        post_res = client.post("/books/add", json=sample_book)
        print("POST /books/add:", post_res.status_code, post_res.json())

        # GET /books
        get_res = client.get("/books")
        print("GET /books:", get_res.status_code)
        # Show last item to confirm presence
        try:
            books = get_res.json()
            print("Total books:", len(books))
            if books:
                print("Most recent book:", books[-1])
        except Exception as e:
            print("Failed to parse books list:", e)


if __name__ == "__main__":
    main()