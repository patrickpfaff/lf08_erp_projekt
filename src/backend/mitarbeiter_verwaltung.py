import threading
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
    
    def get_all_mitarbeiter(self) -> list:
        q = """
        SELECT * FROM Mitarbeiter
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

    def add_mitarbeiter(self, vorname: str, nachname: str, geburtsdatum: str, angestelltSeit: str, job_id: int, abteilungId: int, hausnummer: str, strasse: str, zusatz: str, plz: str):
        max_id: int | None = self.__db_service.get_current_highest_id("Mitarbeiter", "Id")
        id: int = max_id if max_id is not None else 0

        max_adresse_id: int | None = self.__db_service.get_current_highest_id("Adresse", "Id")
        adresse_id: int = max_adresse_id if max_adresse_id is not None else 0

        q = f"""
        INSERT INTO Adresse (Id, Strasse, Hausnummer, Zusatz, Plz)
        VALUES ({str(adresse_id + 1)}, '{strasse}', '{hausnummer}', '{zusatz}', '{plz}')
        """
        self.__db_service.execute_query(q)
        q = f"""
        INSERT INTO Mitarbeiter (Id, Vorname, Nachname, Geburtsdatum, AngestelltSeit, JobId, AdresseId, AbteilungId)
        VALUES ({str(id + 1)}, '{vorname}', '{nachname}', '{geburtsdatum}', '{angestelltSeit}', {job_id}, {adresse_id +1}, {abteilungId})
        """
        self.__db_service.execute_query(q)

    def delete_mitarbeiter(self, id: int) -> None:
        q = f"""
        DELETE FROM Mitarbeiter WHERE Id = {id}
        """
        self.__db_service.execute_query(q)

    def get_ortsname_from_plz(self, plz: str) -> str:
        q = f"""
        SELECT Name FROM Ort WHERE Plz = '{plz}'
        """
        newcur = self.__db_service.execute_query(q)
        res = newcur.fetchall()
        if len(res) == 0:
            return "Ort nicht gefunden"
        return res[0][0]
    
    def get_all_jobs(self) -> list:
        q = """
        SELECT * FROM Job
        """
        new_cur = self.__db_service.execute_query(q)
        res_list = new_cur.fetchall()
        self.__logger.LogDebug("Query Response: " + str(res_list))
        return res_list
    
    def add_job(self, titel: str) -> None:
        max_id: int | None = self.__db_service.get_current_highest_id("Job", "Id")

        id: int = max_id if max_id is not None else 0
        q = f"""
        INSERT INTO Job (Id, Titel)
        VALUES ({str(id + 1)}, '{titel}')
        """
        self.__db_service.execute_query(q)

    def delete_job(self, id: int) -> None:
        q = f"""
        DELETE FROM Job WHERE Id = {id}
        """
        self.__db_service.execute_query(q)

    def get_job_by_id(self, id: int) -> tuple:
        q = f"""
        SELECT * FROM Job WHERE Id = {id}
        """
        res = self.__db_service.execute_query(q)
        return res.fetchall()[0]
    
    def get_adresse_by_id(self, id: int) -> tuple:
        q = f"""
        SELECT * FROM Adresse WHERE Id = {id}
        """
        res = self.__db_service.execute_query(q)
        return res.fetchall()[0]
        
