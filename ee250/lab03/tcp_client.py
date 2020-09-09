"""
Name: Mohaimen Syed
Github: https://github.com/mohaimensyed/GrovePi-EE250.git

Server IP is 52.88.20.156, ports are 5000-5008, socket is UNIX TCP 
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
"""
import socket


IP = '54.153.68.109'
PORT = 5010

def main():

	#Ask for a message to send to server
	user_in = input("Send Message: ")
	message = bytes(user_in, 'utf-8')
    
	# TODO: Create a socket and connect it to the server at the designated IP and por
	soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	soc.connect((IP, PORT))

	# TODO: Get user input and send it to the server using your TCP socket
	soc.send(message)

	# TODO: Receive a response from the server and close the TCP connection
	response = str(soc.recv(256), 'utf-8')
	soc.close()

	#Prints response from server
	print('Server: ' + response)

if __name__ == '__main__':
    main()
