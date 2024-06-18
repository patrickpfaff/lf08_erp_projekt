from fastapi import FastAPI
from mv_model_factory import create_mitarbeiter_model, create_job_model, create_adresse_model, create_abteilung_model

from mitarbeiter_verwaltung import MitarbeiterVerwaltung

app = FastAPI()
mv = MitarbeiterVerwaltung()

@app.get("/get_all_abteilungen/")
def get_all_abteilungen():
    response = mv.get_all_abteilungen()
    abteilung_result = []
    for abteilung in response:
        abteilung_result.append(create_abteilung_model(name=abteilung[1], beschreibung=abteilung[2], leiterId=abteilung[3]))

    return abteilung_result

@app.post("/add_mitarbeiter/")
def add_mitarbeiter(vorname: str, nachname: str, geburtsdatum: str, angestelltseit: str, jobId: int, abteilungId: int = None):
    mv.add_mitarbeiter(vorname, nachname, geburtsdatum, angestelltseit, jobId, abteilungId)

@app.post("/add_abteilung/")
def add_abteilung(beschreibung: str, name: str, leiterId: int = None, custom_id: int = None):
    mv.add_abteilung(beschreibung, name, leiterId, custom_id)

@app.get("/get_all_mitarbeiter/")
def get_all_mitarbeiter():
    response = mv.get_all_mitarbeiter()
    mitarbeiter_result = []
    for mitarbeiter in response:
        mitarbeiter_result.append(create_mitarbeiter_model(nachname=mitarbeiter[2], vorname=mitarbeiter[1], geburtsdatum=mitarbeiter[3], angestelltseit=mitarbeiter[4], jobId=mitarbeiter[5], abteilungid=mitarbeiter[6]))

    return mitarbeiter_result





if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)