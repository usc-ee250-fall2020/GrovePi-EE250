FROM ubuntu:16.04

# Install required libraries
RUN apt-get update
ADD ./tcp_server.c ./
ADD ./server ./
RUN chmod +x ./server

EXPOSE 5000

CMD ["./server","5000"]

# run with docker run -d --restart always -p 500X:5000 {IMAGE_ID}
