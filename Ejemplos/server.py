from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
books = [
    {'id': 1, 'title': 'El principito', 'author': 'Antoine de Saint-Exupéry'},
    {'id': 2, 'title': 'Cien años de soledad', 'author': 'Gabriel García Márquez'}
]

# Endpoint to get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Endpoint to get a book by its ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

# Endpoint to create a new book
@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.get_json()
    new_book['id'] = len(books) + 1
    books.append(new_book)
    return jsonify(new_book), 201

# Endpoint to update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    updated_book = request.get_json()
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        book.update(updated_book)
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

# Endpoint to delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        books.remove(book)
        return jsonify({"message": "Book deleted successfully"})
    else:
        return jsonify({"error": "Book not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)