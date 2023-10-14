# Use a Python base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy Pipfiles into the container
COPY Pipfile Pipfile.lock /app/

# Install Pipenv and project dependencies
RUN pip install pipenv && pipenv install --system --deploy

# Copy the rest of your project files into the container
COPY . /app/

# Expose the port your application runs on
EXPOSE 8000

# Define the default command to run when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]