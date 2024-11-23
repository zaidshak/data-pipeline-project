# Use a lightweight Python image as the base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the updated ingestion script into the container’s working directory
COPY ingest_data.py /app

# Install the required library
RUN pip install requests

# Set environment variables for the API key and city (optional for flexibility)
# Replace `your_api_key` with the actual OpenWeatherMap API key if you'd like to set it here
ENV API_KEY=3e27e015895e9b5c1c662edef0a97466
ENV CITY=London

# Specify the default command to run the ingestion script
CMD ["python", "ingest_data.py"]


