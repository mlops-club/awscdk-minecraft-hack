FROM --platform=linux/amd64 nikolaik/python-nodejs:python3.11-nodejs22-slim

RUN npm install -g aws-cdk

WORKDIR /app

COPY uv.lock pyproject.toml ./
RUN touch README.md \
    && uv sync --frozen

COPY ./ ./
RUN uv sync --frozen

ENTRYPOINT ["uv", "run", "--", "cdk"]