# COOKPAW RECIPE APPLICATION

## ABOUT PROGRAM

Cookpaw adalah aplikasi recipe........

## Prerequisites

- Python 3.X
- pip (make sure to add the path to environtment variables)
- pytest, to install :

```bash
pip install pytest
```

- PyQt5, to install :

```bash
pip install PyQt5
```

- PIL, to install:

```bash
pip install pillow
```

- Docker, to install :

```bash
https://www.docker.com/products/docker-desktop/
```

## How to Run

Make sure you run it from the root directory

### Pytest

Recommended db harus baru

1. Delete `cookpaw.db` di directory `src/database/`
2. Initialize new db

```bash
py src/database/db.py
```

3. Run pytest

```bash
pytest -v
```

### GUI

To run
secara default, db sudah ada, in case tidak ada `cookpaw.db` di `src/database` , run :

```bash
py src/database/db.py
```

Jika db sudah ada

```bash
py src/main.py
```

### Docker and CI

This application development use CI/CD with `test` stage for testing the application using PyTest. The CI/CD runs on a docker runner implemented for this project. It is recommended just to pull the docker image by following the instructions below.

#### For building new runner

- Build the docker

```bash
docker build -t gitlab-runner-rpl-k02-g08 .
```

- Set the tag of the runner and where to push

```bash
docker tag gitlab-runner-rpl-k02-g08:latest jeffreychow19/gitlab-runner-rpl-k02-g08:latest
```

- Login to docker hub if not yet logged in

```bash
docker login
```

- Push docker image to the docker hub

```bash
docker push jeffreychow19/gitlab-runner-rpl-k02-g08:latest
```

- Create container in docker

```bash
docker run -d --name gitlab-runner-rpl-k02-g08 -v /var/run/docker.sock:/var/run/docker.sock jeffreychow19/gitlab-runner-rpl-k02-g08:latest
```

#### For pulling docker

- Pull the image from docker

```bash
docker pull jeffreychow19/gitlab-runner-rpl-k02-g08:latest
```

- Create container in docker

```bash
docker run -d --name gitlab-runner-rpl-k02-g08 -v /var/run/docker.sock:/var/run/docker.sock jeffreychow19/gitlab-runner-rpl-k02-g08:latest
```

## DAFTAR MODUL

## AUTHOR and PEMBAGIAN TUGAS

## TABEL BASIS DATA
