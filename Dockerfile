# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy the pyproject.toml and poetry.lock files to the container
COPY pyproject.toml poetry.lock /app/

# Install dependencies using Poetry
RUN poetry install --no-dev --no-root


# Copy the application code to the container
COPY ./app /app/app

# Copy the Alembic configurations
COPY ./alembic.ini /app/
COPY ./alembic /app/alembic

# Copy the .env file
COPY .env /app/


# Expose port 8000 for the FastAPI app
EXPOSE 8000


# Command to run the FastAPI app using uvicorn
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# Command to run Alembic migrations and then start the FastAPI app using uvicorn
# CMD ["sh", "-c", "poetry run alembic upgrade head && poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"]

