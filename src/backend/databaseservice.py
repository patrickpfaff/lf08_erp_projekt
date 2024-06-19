import sqlite3
from log_level import LogLevel
from test_logger import TestLogger

class DatabaseService:
    __cursor: sqlite3.Cursor
    __connection: sqlite3.Connection
    __logger: TestLogger

    def __init__(self, file_name: str) -> None:
        try:
            fin_file_name: str = ""
            if ".db" in file_name:
                fin_file_name = file_name
            else:
                fin_file_name = file_name + ".db"
                
            self.__connection = sqlite3.connect(fin_file_name, check_same_thread=False)
            self.__cursor = self.__connection.cursor()
        except:
            print("Fehler beim Zugriff/der Erstellung der Datenbankdatei")
        self.__logger = TestLogger(LogLevel.DEBUG, "log.txt")

    def get_cursor(self) -> sqlite3.Cursor:
        """
        Gibt eine Referenz auf den aktuellen Cursor zurück
        """
        if self.__cursor is not None:
            return self.__cursor
        raise Exception("Cursor wurde nicht initialisiert!")
    
    def get_connection(self) -> sqlite3.Connection:
        """
        Gibt eine Referenz auf die aktuelle Datenbankverbindung zurück
        """
        if self.__connection is not None:
            return self.__connection
        raise Exception("DB Connection wurde nicht initialisiert!")
    
    def add_test_table(self) -> None:
        """
        Fügt eine Testtabelle hinzu
        """
        q = """
        CREATE TABLE IF NOT EXISTS test (
        id INT,
        name VARCHAR(20)
        );
        """
        self.execute_query(q)

    def delete_test_table(self) -> None:
        """
        Löscht die Testtabelle
        """
        q = """
        DROP TABLE IF EXISTS test;
        """
        self.execute_query(q)

    def execute_query(self, query) -> sqlite3.Cursor:
        self.__logger.LogDebug("Query: " + query)
        res = self.get_cursor().execute(query)
        self.get_connection().commit()
        return res
    
    def get_current_highest_id(self, table_name: str, id_column_name: str) -> int | None:
        q = f"""
        SELECT MAX({id_column_name}) from {table_name};
        """
        cur = self.execute_query(q)
        res_list = cur.fetchall()
        print(res_list)
        if not len(res_list) == 1 and len(res_list[0]) == 1:
            raise Exception("Antwort auf MaxId abfrage hat unerwartetes format:", res_list)
        else:
            return res_list[0][0]


        

