# docker_flask_homework
Dockerizing Flask Applications


## Docker Steps

1. Create a folder that contains your app.py file, your requirements.txt file, and the Dockerfile configured to search for and run your app.py file.
2. Build the docker image using: docker build -t <image_name> .
3. Run the docker image in a container using: docker run -p <port>:5000 <image_name>. Adding -d as an argument will detach the container, allowing it to be accessed without the flask app running directly through the terminal.
4. Commands to end the process:
    Stop container: docker stop <container-id>
    Remove container: docker rm <container-id>
    Remove all containers and images: docker system prune -a -f


## Docker Compose

Docker-compose works to combine multiple docker files into one instance so they can be run together. My example takes two Flask apps that are open on two different ports.

1. Create a folder with a docker-compose.yaml file, and two subfolders that each contain an app.py file, a requirements.txt file, and a Dockerfile. Configure the docker-compose file to specify the order in which the apps are run and on which port each one is run.
2. To build the image, use: docker-compose build
3. To run the image in a container, use: docker-compose run. You should be able to preview your app and change the port to swap between your Flask apps.
4. To remove all instances, use: docker-compose down -v --rmi all --remove-orphans
   
