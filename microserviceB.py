# myBookNook Microservice B
# This microservice takes an ISBN and returns the Title, Author, and Description of the book

from isbnlib import meta, desc
import zmq

# Gets the title, author, and description for the specified ISBN
# Returns a dictionary with said information
def get_book_info(isbn):
    book_data = meta(isbn)
    book_info = {"isbn": isbn}
    for key, value in book_data.items():
        match key:
            case "Title":
                book_info["title"] = value
            case "Authors":
                book_info["author"] = value[0]
    book_info["description"] = desc(isbn)

    return book_info


# Establish a socket to receive client connections
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
