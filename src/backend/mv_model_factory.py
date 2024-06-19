from pydantic import BaseModel

class Mitarbeiter(BaseModel):
    nachname: str
    vorname: str
    geburtsdatum: str
    angestelltseit: str
    jobId: int
    abteilungId: int | None

class Job(BaseModel):
    titel: str

class Adresse(BaseModel):
    strasse: str
    hausnummer: str
    zusatz: str
    plz: str

class Abteilung(BaseModel):
    name: str
    beschreibung: str
    leiterId: int | None

def create_mitarbeiter_model(nachname:str, vorname: str, geburtsdatum: str, angestelltseit: str, jobId: int, abteilungid: int) -> Mitarbeiter:
    return Mitarbeiter(nachname=nachname,
        vorname=vorname,
        geburtsdatum=geburtsdatum,
        angestelltseit=angestelltseit,
        jobId=jobId,
        abteilungId=abteilungid)

def create_job_model(titel: str) -> Job:
    return Job(titel=titel)

def create_adresse_model(strasse: str, hausnummer: str, zusatz: str, plz: str) -> Adresse:
    return Adresse(strasse=strasse,
        hausnummer=hausnummer,
        zusatz=zusatz,
        plz=plz)

def create_abteilung_model(name: str, beschreibung: str, leiterId: int) -> Abteilung:
    return Abteilung(name=name,
        beschreibung=beschreibung,
        leiterId=leiterId)
