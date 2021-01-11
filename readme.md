#  Todo List - Flask

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