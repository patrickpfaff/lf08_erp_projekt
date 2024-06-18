from fastapi import FastAPI

from mitarbeiter_verwaltung import MitarbeiterVerwaltung

app = FastAPI()
mv = MitarbeiterVerwaltung()

@app.get("/get_all_mitarbeiter/")
def get_all_mitarbeiter(test: str):
    test = mv.

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)