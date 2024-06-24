from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mv_model_factory import Abteilung, Adresse, Job, Mitarbeiter, create_mitarbeiter_model, create_job_model, create_adresse_model, create_abteilung_model

from mitarbeiter_verwaltung import MitarbeiterVerwaltung

app = FastAPI(title="Mitarbeiterverwaltung API", description="API zum Verwalten von Mitarbeitern", version="0.1")
mv = MitarbeiterVerwaltung()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

### Test ###
@app.get("/test/", name="test-endpoint", tags=["test"])
def test():
    return {"message": "API is running"}

### Abteilungen ###
@app.get("/get_all_abteilungen/", response_model=list[Abteilung], name="get-all-abteilungen", tags=["abteilungen"])
def get_all_abteilungen():
    response = mv.get_all_abteilungen()
    abteilung_result = []
    for abteilung in response:
        abteilung_result.append(create_abteilung_model(name=abteilung[1], beschreibung=abteilung[2], leiterId=abteilung[3], id=abteilung[0]))

    return abteilung_result

@app.post("/add_abteilung/", name="add-abteilung", tags=["abteilungen"])
def add_abteilung(beschreibung: str, name: str, leiterId: int = None, custom_id: int = None):
    mv.add_abteilung(beschreibung, name, leiterId, custom_id)

@app.delete("/delete_abteilung/", name="delete-abteilung", tags=["abteilungen"])
def delete_abteilung(id: int):
    mv.delete_abteilung(id)

@app.get("/get_abteilung_by_id/", name="get-abteilung-by-id", response_model=Abteilung, tags=["abteilungen"])
def get_abteilung_by_id(id: int):
    response = mv.get_abteilung_by_id(id)
    return create_abteilung_model(name=response[1], beschreibung=response[2], leiterId=response[3], id=response[0])

@app.post("/update_abteilung/", name="update-abteilung", tags=["abteilungen"])
def update_abteilung(id: int, beschreibung: str, name: str, leiterId: int = None):
    mv.update_abteilung(id, beschreibung, name, leiterId)


### Mitarbeiter ###
@app.get("/get_all_mitarbeiter/", response_model=list[Mitarbeiter] , name="get-all-mitarbeiter", tags=["mitarbeiter"])
def get_all_mitarbeiter():
    response = mv.get_all_mitarbeiter()
    mitarbeiter_result = []
    for mitarbeiter in response:
        print(mitarbeiter)
        m_temp = create_mitarbeiter_model(nachname=mitarbeiter[2], vorname=mitarbeiter[1], geburtsdatum=mitarbeiter[3], angestelltseit=mitarbeiter[4], jobId=mitarbeiter[5], adresseId=mitarbeiter[6], abteilungid=mitarbeiter[7], id=mitarbeiter[0])
        mitarbeiter_result.append(m_temp)

    return mitarbeiter_result

@app.get("/get_mitarbeiter_by_id/", response_model=Mitarbeiter, name="get-mitarbeiter-by-id", tags=["mitarbeiter"])
def get_mitarbeiter_by_id(id: int):
    response = mv.get_mitarbeiter_by_id(id)
    return create_mitarbeiter_model(nachname=response[2], vorname=response[1], geburtsdatum=response[3], angestelltseit=response[4], jobId=response[5], abteilungid=response[7], adresseId=response[6], id=response[0])

@app.get("/get_mitarbeiter_by_name/", name="get-mitarbeiter-by-name", response_model=list[Mitarbeiter], tags=["mitarbeiter"])
def get_mitarbeiter_by_name(vorname: str, nachname: str):
    response = mv.get_mitarbeiter_by_name(vorname, nachname)
    mitarbeiter_result = []
    for mitarbeiter in response:
        mitarbeiter_result.append(create_mitarbeiter_model(nachname=mitarbeiter[2], vorname=mitarbeiter[1], geburtsdatum=mitarbeiter[3], angestelltseit=mitarbeiter[4], jobId=mitarbeiter[5], abteilungid=mitarbeiter[6]))

    return mitarbeiter_result

@app.post("/update_mitarbeiter/", name="update-mitarbeiter", tags=["mitarbeiter"])
def update_mitarbeiter(id: int, vorname: str, nachname: str, geburtsdatum: str, angestelltseit: str, jobId: int, abteilungId: int, strasse: str = None, hausnummer: str = None, zusatz: str = None, plz: str = None):
    mv.update_mitarbeiter(id, vorname, nachname, geburtsdatum, angestelltseit, jobId, abteilungId, strasse, hausnummer, zusatz, plz)


@app.post("/add_mitarbeiter/", name="add-mitarbeiter", tags=["mitarbeiter"])
def add_mitarbeiter(vorname: str, nachname: str, geburtsdatum: str, angestelltseit: str, jobId: int, abteilungId: int, strasse: str = None, hausnummer: str = None, zusatz: str = None, plz: str = None):
    mv.add_mitarbeiter(vorname, nachname, geburtsdatum, angestelltseit, jobId, abteilungId, strasse, hausnummer, zusatz, plz)

@app.delete("/delete_mitarbeiter/", name="delete-mitarbeiter", tags=["mitarbeiter"])
def delete_mitarbeiter(id: int):
    mv.delete_mitarbeiter(id)

### Jobs ###
@app.get("/get_all_jobs/", name="get-all-jobs", response_model=list[Job], tags=["jobs"])
def get_all_jobs():
    response = mv.get_all_jobs()
    job_result = []
    for job in response:
        job_result.append(create_job_model(id=job[0], titel=job[1]))

    return job_result

@app.post("/add_job/", name="add-job", tags=["jobs"])
def add_job(titel: str):
    mv.add_job(titel)

@app.delete("/delete_job/", name="delete-job", tags=["jobs"])
def delete_job(id: int):
    mv.delete_job(id)

@app.get("/get_job_by_id/", name="get-job-by-id", response_model=Job, tags=["jobs"])
def get_job_by_id(id: int):
    response = mv.get_job_by_id(id)
    if response is not None:
        return create_job_model(id=response[0], titel=response[1])
    return None
    
    


### Adressen ###
@app.get("/get_all_adressen/", name="get-all-adressen", response_model=list[Adresse], tags=["adressen"])
def get_all_adressen():
    response = mv.get_all_adressen()
    adresse_result = []
    for adresse in response:
        adresse_result.append(create_adresse_model(strasse=adresse[1], hausnummer=adresse[2], zusatz=adresse[3], plz=adresse[4]))

    return adresse_result

@app.post("/add_adresse/", name="add-adresse", tags=["adressen"])
def add_adresse(strasse: str, hausnummer: str, zusatz: str, plz: str):
    mv.add_adresse(strasse, hausnummer, zusatz, plz)

@app.delete("/delete_adresse/", name="delete-adresse", tags=["adressen"])
def delete_adresse(id: int):
    mv.delete_adresse(id)

@app.get("/get_adresse_by_id/", name="get-adresse-by-id", response_model=Adresse, tags=["adressen"])
def get_adresse_by_id(id: int):
    response = mv.get_adresse_by_id(id)
    return create_adresse_model(id=response[0],strasse=response[1], hausnummer=response[2], zusatz=response[3], plz=response[4])

@app.get("/get_ortsname_from_plz/", name="get-ortsname-from-plz", response_model=str, tags=["adressen"])
def get_ortsname_from_plz(plz: str):
    return mv.get_ortsname_from_plz(plz)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)