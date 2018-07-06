import os
from dataclasses import dataclass


@dataclass
class setting:
    PGHOST: str = os.getenv('PGHOST', 'default')
    PGDBNAME: str = os.getenv('PGDBNAME', 'default')
    PGUSER: str = os.getenv('PGUSER', 'postgres')
