from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return{
        "hi welcome fastapi learner",
        "this example to fetch the data"
    }