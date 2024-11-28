FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Add source code in the container
COPY . /app

# Define container entry point (could also work with CMD python main.py)
CMD ["fastapi", "run", "app/main.py", "--port", "80"]