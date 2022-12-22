from app import db
# Subclass db.Model is used to define a model class.
# The model will generate a table name by converting the CamelCase class name to snake_case.
# The table name "book" will automatically be assigned to the model’s table.

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)