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

- Gitlab Runner, to install :

```bash
https://docs.gitlab.com/runner/install/windows.html
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
