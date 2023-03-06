import sqlalchemy as sql
from sqlalchemy import text

import pandas as pd
import glob
import time


class SQLeto:    
    def __init__(self, database: str, user: str, password: str) -> None:
        self.engine = None        
        self.database = database
        self.user = user
        self.pwd = password
        self.url = f"postgresql://{self.user}:{self.pwd}@db:5432/{self.database}"

   
    def create_engine(self) -> sql.engine.Engine:
        if (self.engine == None):
           url = self.url
           self.engine = sql.create_engine(url)              

    
    def execute_DQL(self, query: str, **kwargs) -> pd.DataFrame:  
        self.create_engine()
        connection=self.engine.connect()             
        return pd.read_sql(sql=text(query),con=connection,**kwargs)    
     
    
    def creating_tables(
        self,
        dataframe: pd.DataFrame,
        name_table: str,
        primary_key: str,
        has_fk: bool = False,
        foreign_key: str = "",
        reference_table: str = "",
    ):

        query = f"CREATE TABLE {name_table}("
        schema = self.create_type_column(data=dataframe)
        for key, value in schema.items():
            query += f"{key} {value},"
        if has_fk:
            query += f"FOREIGN KEY ({foreign_key}) REFERENCES {reference_table} ({foreign_key}),"
        query += f"PRIMARY KEY ({primary_key}));"

        return query    
    
  
    def upload_dataframe_to_db(self, table_name: str, dataframe: pd.DataFrame, if_exists_: str) -> None:
        """
        This method receives a dataframe name, and dataframe, to upload it to db.
        """    
        self.create_engine()    
        print(f"Saving table {table_name}")
        dataframe.to_sql(table_name, self.engine, if_exists=if_exists_, index=False)
        print(f"Table {table_name} saved!")

