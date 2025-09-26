FROM python:3.11-slim

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /code/

COPY .env /code/.env


# Default command
CMD ["gunicorn", "erp_1_0.wsgi:application", "--bind", "0.0.0.0:8000"]
