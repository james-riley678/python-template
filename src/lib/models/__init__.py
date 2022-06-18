# MyPy for Static Typing
from typing import List, Set, Dict, Tuple, Optional, Any, Iterable, Union

# Custom Modules
from helpers import logger, config

# PyPi Modules
import json
import mysql.connector.pooling as pooling
from pandas.core.frame import DataFrame
import pandas as pd
from mysql.connector.errors import PoolError
import threading


class Initialise:

    def __init__(self) -> None:

        self.pool_connections: Dict[Any, Any] = {}

        self.pool_cursors: Dict[Any, Any] = {}

        maria_det: dict = config['database']

        try:
            logger.info(f'Initialisng Maria pool: {maria_det}')
            self.pool = pooling.MySQLConnectionPool(
                pool_size=maria_det.get('poolSize'),
                pool_reset_session=False,
                host=maria_det.get('host'),
                database=maria_det.get('database'),
                port=maria_det.get('port'),
                user=maria_det.get('user'),
                password=maria_det.get('password'),
                autocommit=True
            )
        except Exception as error:
            logger.error(f'Unable to connect to maria database, with error: {error}')
            raise

    def acquire(self, autocommit: bool = True) -> None:
        threadName: str = threading.current_thread().name
        try:
            self.pool_connections[threadName] = self.pool.get_connection()
            self.pool_cursors[threadName] = self.pool_connections[threadName].cursor()
        except Exception as error:
            if type(error) is PoolError and error.args[1] == 'Failed getting connection; pool exhausted':
                self.pool.add_connection()
                self.addConnection = True
                self.pool_connections[threadName] = self.pool.get_connection()
                self.pool_cursors[threadName] = self.pool_connections[threadName]
            else:
                raise

    def release(self) -> None:
        threadName: str = threading.current_thread().name
        self.pool_connections[threadName].close()

    def getData(self, sql, bindings=None, dataframe=None):
        threadName: str = threading.current_thread().name
        cursor = self.pool_cursors[threadName]
        try:
            if bindings:
                cursor.execute(sql, bindings)
            else:
                cursor.execute(sql)
        except Exception as error:
            raise MariaError(f"Unable to retrieve data with error: {error}")

        columns = [field[0] for field in cursor.description]
        data = cursor.fetchall()
        result = []
        for x in data:
            result.append(list(x))

        for i, x in enumerate(result):
            for j, y in enumerate(x):
                try:
                    x[j] = json.loads(y)
                except json.decoder.JSONDecodeError:
                    x[j] = y
            data[i] = x

        if dataframe:
            if len(result) > 0:
                return pd.DataFrame(data=result, columns=columns)
            else:
                return pd.DataFrame(data=[], columns=columns)
        else:
            return [dict(zip(columns, x)) for x in result]

    def execute(self, sql, params=None):
        threadName: str = threading.current_thread().name
        cursor = self.pool_cursors[threadName]
        try:
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
        except Exception as error:
            raise MariaError("Unable to execute statement, with error: {}".format(error))

    def executeMany(self, sql, batchData, batchLimit):
        threadName: str = threading.current_thread().name
        cursor = self.pool_cursors[threadName]
        try:
            for i in range(0, len(batchData)+batchLimit, batchLimit):
                cursor.executemany(
                    sql,
                    batchData[i:i+batchLimit]
                )
        except Exception as error:
            raise MariaError("Unable to executemany statement, with error: {}".format(error))

    def insert(self, sql, params=None):
        threadName: str = threading.current_thread().name
        cursor = self.pool_cursors[threadName]
        try:
            cursor.execute(sql, params)
        except Exception as error:
            raise MariaError("Unable to execute statement, with error: {}".format(error))


class MariaError(Exception):
    pass


Pool: Initialise = Initialise()
