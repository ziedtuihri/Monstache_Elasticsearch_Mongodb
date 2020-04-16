# Use an official Python runtime as a parent image
FROM ubuntu

#Create folder
RUN mkdir app

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN apt-get update

# Set privilege 
RUN chmod a+x -R /app

# Run app.py when the container launches
CMD ./build/linux-amd64/monstache -f monstache.config.toml
