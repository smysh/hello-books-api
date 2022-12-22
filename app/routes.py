
from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, abort, make_response, request
# A Blueprint is a way to organize a group of related views and other code. 
# Rather than registering views and other code directly with an application, they are registered with a blueprint.
# Parameters
# name (str) – The name of the blueprint. Will be prepended to each endpoint name.
# import_name (str) – The name of the blueprint package, usually __name__. This helps locate the root_path for the blueprint.
# static_folder (Optional[Union[str, os.PathLike]]) – A folder with static files that should be served by the blueprint’s static route.
# static_url_path (Optional[str]) – The url to serve static files from. Defaults to static_folder. 
# template_folder (Optional[str]) – A folder with templates that should be added to the app’s template search path. 
# Blueprint templates have a lower precedence than those in the app’s templates folder.
# url_prefix (Optional[str]) – A path to prepend to all of the blueprint’s URLs, to make them distinct from the rest of the app’s routes.
# subdomain (Optional[str]) – A subdomain that blueprint routes will match on by default.
# url_defaults (Optional[dict]) – A dict of default values that blueprint routes will receive by default.
# root_path (Optional[str]) – By default, the blueprint will automatically set this based on import_name. 
# cli_group (Optional[str]) –
books_bp = Blueprint("books_bp", __name__, url_prefix="/books/")
# Decorating a function with a blueprint creates a deferred function that is called with BlueprintSetupState 
# when the blueprint is registered on an application.
# The methods parameter defaults to ["GET"]. 
@books_bp.route("", methods=["POST"])
def handle_books():
    # request is used to access incoming request data
    # Parses the incoming JSON request data and returns it
    request_body = request.get_json()
    new_book = Book(title=request_body["title"],
                    description=request_body["description"])
    # To insert data, pass the model object to db.session.add():
    db.session.add(new_book)
    db.session.commit()
    # The above operation will commit the transaction that was in progress.
    return make_response(f"Book {new_book.title} successfully created", 201)

