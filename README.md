# IF2250-2023-K02-08-CookPaw

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

- pyuic5.exe and pyrcc5.exe from PyQt5, make sure to add these to environtment variables
- QT Designer, to install :

```bash
https://build-system.fman.io/qt-designer-download
```

- Docker, to install :

```bash
https://www.docker.com/products/docker-desktop/
```

## How to Run

Run from root directory

### Pytest

```bash
pytest -v
```

### GUI

To recompile [page]

```bash
pyuic5.exe src/ui/page/ui_page.ui -o src/ui/page/ui_page.py
pyrcc5.exe src/ui/page/resource_ui_page.qrc -o src/ui/page/resource_ui_page.py
```

For example page home : [home]

```bash
pyuic5.exe src/ui/home/ui_home.ui -o src/ui/home/ui_home.py
pyrcc5.exe src/ui/home/ui_home.qrc -o src/ui/home/ui_home_rc.py
```

To run

```bash
py src/ui/home/main_ui_home.py
```

### Docker and CI

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
