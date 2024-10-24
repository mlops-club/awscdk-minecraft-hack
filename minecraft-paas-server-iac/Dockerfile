FROM --platform=linux/amd64 nikolaik/python-nodejs:python3.11-nodejs22-slim

USER root

# Install AWS CDK globally
RUN npm install -g aws-cdk

# Set the working directory
WORKDIR /app

# Copy dependency files and install them
COPY uv.lock pyproject.toml ./
RUN touch README.md \
    && uv sync --frozen

# Copy all files, including resources
COPY ./ ./  


# Set the virtual environment path
ENV PATH="/app/.venv/bin:${PATH}"

# Entry point for the container
ENTRYPOINT ["cdk"]
