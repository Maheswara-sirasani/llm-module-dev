from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def fast():
    return{
        "welcome to fastapi"
    }