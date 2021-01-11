# Todo List - Flask

## Creating a virtual env

- Install virtualenv package
  ```bash
  pip3 install virtualenv
  ```
- Create a virtualenv named env
  ```bash
  python3 -m venv env
  ```
- Activate
  ```bash
  source env/bin/activate
  ```
- Deactivating
  ```bash
  deactivate
  ```
- listing installed package
  ```bash
  pip freeze
  ```

## Installing flask

```bash
pip install flask
```

## Running flask application

If your `.py` file is named as `app.py` or `wsgi.py`, flask can auto detect the file. But any other filenames should be passed as an environment variable. If our filename was `main.py` then,

```bash
export FLASK_APP=main # no need of extension
```

## Activating debug mode

set `FLASK_ENV` environment variable to `development`

- bash
  ```bash
  export FLASK_ENV=development
  ```
- cmd
  ```cmd
  set FLASK_ENV=development
  ```
- powershell
  ```powershell
  $env:FLASK_ENV = "development"
  ```

with python code,

- add this line to `app.py`
  ```python
  app.run(debug=True)
  ```
- and then,
  ```bash
  python app.py #instead of flask run
  ```

# Changing the directory structure
```diff
    ├── todolist-flask
-       ├── templates
-       ├── static
-       ├── app.py
+       ├── app
+       │   ├── __init__.py
+       │   ├── templates
+       │   ├── static
+       │   ├── models.py
+       │   └── views.py
+       ├── config.py
+       ├── run.py
        ├── readme.md
        └── .gitignore
```

# Database Setup

- install `sqlalchemy` and `mysql-python`

```bash
pip install flask-sqlalchemy mysql-python
```

(`flask-sqlalchemy` is a wrapper library on `sqlalchemy` which is specially made for `flask`)

- Create new mysql db.
  -  can use phpmyadmin, adminer, sequelpro etc.
  <center>OR</center>

  ```
    $ mysql -u root

    mysql> CREATE USER 'johndoe'@'localhost' IDENTIFIED BY 'doejohn';
    Query OK, 0 rows affected (0.00 sec)

    mysql> CREATE DATABASE todolist-api;
    Query OK, 1 row affected (0.00 sec)

    mysql> GRANT ALL PRIVILEGES ON todolist-api . * TO 'johndoe'@'localhost';
    Query OK, 0 rows affected (0.00 sec)
  ```
  `!! use your db username and password wherever necessary`
