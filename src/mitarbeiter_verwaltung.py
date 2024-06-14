from databaseservice import DatabaseService


class Mitarbeiter_Verwaltung:
    __db_service: DatabaseService

    def __init__(self):
        self.__db_service = DatabaseService("test.db")