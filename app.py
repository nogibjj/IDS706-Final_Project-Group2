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
async def get_max_tran_amount():
    '''Get Max TranAmount'''
    conn=db.Connector()
    return conn.querydb('SELECT MAX(Tran_Amount) FROM hive_metastore.default.daily_train_cleaned_csv limit 1')

#write the date with max transaction amount
@app.get("/getMaxTranAmountDate")
async def get_max_tran_amount_date():
    '''Get Max TranAmount Date'''
    conn=db.Connector()
    return conn.querydb('SELECT Data FROM hive_metastore.default.daily_train_cleaned_csv where Tran_Amount = (SELECT MAX(Tran_Amount) FROM hive_metastore.default.daily_train_cleaned_csv limit 1)')

#write the date with max fraud  amount
@app.get("/getMaxFraudAmount")
async def get_max_fraud_amount():
    '''Get Max Fraud Amount'''
    conn=db.Connector()
    return conn.querydb('SELECT MAX(Fraud_Amount) FROM hive_metastore.default.daily_train_cleaned_csv limit 1')
    
#write the date with max fraud count
@app.get("/getMaxFraudCountDate")
async def get_max_fraud_count_date():
    '''Get Max Fraud Count Date'''
    conn=db.Connector()
    return conn.querydb('SELECT Data FROM hive_metastore.default.daily_train_cleaned_csv where Fraud_Count = (SELECT MAX(Fraud_Count) FROM hive_metastore.default.daily_train_cleaned_csv limit 1)')

#write the date with max transaction count
@app.get("/getMaxTranCountDate")
async def get_max_tran_count_date():
    '''Get Max Tran Count Date'''
    conn=db.Connector()
    return conn.querydb('SELECT Data FROM hive_metastore.default.daily_train_cleaned_csv where Tran_Count = (SELECT MAX(Tran_Count) FROM hive_metastore.default.daily_train_cleaned_csv  limit 1)')

#write the function that returns sample dataframe
@app.get("/getSampleData")
async def get_sample_data():
    '''Get Sample Data'''
    conn=db.Connector()
    return conn.querydb('SELECT * FROM hive_metastore.default.daily_train_cleaned_csv limit 10')


#count the number of days where fraud count is 0
@app.get("/getNoFraudCount")
async def get_no_fraud_count():
    '''Get No Fraud Count Days'''
    conn=db.Connector()
    return conn.querydb('SELECT COUNT(*) FROM hive_metastore.default.daily_train_cleaned_csv where Fraud_Count = 0')

@app.get("/getFraudCount")
async def get_fraud_count():
    '''Get Fraud Count Days'''
    conn=db.Connector()
    return conn.querydb('SELECT COUNT(*) FROM hive_metastore.default.daily_train_cleaned_csv where Fraud_Count > 0')


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")