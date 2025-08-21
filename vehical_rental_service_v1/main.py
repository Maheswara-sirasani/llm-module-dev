from fastapi import FastAPI

app=FastAPI(
    title="vehical rental service",
    version="0.13"
)

@app.get("/health")
def health():
    return("welcome to vehicl rental service")