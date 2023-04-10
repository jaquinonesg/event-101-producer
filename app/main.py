from fastapi import FastAPI
from mangum import Mangum

app = FastAPI(title='event-101-registry ')

@app.get("/",  tags=["Endpoint"])
async def main_endpoint_test():
    return {"message": "Welcome to event-101-registry"}

@app.get("/health")
async def health_check():
    return {"message": "It's alive"}

handler = Mangum(app=app)