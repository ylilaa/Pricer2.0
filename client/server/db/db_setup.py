from requests import Session
from sqlalchemy import create_engine
import urllib
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

params = urllib.parse.quote_plus(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\ylila\Desktop\Pricer 2.0\client\server\db\db.accdb;ExtendedAnsiSQL=1')

cnn_str = 'access+pyodbc:///?odbc_connect={}'.format(params)

engine = create_engine(cnn_str)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()