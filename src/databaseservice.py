import sqlite3

class DatabaseService:
    __cursor: sqlite3.Cursor
    __connection: sqlite3.Connection

    def __init__(self, file_name) -> None:
        try:
            fin_file_name: str = ""
            if ".db" in file_name:
                fin_file_name = file_name
            else:
                fin_file_name = file_name + ".db"
                
            self.__connection = sqlite3.connect(fin_file_name)
            self.__cursor = self.__connection.cursor()
        except:
            print("Fehler beim Zugriff/der Erstellung der Datenbankdatei")

    def get_cursor(self) -> sqlite3.Cursor:
        if self.__cursor is not None:
            return self.__cursor
        raise Exception("Cursor wurde nicht initialisiert!")
    
    def get_connection(self) -> sqlite3.Connection:
        if self.__connection is not None:
            return self.__connection
        raise Exception("DB Connection wurde nicht initialisiert!")
    
    def add_test_table(self) -> None:
        q = """
        CREATE TABLE IF NOT EXISTS test (
        id INT,
        name VARCHAR(20)
        );
        """
        self.execute_query(q)

    def delete_test_table(self) -> None:
        q = """
        DROP TABLE IF EXISTS test;
        """
        self.execute_query(q)

    def execute_query(self, query) -> None:
        try:
            self.get_cursor().execute(query)
        except:
            raise 

        

