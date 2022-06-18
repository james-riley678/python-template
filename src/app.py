# This is the source file that you will execute when running the project.
# "cd src/ && pipenv run python app.py"

# MyPy for Static Typing
from typing import List, Set, Dict, Tuple, Optional, Any, Iterable, Union

# Custom Modules
from helpers import config, logger

# PyPi Modules

def app() -> None:

    logger.info('Starting')
    logger.info(config)
    logger.info('Ended...')

if __name__ == "__main__":
    app()
