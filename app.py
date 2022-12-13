'''Webapp'''
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
import uvicorn
import dblib.connector as db

app = FastAPI()

def my_schema():
    '''Schema'''
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

#write api to get data from database
@app.get("/getMaxTranAmount")
async def getMaxTranAmount():
    '''Get Max TranAmount'''
    conn=db.Connector()
    return conn.querydb('SELECT MAX(Tran_Amount) FROM hive_metastore.default.daily_train_cleaned_csv limit 1')

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")