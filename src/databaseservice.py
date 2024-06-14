import sqlite3
from mitarbeiter_db_setup import MitarbeiterDbSetup

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

    def setup_db(self) -> None:
        setup_helper = MitarbeiterDbSetup(self.get_connection(), self.get_cursor())

        setup_helper.setup_mitarbeiter_db()

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
        print("Query: ", query)
        res = self.get_cursor().execute(query)
        self.get_connection().commit()
        return res
            

        

