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

    ###
    ### INIT ###
    ###

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




    ###
    ### ABTEILUNGEN ###
    ###
    
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
        leiter: str = leiterId if leiterId is not None else None
        leiter_id_sql: str = f"'{leiter}'" if leiter is not None else "NULL"

        id: int = custom_id if custom_id is not None else max_id + 1 if max_id is not None else 0
        q = f"""
        INSERT INTO Abteilung (Id, Name, Beschreibung, LeiterId)
        VALUES ({str(id)}, '{name}', '{beschreibung}', {leiter_id_sql})
        """
        self.__db_service.execute_query(q)

    def get_abteilung_by_id(self, id: int) -> tuple:
        q = f"""
        SELECT * FROM Abteilung WHERE Id = {id}
        """
        cur = self.__db_service.execute_query(q)
        res = cur.fetchall()
        if len(res) == 0:
            return None
        return res[0]
    
    def update_abteilung(self, id: int, beschreibung: str, name: str, leiterId: str = None) -> None:
        leiter_id_sql: str = f"'{leiterId}'" if leiterId is not None else "NULL"
        q = f"""
        UPDATE Abteilung SET Name = '{name}', Beschreibung = '{beschreibung}', LeiterId = {leiter_id_sql} WHERE Id = {id}
        """
        self.__db_service.execute_query(q)

    def delete_abteilung(self, id: int) -> None:
        q = f"""
        DELETE FROM Abteilung WHERE Id = {id}
        """
        self.__db_service.execute_query(q)



    ###
    ### MITARBEITER ###
    ###

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

    def get_mitarbeiter_by_id(self, id: int) -> tuple:
        q = f"""
        SELECT * FROM Mitarbeiter WHERE Id = {id}
        """
        cur = self.__db_service.execute_query(q)
        res = cur.fetchall()
        if len(res) == 0:
            return None
        return res[0]
    
    def get_all_mitarbeiter(self) -> list:
        q = """
        SELECT * FROM Mitarbeiter
        """
        new_cur = self.__db_service.execute_query(q)
        res_list = new_cur.fetchall()
        self.__logger.LogDebug("Query Response: " + str(res_list))
        return res_list
    
    def update_mitarbeiter(
        self,
        id: int,
        vorname: str,
        nachname: str,
        geburtsdatum: str,
        angestelltseit: str,
        jobId: int,
        abteilungId :int,
        strasse: str,
        hausnummer: str,
        zusatz: str,
        plz: str):
    
        # get mitarbeiter
        m_q: str = f"""
        SELECT * FROM Mitarbeiter WHERE Id = {id}
        """
        m_cur = self.__db_service.execute_query(m_q)
        m_res = m_cur.fetchall()
        if len(m_res) == 0:
            return None
        m = m_res[0]

        # get current adresse
        a_q: str = f"""
        SELECT * FROM Adresse WHERE Id = {m[6]}
        """
        a_cur = self.__db_service.execute_query(a_q)
        a_res = a_cur.fetchall()
        if len(a_res) == 0:
            return None
        a = a_res[0]

        # compare current adresse with new adresse
        if a[1] != strasse or a[2] != hausnummer or a[4] != zusatz or a[3] != plz:
            # update adresse
            q = f"""
            UPDATE Adresse SET Strasse = '{strasse}', Hausnummer = '{hausnummer}', Zusatz = '{zusatz}', Plz = '{plz}' WHERE Id = {m[6]}
            """
            self.__db_service.execute_query(q)

        # update mitarbeiter
        q = f"""
        UPDATE Mitarbeiter SET Vorname = '{vorname}', Nachname = '{nachname}', Geburtsdatum = '{geburtsdatum}', AngestelltSeit = '{angestelltseit}', JobId = {jobId}, AbteilungId = {abteilungId} WHERE Id = {id}
        """
        self.__db_service.execute_query(q)




    ###
    ### JOBS ###
    ###
    
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
        cur = self.__db_service.execute_query(q)
        res = cur.fetchall()
        if len(res) == 0:
            return None
        return res[0]
    
    def update_job(self, id: int, titel: str) -> None:
        q = f"""
        UPDATE Job SET Titel = '{titel}' WHERE Id = {id}
        """
        self.__db_service.execute_query(q)
    


    ###
    ### ADRESSEN ###
    ###

    def get_ortsname_from_plz(self, plz: str) -> str:
        q = f"""
        SELECT Name FROM Ort WHERE Plz = '{plz}'
        """
        newcur = self.__db_service.execute_query(q)
        res = newcur.fetchall()
        if len(res) == 0:
            return "Ort nicht gefunden"
        return res[0][0]

    
    def get_adresse_by_id(self, id: int) -> tuple | None:
        q = f"""
        SELECT * FROM Adresse WHERE Id = {id}
        """
        cur = self.__db_service.execute_query(q)
        res = cur.fetchall()
        if len(res) == 0:
            return None
        return res[0]
        
