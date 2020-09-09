Mohaimen Syed
EE250 - Lab03

A.	
	1. The sequence of 1 to 10 were not completely transferred since I observed that
	   a few of the numbers were missing on the other terminal. This was because UDP
	   does not have a mechanism for error recovery and so data was lost while transmission,
	   and the incomplete data was received by the application layer.

	2. The sequence of 1 to 10 was completely transferred and I received all the numbers
		on the other end. This was because there is a mechanism for error recovery on the tcp channel
		so data is received in the sequence of how it was received by the application layer.

	3.	The speed of the TCP response was slower after a 50% loss, since the tcp channel waited for
		all the packets of data before sending it to the application layer and with a connection with more
		latency it took a longer time.


C.

    1. argc and argv[] are the parameters that hold the values of the command line arguements entered when running the program.
       argc is the number of command line arguements and arv[] holds the strings entered.

    2. A file descriptor is a number that uniquely representsan opened file in the operating system, and a file
       descriptor table holds all the file descriptors.

    3. Structs are blueprints that are used to create the instance of a class, it holds a collection of
       data members that represent the struct. sockaddr_in holds data members sin_family, sin_port, sin_ddr, sin_zero[], that represents the socket type, port and address.

    4. The parameters are domain, type and protocol, and the return type is an integer.

    5. The parameters of bind() are sockfd, *servaddr, addrlen, and for listen() are sockfd and backlog.

    6. The server will only listen to the messages coming from one client and ignore the clients since it will be inside
       the infinite while loop. 

    7. The fork() function can be used to listen and respond to multiple clients. All child processes will run concurrently
       after a call to fork has been made. And each identical fork() can respond to each client.