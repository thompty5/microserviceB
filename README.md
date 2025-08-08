# microserviceB
Microservice B for myBookNook

This microservice acts as a server using ZeroMQ to communicate with the main program. It receives an already-validated ISBN from the main program, gets the title, author, and description, and returns a dictionary with the ISBN, title, author, and description to the main program.