from pydantic import BaseModel

class Mitarbeiter(BaseModel):
    id: int = None
    nachname: str
    vorname: str
    geburtsdatum: str
    angestelltseit: str
    jobId: int
    abteilungId: int
    adresseId: int

class Job(BaseModel):
    id: int = None
    titel: str

class Adresse(BaseModel):
    id: int = None
    strasse: str
    hausnummer: str
    zusatz: str
    plz: str

class Abteilung(BaseModel):
    id: int = None
    name: str
    beschreibung: str
    leiterId: int | str

def create_mitarbeiter_model(nachname:str, vorname: str, geburtsdatum: str, angestelltseit: str, jobId: int, abteilungid: int, adresseId: int, id: int = None) -> Mitarbeiter:
    return Mitarbeiter(nachname=nachname,
        vorname=vorname,
        geburtsdatum=geburtsdatum,
        angestelltseit=angestelltseit,
        jobId=jobId,
        abteilungId=abteilungid,
        adresseId=adresseId,
        id=id)

def create_job_model(id: int, titel: str) -> Job:
    return Job(id=id, titel=titel)

def create_adresse_model(strasse: str, hausnummer: str, zusatz: str, plz: str, id: int) -> Adresse:
    return Adresse(strasse=strasse,
        hausnummer=hausnummer,
        zusatz=zusatz,
        plz=plz,
        id=id)

def create_abteilung_model(name: str, beschreibung: str, leiterId: int | str = None, id: int = None) -> Abteilung:
    return Abteilung(name=name,
        beschreibung=beschreibung,
        leiterId=leiterId,
        id=id)
