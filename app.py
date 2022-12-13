'''Webapp'''
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
import dblib.dbfunctions as db
import uvicorn


app = FastAPI()

def my_schema():
    openapi_schema = get_openapi(
       title="Fraud Analysis",
       version="1.0",
       description="API Description",
       routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema
app.openapi = my_schema
@app.get("/")
async def root():
    '''Root'''
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")