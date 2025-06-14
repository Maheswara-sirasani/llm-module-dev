import json
import logging
from datetime import datetime
from functools import wraps
 
logging.basicConfig(
    filename='bookstore_app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
 
logger = logging.getLogger(__name__)
 
def handle_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            logger.info(f"Executing: {func.__name__}")
            return func(*args, **kwargs)
        except Exception as e:
            logger.exception(f"Error while Executing: {func.__name__} : {e}")
    return wrapper
 
class Book:
    def __init__(self, book_id, title, author, genre, price, published_date, stock):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.published_date = published_date
        self.stock = stock
 
    def is_in_stock(self):
        return self.stock > 0
 
    def get_age(self):
        pub_date = datetime.strptime(self.published_date, "%Y-%m-%d")
        return (datetime.now() - pub_date).days // 365
 
# ***** Helper Methods *****
@handle_exceptions
def load_books(filepath):
    with open(filepath, 'r') as f:
        books = json.load(f)
        return [Book(**b) for b in books]
 
def showcli():
    while True:
        print("\n ===== Book Store Menu =====")
        print("1. List All Books")
        print("2. Find All Books In Stock")
        print("3. Search Books By Author")
        print("4. Search Books By Genre")
        print("5. Search Books By Price Range")
        print("6. Find Books Published Before Year")
        print("7. Count Books Per Genre")
        print("8. Exit")
 
        choice = input("Please Select an Option : ")
 
        if choice == "1":
            for book in books:
                print(f"{book.book_id} - {book.title} by {book.author} - {book.genre} - ${book.price} - Published: {book.published_date} - Stock: {book.stock}")
 
        elif choice == "2":
            for book in books:
                if book.is_in_stock():
                    print(f"{book.book_id} - {book.title} - In Stock: {book.stock}")
 
        elif choice == "3":
            author = input("Enter the Author's Name: ").lower()
            for book in books:
                if author in book.author.lower():
                    print(f"{book.book_id} - {book.title} by {book.author}")
 
        elif choice == "4":
            genre = input("Enter Genre: ").lower()
            for book in books:
                if book.genre.lower() == genre:
                    print(f"{book.book_id} - {book.title} - Genre: {book.genre}")
 
        elif choice == "5":
            min_price = float(input("Enter Minimum Price: "))
            max_price = float(input("Enter Maximum Price: "))
            for book in books:
                if min_price <= book.price <= max_price:
                    print(f"{book.book_id} - {book.title} - ${book.price}")
 
        elif choice == "6":
            year = int(input("Enter the Year: "))
            for book in books:
                if int(book.published_date[:4]) < year:
                    print(f"{book.book_id} - {book.title} - Published: {book.published_date}")
 
        elif choice == "7":
            genre_count = {}
            for book in books:
                genre_count[book.genre] = genre_count.get(book.genre, 0) + 1
            for genre, count in genre_count.items():
                print(f"{genre} : {count} books")
 
        elif choice == "8":
            print("Exiting Bookstore CLI. Thank you!")
            break
        else:
            print("Invalid Choice. Please enter a number between 1 and 8")
 
if __name__ == "__main__":
    filepath = "books_data.json"
    books = load_books(filepath=filepath)
 
    if books:
        showcli()
    else:
        print("No books found or file is missing")

 