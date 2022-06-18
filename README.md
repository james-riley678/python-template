# Python Template
This service is a Python Template.

# Author
James Riley

# Run
```bash
python -m pip install --upgrade pip

pip install pipenv

cd src && pipenv install

pipenv run mypy app.py

pipenv run python app.py
```
Edit config.json file to the correct configuration

# Auto created files
The only file that will be automatically created is initiating a pipenv virtual environment using the command
```bash
pipenv --python 3.10
```
This command will auto create a Pipenv file.

When you begin installing Python packages, a Pipfile.lock file will be auto created. You should commit Pipenv.lock to git but never make any manual changes to it. Pipenv will sort it for you.

# Note 
This app is for python 3.10, if you are using a different version of Python, either install Python 3.10 or change the src/Pipenv at the bottom file to the version you are using (beware, some of the Pypi modules may not work if you use an older version).
```toml
[requires]
python_version = "3.10"
```