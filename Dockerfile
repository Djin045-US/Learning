# Use an official lightweight Python image from Docker Hub
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your local script into the container's working directory
COPY HelloTest.py .

# Command to execute your Python script when the container starts
CMD ["python", "HelloTest.py"]
