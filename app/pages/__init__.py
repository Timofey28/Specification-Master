from abc import ABC, abstractmethod
from database import Database
from data import db_dbname, db_host, db_user, db_password


class CurrentPage(ABC):
    def __init__(self):
        self.db = Database(db_dbname=db_dbname,
                           db_host=db_host,
                           db_user=db_user,
                           db_password=db_password)

    @abstractmethod
    def load_page(self) -> None:
        pass