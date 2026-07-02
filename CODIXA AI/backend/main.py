from fastapi import FastAPI

app = FastAPI(
    title="CODIXA AI",
    version="0.0.1",
    description="The Future of Open Source Artificial Intelligence"
)

@app.get("/")
def home():
    return {
        "project": "CODIXA AI",
        "version": "0.0.1",
        "status": "Running"
    }