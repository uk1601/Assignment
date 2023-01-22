**app.py**

The above code is a Python script that uses the Flask web framework to create a simple API. The API has 3 endpoints for adding words, autocompleting words, and the default endpoint for the home page. The script also uses the Redis database to store the words that are added by the user.

The script starts by importing the necessary libraries, redis and flask. 
Then it sets the Redis connection by specifying the host, port, and key. The redis connection r = redis.Redis(host='127.0.0.1',port=6379) connects to a Redis server on the localhost IP address, on the default port 6379. 
The redis_key variable redis_key='test' is used as a key for Redis commands to operate on the specific data.

It creates an instance of the Flask application app = Flask(__name__) and defines the endpoints for the API using decorators.

The home endpoint @app.route('/', methods = ['GET']) returns a simple string message that explains the functionality of the API.

The add_word endpoint @app.route('/add_word/word=<word>', methods = ['GET']) accepts a word as a parameter and stores it in the Redis database using the ZADD command. The word variable passed as a parameter, is added to a dictionary with a value of 1, and it is passed as an argument to the Redis zadd() method. The zadd command is used to add one or more members to a sorted set, or update its score if it already exists.

The autocomplete endpoint @app.route('/autocomplete/query=<query>', methods = ['GET']) accepts a query as a parameter, then it uses the ZRANGEBYLEX command to retrieve the words from the Redis database that match the query. It returns the matching words in a list. If the query parameter is empty it will return all the words in the redis.

The script also includes error handling for a 404 error using @app.errorhandler(404) which returns a message “Error 404 occured” when an error 404 occurs.

Finally, the script runs the Flask app on the host IP of 0.0.0.0 using if __name__ == '__main__': and app.run(host='0.0.0.0'). This makes the app accessible from anywhere on the network by specifying the IP address of the host machine.


**Dockerfile**

The Dockerfile creates an image that runs a Python application using the Flask web framework and Redis. The file contains a series of instructions that get executed in order to create the image.

1. The first instruction FROM redis:latest specifies that the image should be based on the official Redis image, using the latest version available.
2. The next instruction RUN apt -y update updates the package list on the image to the latest version.
3. The next instruction RUN apt -y install python3 python3-pip curl installs Python3, Python3-pip, and curl which are required for running the application.
4. The next instruction RUN pip install redis flask installs the Redis and Flask python packages.
5. The next instruction RUN mkdir /app creates a new directory called app in the root of the image.
6. The next instruction COPY app.py /app/app.py copies the app.py file from the host machine to the /app directory on the image.
7. The next instruction COPY start.sh /app/start.sh copies the start.sh file from the host machine to the /app directory on the image.
8. The next instruction EXPOSE 5000 maps the container's port 5000 to the host machine.
9. The last instruction CMD ["/bin/bash","/app/start.sh"] specifies the command that should be run when the container starts. In this case, it is running the start.sh shell script.

Overall, this Dockerfile specifies all the steps required to create an image that runs a Python application using the Flask web framework and Redis, by installing the necessary dependencies, copying the required files, and running the command to start the application.
  
**start.sh**

The above code is a Bash script that starts a Redis server and runs a Python application.

The first command redis-server --daemonize yes starts the Redis server and runs it in the background as a daemon process. The --daemonize yes option tells Redis to run as a daemon in the background.

The next command python3 /app/app.py runs the Python script app.py located in the /app directory. This script is the main application that uses the Flask web framework and Redis.
  
**build.sh**
  
The above code is a Bash script that creates and runs a Docker container for a specific image.

The first command sudo docker build -t myapi:latest . creates a Docker image using the Dockerfile in the current directory. The . at the end specifies the current directory. The -t option specifies a name and a tag for the image, in this case, it's named myapi and tagged as latest.

The next command sudo docker run -d -p 80:5000/tcp myapi runs a Docker container in detached mode using the image created by the previous command. The -d option specifies detached mode, which runs the container in the background. The -p option maps the host machine's port 80 to the container's port 5000. The myapi at the end specifies the image to use for the container.
  
  
  
Overall, RUN the build.sh script manually which builds and starts a container. It executes the flask app file and installs redis while creating the container. Also, it exposes container's 5000 port to host machine's 80. Thereby it can be accessed using hostmachine's ip and port and execute API endpoints.
