from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, make_response, request

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

@books_bp.route("", methods=["POST"])
def create_book():
    request_body = request.get_json()
    new_book = Book(title=request_body["title"],
                    description=request_body["description"])

    db.session.add(new_book)
    db.session.commit()
    # make_response converts the return value from a view function to an instance of response_class.
    # str : A response object is created with the string encoded to UTF-8 as the body.
    # bytes : A response object is created with the bytes as the body.
    # dict : A dictionary that will be jsonify’d before being returned.
    # list : A list that will be jsonify’d before being returned.
    # generator or iterator : A generator that returns str or bytes to be streamed as the response.
    # tuple : Either (body, status, headers), (body, status), or (body, headers), 
    # where body is any of the other types allowed here, status is a string or an integer, 
    # and headers is a dictionary or a list of (key, value) tuples. 
    # If body is a response_class instance, status overwrites the exiting value and headers are extended.
    return make_response(f"Book {new_book.title} successfully created", 201)

@books_bp.route("", methods=["GET"])
def read_all_books():
    books_response = []
    # Flask-SQLAlchemy provides a query attribute on your Model class. 
    # When you access it you will get back a new query object over all records. e.g.query.all()
    # You can then use methods like filter() to filter the records before you fire the select with all() or first(). 
    # e.g. missing = User.query.filter_by(username='missing').first()
    # e.g. User.query.filter(User.email.endswith('@example.com')).all()
    # Ordering users by something: e.g. User.query.order_by(User.username).all()
    # Limiting users: e.g. User.query.limit(1).all()
    # If you want to go by primary key you can also use get() : e.g. User.query.get(1)
    books = Book.query.all()
    for book in books:
        books_response.append(
            {
                "id": book.id,
                "title": book.title,
                "description": book.description
            }
        )
    # Serialize the given arguments as JSON, and return a Response object with the application/json mimetype. 
    # A dict or list returned from a view will be converted to a JSON respon
    return jsonify(books_response)

#def validate_book(book_id):
#    try:
#        book_id = int(book_id)
#    except:
#        abort(make_response({"message":f"book {book_id} invalid"}, 400))
#
#    for book in books:
#        if book.id == book_id:
#            return book
#
#    abort(make_response({"message":f"book {book_id} not found"}, 404))
        
# @books_bp.route("/<book_id>", methods=["GET"])
# def handle_book(book_id):
#     book = validate_book(book_id)
#
#     return {
#           "id": book.id,
#           "title": book.title,
#           "description": book.description,
#     }


