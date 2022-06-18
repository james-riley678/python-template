# Src directory
This directory will store all of your physical Python code, package manager [Pipenv](https://realpython.com/pipenv-guide/) and the static type checker [MyPy](https://mypy.readthedocs.io/en/stable/)

# Pipenv File
Pipenv is a packaging tool for Python that solves common problems associtated with the tpyical workflow using pip, virutalenv and requirements.txt. If you're familiar with Node. js's npm or Ruby's bundler, it is similar in spirit to those tools.

Note - There are other package / environment managers you can use. [Conda](https://docs.conda.io/en/latest/) is a good example.

# MyPy
Mypy is a static checker, it will find bugs in your programs without actually executing the program. Mypy is designed with gradual typing in mind. This means you can add type hints to your code base slowly and that you can always fall back to dynamic typing when static typing is not convenient.

Python File
```python
def greeting(name: str) -> str:
    return 'Hello ' + name

greeting(5)
```

Running Python file in terminal
```bash
$ pipenv run mypy filename.py

error: Argument 1 to "greeting" has incompatible type "int"; expected "str"
```