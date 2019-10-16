FROM python:3.6-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY docker-requirements.txt /app
COPY autoscheduler /app

# Shouldn't have to do python -m venv env & source it
RUN pip install -r docker-requirements.txt
# RUN chmod +x docker-entrypoint.sh

COPY docker-entrypoint.sh /usr/local/bin
ENTRYPOINT ["docker-entrypoint.sh"]