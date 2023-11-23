import streamlit as st
import snowflake.connector
import pandas as pd
import numpy
st.title("Snowflake Streamlit App")
default_snowflake_account='on89866.central-india.azure'
default_snowflake_user='LTI10688009'
default_snowflake_password='Sunnrahahai@123'
default_snowflake_database='ACCOUNT360'
default_snowflake_schema='ACC360_DATALAKE'
default_snowflake_warehouse='ACC360_DEV_DE_WH'
def execute_snowflake_query(query,user,password,account,warehouse,
database,schema):
    connection=snowflake.connector.connect(
            user=user,
            password=password,
            account=account,
            warehouse=warehouse,
            database=database,
            schema=schema,query=query
    )
    cursor=connection.cursor()
    cursor.execute(query)
    result=cursor.fetchall()
    connection.close()
    return cursor,result


def main():

    snowflake_account=default_snowflake_account
    snowflake_user=default_snowflake_user
    snowflake_password=default_snowflake_password
    snowflake_database=default_snowflake_database
    snowflake_schema=default_snowflake_schema
    snowflake_warehouse=default_snowflake_warehouse
    query='SELECT * FROM MANPOWER_TGT WHERE EXDATE=CURRENT_DATE() LIMIT 5'
    if st.button("Execure Query"):
        cursor,result=execute_snowflake_query(
            query,
            snowflake_user,
            snowflake_password,
            snowflake_account,
            snowflake_warehouse,
            snowflake_database,
            snowflake_schema
        )
        if result:
            st.success("Query executed ")
            st.write("Result:")
            df=pd.DataFrame(result,columns=[desc[1] for desc in cursor.description])
            st.dataframe(df)
        else:
            st.warning("No data retrieved")    
if __name__=="__main__":
    main()
