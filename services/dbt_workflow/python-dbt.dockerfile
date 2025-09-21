FROM python:3.13-slim-bookworm

WORKDIR /app

COPY ./dbt_workflow/ /app/dbt_workflow/
COPY ./uv.lock /app/uv.lock
COPY ./pyproject.toml /app/pyproject.toml

ENV UV_PROJECT_ENVIRONMENT="/usr/local/"
RUN mkdir 'datawarehouse' && \
pip install uv && \
uv sync --locked --no-dev

WORKDIR /app/dbt_workflow

CMD ["dbt", "run"]

#https://www.reddit.com/r/learnpython/comments/1hspt62/installing_dependencies_with_uv_sync_systemwide/?tl=pt-br


