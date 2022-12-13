'''Databricks Connect CLI'''
import os
from databricks import sql


class Connector():
    '''Connect to Databricks and run a query'''
    def __init__(self):
        self.server_hostname = os.getenv("DATABRICKS_SERVER_HOSTNAME")
        self.http_path = os.getenv("DATABRICKS_HTTP_PATH")
        self.access_token = os.getenv("DATABRICKS_TOKEN")

    def querydb(self, query):
        '''Connect to Databricks and run a query'''
        with sql.connect(
            server_hostname=self.server_hostname,
            http_path=self.http_path,
            access_token=self.access_token,
        ) as connection:

            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()

            for row in result:
                print(row)
        return result
