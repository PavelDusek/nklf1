FROM python:latest

WORKDIR /app

COPY pyproject.toml requirements.txt ./
RUN pip install --no-cache-dir .

COPY app/ ./app/
COPY static/ ./static/
COPY wsgi.py .

# Not to bake .env file into the container, we comment the next line:
# COPY .env .
# and run
# sudo podman build . -t nklf1
# sudo podman run -p 8888:80 --env-file .env nklf1

EXPOSE 8880

CMD ["gunicorn", "--bind", "0.0.0.0:8880", "wsgi:app"]
