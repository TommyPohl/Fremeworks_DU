from flask import Flask, render_template

app = Flask(__name__)

books = [
    {"title": "1984", "author": "George Orwell", "available": True},
    {"title": "Sto roků samoty", "author": "Gabriel García Márquez", "available": False},
    {"title": "Hobit", "author": "J.R.R. Tolkien", "available": True},
    {"title": "Malý princ", "author": "Antoine de Saint-Exupéry", "available": False},
]

@app.route("/books")
def book_list():
    return render_template("books.html", books=books)

if __name__ == "__main__":
    app.run(debug=True)
