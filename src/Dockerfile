FROM python:3.10-slim

WORKDIR /app

# Install build tools
RUN pip install --upgrade pip setuptools wheel

# Copy only necessary files relative to the build context
# This assumes you run `docker build -f src/Dockerfile .` from the root dir
COPY pyproject.toml ./pyproject.toml
COPY src ./src
COPY run.py ./run.py

# Install your package in editable mode
ENV PYTHONPATH=/app/src
RUN pip install -e .

EXPOSE 5000

CMD ["python", "run.py"]
