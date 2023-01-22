**Getting Started**
These instructions will help you to run the API and test the endpoints.

**Prerequisites**

You will need to have the following software installed on your linux based system:
1. GIT
2. Docker
Note: Make sure docker service is up and running. If not use command 
$systemctl start docker

**Cloning the Repository**
To start, clone the repository to your local machine using the following command:
$ git clone https://github.com/uk1601/Assignment.git
This will create a copy of the repository in a new directory called "Assignment".

**Setting up and Running the system**
Navigate to the directory of the 3rd solution
$ cd Assignment/3/API/

Give the executable permissions to the two scripts in API directory.
$chmod +x build.sh start.sh

Run the build.sh script using command
$./build.sh

Redis server and API endpoints would be ready to use after the successful execution of the above step.

**Testing API Endpoints**
Check the IP address where you have hosted the above setup. Use the IP address in web browser to test the endpoint Add_word and autocomplete

"HTTP://<IP ADDRESS>/" # this would give you the default home page
"HTTP://<IP ADDRESS>/add_word/word=foo" #This would add the word foo to the redis db.
"HTTP://<IP ADDRESS>/autocomplete/query=f" #This would give you the suggestions i.e, words starting with f
"HTTP://<IP ADDRESS>/autocomplete/query=" #This blank query would give you all the words which are added previosuly.
 
NOTE: If any other endpoints are tried to access other than the above, this would give you a error page.
 
To check if the words added in redis server
Login to docker container using command
 $docker exec -it <containerid> /bin/bash
And Use the following command to list all the words
 $redis-cli zrange <key name> 0 -1 

NOTE: Keyname defined in this project is 'test'


NOTE:
  1. If AWS EC2 instance is used for the above process then make sure that the security groups are configured correctly for inbound requests.
  
