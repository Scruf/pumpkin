import os
from sqlalchemy import create_engine


class Connection:

    def __init__(self):
        self.__db = create_engine(f'mysql://pumpkin:password@{os.environ["EGOR_PUMPKIN_DB_IP"]}:3306/Pumpkin')
        self.__connection = self.__db.connect()

    def get_connection(self):
        return self.__connection
