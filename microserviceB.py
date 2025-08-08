# myBookNook Microservice B
# This microservice takes an ISBN and returns the Title, Author, and Description of the book

import isbnlib
import zmq

# Gets the title, author, and description for the specified ISBN
# Returns a dictionary with said information
def get_book_info(isbn):
    global title, author
    book_data = isbnlib.meta(isbn)

    for key, value in book_data.items():
        match key:
            case "Title":
                title = value
            case "Authors":
                author = value[0]

    description = isbnlib.desc(isbn)

    book_info = {
        "isbn": isbn,
        "title": title,
        "author": author,
        "description": description
    }

    return book_info


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")

while True:
    new_isbn = socket.recv_string()
    print(f"Received request from the client: {new_isbn}")
    if new_isbn == "Q":
        print("Ending connection.")
        break

    book_dict = get_book_info(new_isbn)
    socket.send_json(book_dict)

context.destroy()
