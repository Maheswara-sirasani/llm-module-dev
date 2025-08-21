from fastapi import FastAPI

app=FastAPI(
    title="vehical rental service",
    version="0.11"
)

@app.get("/health")
async def health():
    return{"status":"ok",
           "service":"rental",
           "version":"0.11"
    }
    

