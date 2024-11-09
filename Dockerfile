# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Expose the application port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
