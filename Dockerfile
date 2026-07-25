# This Dockerfile creates a lightweight Docker image. It copies seg_pipeline,
# install the dependencies and sets the entrypoint to run_seg.py.

# Python base image.
FROM python:3.11-slim

# Optional metadata.
LABEL maintainer="Pedro <pedronovaesmelo@gmail.com>"

# Define workdir inside docker container.
WORKDIR /app

# Copy package and entrypoint script.
COPY seg_pipeline /app/seg_pipeline
COPY run_seg.py /app/run_seg.py
COPY requirements.txt /app/requirements.txt

# Install dependencies.
RUN apt update \
    && apt install -y --no-install-recommends build-essential \
    && pip install --no-cache-dir -r /app/requirements.txt \
    && apt remove -y build-essential \
    && apt autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# Ensure Python can find the package.
ENV PYTHONPATH=/app

# Create non-root user.
RUN useradd -m -s /bin/bash appuser && chown -R appuser:appuser /app
USER appuser

# Define container executable.
ENTRYPOINT ["python", "/app/run_seg.py"]
CMD []
