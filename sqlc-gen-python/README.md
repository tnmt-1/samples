# sqlc-gen-python

## docs

https://docs.sqlc.dev/en/latest/overview/install.html

## run sqlc

```shell
cd src/sql
docker pull sqlc/sqlc
docker run --rm -v $(pwd):/src -w /src sqlc/sqlc generate
```

## run sample code

```shell
docker compose up -d
rye run python src/main.py
```
