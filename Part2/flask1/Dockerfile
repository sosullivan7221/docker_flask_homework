# Select Docker python image from Docker registry
FROM python:3.7-alpine 

# Select file called 'app' as the docker working directory
WORKDIR /app1

# Copy all contents of file 'app' into the docker working directory
COPY . /app1

# Installing dependencies 
RUN pip install -r requirements.txt

# Port which app will be run on
EXPOSE 5000

# Terminal commands run to deploy app
CMD ["python", "app1.py"]

