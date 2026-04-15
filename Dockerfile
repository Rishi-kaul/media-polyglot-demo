# Use lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Expose port for local server
EXPOSE 5000

# Run the script
CMD ["python", "polyglot_tool.py"]