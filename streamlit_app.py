import streamlit as st
from snowflake.snowpark.context import get_active_session
session = get_active_session()
# sql = st.text_area("Query",value="select * from snowflake_sample_data.tpch_sf1.lineitem limit 10")
# f"select * from snowflake_sample_data.tpch_sf1.lineitem limit 20"
sql='SELECT EMP_CTR AS "Category",COUNT(*) AS "No Of Employees" FROM STREAMLIT.PUBLIC.MANPOWER GROUP BY 1'
data=session.sql(sql).collect()
if st.button("Execute Query") :
    if data:
            st.success("Query executed ")
            st.write("Result:")
            st.area_chart(data)
    else:
            st.warning("No data retrieved")
