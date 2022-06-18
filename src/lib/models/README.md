# Models
This is where you store code that connects and runs queries against a database.

In this example it is MySQL / MariaDB.

When the module is imported, it returns a Pool connection to the database when you can get execute queries against the database using the functions of the Initialise class.
```python
from lib.models import Pool
from helpers import logger, config

sql: str = 'select id, age from people'
data = Pool.getData(sql)
logger.info(data)
```
```bash
$ pipenv run python app.py
[2022-04-22 20:14:15] [MainThread] {/apps/python-project-template/src/lib/models/__init__.py:21} INFO - Initialisng Maria pool: {"host" : "", "database" : "", "port" : "", "user" : "", "password" : "", "poolSize" : 2}
[2022-04-22 20:14:15] [MainThread] {/apps/python-project-template/src/app.py:20} INFO - [{'id': 1, 'age': 20}, {'id': 2, 'age': 11}]
```