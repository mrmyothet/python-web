# Python Web Development with Flask

- programming
- variable
- naming conventions
- naming rules
- data types - number(integer, float), string, boolean
- static typing vs dynamic typing
- built-in functions
  - print() - display data at console
  - type() - return the type of data
- operators
  - arithmetic operators (add, sub, mul, div)

### Custom Ubuntu Linux Terminal with Themes and Plug-ins

- https://github.com/pixegami/terminal-profile
- https://github.com/ohmyzsh/ohmyzsh
- https://notes.leetdev.net/misc/ubuntu-setup

```bash

python3 -m pip config set global.break-system-packages true

```

```

python3 -m venv .venv
source .venv/bin/activate

pip install flask
pip list

flask --app app run --debug
flask --app app.py run --port 5000 --debug

```

```bash
==> postgresql@14
This formula has created a default database cluster with:
  initdb --locale=C -E UTF-8 /usr/local/var/postgresql@14

To start postgresql@14 now and restart at login:
  brew services start postgresql@14
Or, if you don't want/need a background service you can just run:
  /usr/local/opt/postgresql@14/bin/postgres -D /usr/local/var/postgresql@14
```
