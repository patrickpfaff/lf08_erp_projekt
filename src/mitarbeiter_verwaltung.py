from databaseservice import DatabaseService
from log_level import LogLevel
from mitarbeiter_db_setup import MitarbeiterDbSetup
from test_logger import TestLogger


class MitarbeiterVerwaltung:
    """
    Klasse, welche die API für alle mitarbeiterverwaltungsrelevaten Funktionen bereitstellt
    """
    __db_service: DatabaseService
    __logger: TestLogger

    def __init__(self):
        self.__db_service = DatabaseService("test.db")
        self.__logger = TestLogger(LogLevel.DEBUG, "log.txt")

        self.__setup_db()

    def __setup_db(self) -> None:
        setup_helper = MitarbeiterDbSetup(
            self.__db_service.get_connection(),
            self.__db_service.get_cursor())
        setup_helper.setup_mitarbeiter_db()
        self.__logger.LogDebug("Mitarbeiter init complete.")

    def get_all_abteilungen(self) -> list:
        q = """
        SELECT * FROM Abteilung
        """
        new_cur = self.__db_service.execute_query(q)
        res_list = new_cur.fetchall()
        self.__logger.LogDebug("Query Response: " + str(res_list))
        return res_list


    def add_abteilung(self, beschreibung: str, name: str, leiterId: str = None, custom_id: int = None) -> None:
        # Aktuell höchste Id ermitteln:
        max_id: int | None = self.__db_service.get_current_highest_id("Abteilung", "Id")
        leiter: str = leiterId if leiterId is not None else "NULL"

        id: int = custom_id if custom_id is not None else max_id if max_id is not None else 0
        q = f"""
        INSERT INTO Abteilung (Id, Name, Beschreibung, LeiterId)
        VALUES ({str(id)}, '{name}', '{beschreibung}', '{leiter}')
        """
        self.__db_service.execute_query(q)

    def add_mitarbeiter(self, vorname: str, nachname: str, geburtsdatum: str, job_id: int, strasse: str, plz: str):
        pass

    def get_ortsname_from_plz(plz: str) -> str:
        
        
