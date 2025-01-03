# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install PostgreSQL development libraries (for psycopg2 build)
RUN apt-get update && \
    apt-get install -y \
    libpq-dev && \
    apt-get clean

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run Scrapy when the container starts
CMD ["scrapy", "crawl", "scraper"]
