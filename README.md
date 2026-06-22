# nklf1
A flask app to make routine tasks of a hospital neurologist easier.

## Run locally for development
```
uv sync
uv pip install -e .
uv run python3 main.py
```

## Run as podman container for production
```
sudo podman build . -t nklf1
sudo podman run -p 8880:8880 --env-file .env -d nklf1
```
