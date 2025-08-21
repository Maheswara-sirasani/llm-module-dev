from fastapi import FastAPI

app=FastAPI()

@app.get("/service")
def service():
    return("vehical for services")

