FROM python:3.10-slim

WORKDIR /app

# Install test dependencies
RUN pip install --no-cache-dir pytest

# Copy framework files
COPY . .

# Ensure entrypoint is executable
RUN chmod +x entrypoint.sh

# Environment variables for default runs (can be overridden in pipeline)
ENV SCENARIO=""
ENV MODE="full"
ENV VIRTUAL_CAN_ACTIVE="1"

ENTRYPOINT ["./entrypoint.sh"]
