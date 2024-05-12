# Stage 1: Build the application
FROM python:3.9-slim AS builder

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install Python packages to a temporary directory
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage 2: Create the final lightweight image
FROM python:3.9-slim

# Copy installed Python dependencies from the builder stage
COPY --from=builder /root/.local /root/.local

# Add the local bin directory to the PATH
ENV PATH=/root/.local/bin:$PATH
ENV DATABASE_URI=postgresql://postgres:postgres@localhost:5432/postgres
ENV SECRET_KEY=your_secret_key

# Set the working directory in the container
WORKDIR /app

# Copy the application code
COPY . .

# Run the application
CMD ["python", "run.py"]
