# Use an official Python runtime as a parent image
FROM python:3.6

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 3007

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]

# docker build : docker build -t ashish/blockcypher-node .
# docker run : docker run -P -p 3003:3003 --network="host" ashish/blockcypher-node