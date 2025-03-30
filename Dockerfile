FROM python:3.10-slim

# Install uv.
RUN pip install uv
# Copy the application into the container.
COPY . .

# Install the application dependencies.
WORKDIR .
RUN uv sync --frozen --no-cache

# Run the application.
CMD ["uv", "run", "uvicorn", "src.main:app", "--port", "8000", "--host", "0.0.0.0"]