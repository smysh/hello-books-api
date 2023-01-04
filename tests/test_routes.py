def test_get_all_books_with_no_records(client):
    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_all_books_with_two_books(client, two_saved_books):
    # Act
    response = client.get("/books")
    book_list = response.get_json()
    # Assert
    assert response.status_code == 200
    assert len(book_list) == 2
    assert book_list[0]["title"] == two_saved_books[0].title
    assert book_list[0]["id"] == two_saved_books[0].id
    assert book_list[0]["description"] == two_saved_books[0].description
    
    assert book_list[1]["title"] == two_saved_books[1].title
    assert book_list[1]["id"] == two_saved_books[1].id
    assert book_list[1]["description"] == two_saved_books[1].description

def test_get_one_book(client, two_saved_books):
    # Act
    response = client.get("/books/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body["title"] == two_saved_books[0].title
    assert response_body["id"] == two_saved_books[0].id
    assert response_body["description"] == two_saved_books[0].description
 