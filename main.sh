echo "In entrypoint.sh >>>>>>>>>>>>"
virtualenv -p python snyk
source snyk/bin/activate
#python -m venv Package-env
#Package-env\Scripts\activate.csh
#pip install -r requirements.txt

pip install pandas
pip install snowflake-connector-python
python streamlit_app.py