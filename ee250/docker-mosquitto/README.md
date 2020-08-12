# ee250 Docker Image Instructions

Run a container using the official `eclipse-mosquitto` image on docker hub on 
a server with a static IP. Below is an example of how to run the image so
it restarts if the server reboots or the image crashes. Also, the command
maps port 11000 on the server to port 1883 inside the container.

```
docker run -d --restart="always" --name ee250-mosquitto -p 11000:1883 eclipse-mosquitto 
```

If you have `mosquitto-clients` installed, you can test the mosquitto broker
inside the container using command line. For example, in one terminal, execute:

```
mosquitto_sub -h yourhostname.usc.edu -p 11000 -t myTopic/mySubtopic
```

In another terminal, execute:

```
mosquitto_pub -h yourhostname.usc.edu -p 11000 -t myTopic/mySubtopic -m "this is a test"
```
