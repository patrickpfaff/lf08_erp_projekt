import sqlite3
from test_logger import LogLevel, TestLogger

class MitarbeiterDbSetup:
    """
    Klasse zum Einrichten der Datenbanktabellen für die Mitarbeiterverwaltung
    """
    __con: sqlite3.Connection
    __cur: sqlite3.Cursor
    __logger: TestLogger

    def __init__(self, con: sqlite3.Connection, cur: sqlite3.Cursor):
        self.__con = con
        self.__cur = cur
        self.__logger = TestLogger(LogLevel.DEBUG, "log.txt")
        
    def setup_mitarbeiter_db(self) -> None:
        """
        Stellt sicher dass die Datenbanktabellen für die Mitarbeiterverwaltung existieren
        """
        self.__setup_job_table()
        self.__setup_ort_table()
        self.__setup_adresse_table()
        self.__setup_mitarbeiter_und_abteilung_table()

    def __setup_job_table(self) -> None:
        self.__execute_query("""
        CREATE TABLE IF NOT EXISTS Job (
            Id int NOT NULL,
            Titel varchar(255) NOT NULL,
            PRIMARY KEY (Id)
        );""")
        self.__commit()

    def __setup_ort_table(self) -> None:
        self.__execute_query("""
        CREATE TABLE IF NOT EXISTS Ort (
            Plz varchar(6) NOT NULL,
            Name varchar(255) NOT NULL,
            PRIMARY KEY (Plz)
        );""")
        self.__commit()

    def __setup_adresse_table(self) -> None:
        self.__execute_query("""
        CREATE TABLE IF NOT EXISTS Adresse (
            Id int NOT NULL,
            Strasse varchar(255) NOT NULL,
            Hausnummer varchar(10) NOT NULL,
            Zusatz varchar(1024)
        );""")
        self.__commit()

        if not self.__check_if_column_exists("Adresse", "Plz"):
            self.__execute_query("""
            ALTER TABLE Adresse ADD COLUMN Plz varchar(6) NOT NULL REFERENCES Ort(Plz);""")
            self.__commit()

    def __setup_mitarbeiter_und_abteilung_table(self) -> None:
        self.__execute_query("""
        CREATE TABLE IF NOT EXISTS Mitarbeiter (
            Id int NOT NULL,
            Vorname varchar(255) NOT NULL,
            Nachname varchar(255) NOT NULL,
            Geburtsdatum varchar(255) NOT NULL,
            JobId int NOT NULL REFERENCES Job(Id),
            AdresseId int NOT NULL REFERENCES Adresse(Id),
            PRIMARY KEY (Id)
        );""")

        self.__execute_query("""
        CREATE TABLE IF NOT EXISTS Abteilung (
            Id int NOT NULL,
            Name varchar(255) NOT NULL,
            Beschreibung varchar(1024),
            PRIMARY KEY (Id)
        );""")

        self.__commit()

        if not self.__check_if_column_exists("Mitarbeiter", "AbteilungId"):
            self.__execute_query("""
            ALTER TABLE Mitarbeiter ADD COLUMN AbteilungId INTEGER NOT NULL REFERENCES Abteilung(Id);""")
            self.__commit()

        if not self.__check_if_column_exists("Abteilung", "LeiterId"):
            self.__execute_query("""
            ALTER TABLE Abteilung ADD COLUMN LeiterId INTEGER REFERENCES Mitarbeiter(Id);""")
            self.__commit()

    def __commit(self):
        self.__con.commit()

    def __check_if_column_exists(self, table_name: str, column_name: str) -> bool:
        # Testen, ob eine spalte bereits existiert
        # Gibt einen eintrag zurück wenn sie existiert
        self.__execute_query(f"""
        SELECT COUNT(*) AS CNTREC FROM pragma_table_info('{table_name}') WHERE name='{column_name}'
        """)
        self.__commit()
        res = self.__cur.fetchall()
        # print(res)
        return not res == [(0,)]
    
    def __execute_query(self, query) -> None:
        self.__logger.LogDebug("Query: " + query)
        self.__cur.execute(query)
            


