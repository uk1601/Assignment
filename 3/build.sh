#!/bin/bash
sudo docker build -t myapi:latest . 
sudo docker run -d -p 80:5000/tcp myapi #binding the 80 port number to 5000 port number of the container 