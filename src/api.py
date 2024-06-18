from fastapi import FastAPI
from mv_model_factory import Abteilung, create_mitarbeiter_model, create_job_model, create_adresse_model, create_abteilung_model

from mitarbeiter_verwaltung import MitarbeiterVerwaltung

app = FastAPI()
mv = MitarbeiterVerwaltung()

### Abteilungen ###
@app.get("/get_all_abteilungen/", response_model=list[Abteilung])
def get_all_abteilungen():
    response = mv.get_all_abteilungen()
    abteilung_result = []
    for abteilung in response:
        abteilung_result.append(create_abteilung_model(name=abteilung[1], beschreibung=abteilung[2], leiterId=abteilung[3]))

    return abteilung_result

@app.post("/add_abteilung/")
def add_abteilung(beschreibung: str, name: str, leiterId: int = None, custom_id: int = None):
    mv.add_abteilung(beschreibung, name, leiterId, custom_id)

@app.delete("/delete_abteilung/")
def delete_abteilung(id: int):
    mv.delete_abteilung(id)


### Mitarbeiter ###
@app.get("/get_all_mitarbeiter/")
def get_all_mitarbeiter():
    response = mv.get_all_mitarbeiter()
    mitarbeiter_result = []
    for mitarbeiter in response:
        mitarbeiter_result.append(create_mitarbeiter_model(nachname=mitarbeiter[2], vorname=mitarbeiter[1], geburtsdatum=mitarbeiter[3], angestelltseit=mitarbeiter[4], jobId=mitarbeiter[5], abteilungid=mitarbeiter[6]))

    return mitarbeiter_result

@app.get("/get_mitarbeiter_by_id/")
def get_mitarbeiter_by_id(id: int):
    response = mv.get_mitarbeiter_by_id(id)
    return create_mitarbeiter_model(nachname=response[2], vorname=response[1], geburtsdatum=response[3], angestelltseit=response[4], jobId=response[5], abteilungid=response[6])

@app.get("/get_mitarbeiter_by_name/")
def get_mitarbeiter_by_name(vorname: str, nachname: str):
    response = mv.get_mitarbeiter_by_name(vorname, nachname)
    mitarbeiter_result = []
    for mitarbeiter in response:
        mitarbeiter_result.append(create_mitarbeiter_model(nachname=mitarbeiter[2], vorname=mitarbeiter[1], geburtsdatum=mitarbeiter[3], angestelltseit=mitarbeiter[4], jobId=mitarbeiter[5], abteilungid=mitarbeiter[6]))

    return mitarbeiter_result

@app.post("/add_mitarbeiter/")
def add_mitarbeiter(vorname: str, nachname: str, geburtsdatum: str, angestelltseit: str, jobId: int, abteilungId: int = None):
    mv.add_mitarbeiter(vorname, nachname, geburtsdatum, angestelltseit, jobId, abteilungId)

@app.delete("/delete_mitarbeiter/")
def delete_mitarbeiter(id: int):
    mv.delete_mitarbeiter(id)

### Jobs ###
@app.get("/get_all_jobs/")
def get_all_jobs():
    response = mv.get_all_jobs()
    job_result = []
    for job in response:
        job_result.append(create_job_model(titel=job[1]))

    return job_result

@app.post("/add_job/")
def add_job(titel: str):
    mv.add_job(titel)

@app.delete("/delete_job/")
def delete_job(id: int):
    mv.delete_job(id)


### Adressen ###
@app.get("/get_all_adressen/")
def get_all_adressen():
    response = mv.get_all_adressen()
    adresse_result = []
    for adresse in response:
        adresse_result.append(create_adresse_model(strasse=adresse[1], hausnummer=adresse[2], zusatz=adresse[3], plz=adresse[4]))

    return adresse_result

@app.post("/add_adresse/")
def add_adresse(strasse: str, hausnummer: str, zusatz: str, plz: str):
    mv.add_adresse(strasse, hausnummer, zusatz, plz)

@app.delete("/delete_adresse/")
def delete_adresse(id: int):
    mv.delete_adresse(id)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)