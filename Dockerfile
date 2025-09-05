FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt
COPY requirements-dev.txt requirements-dev.txt

ARG INSTALL_DEV=true
RUN if [ "$INSTALL_DEV" = "true" ]; then \
      pip install -r requirements-dev.txt; \
    fi \
 && pip install -r requirements.txt

COPY . .
COPY justfile justfile
