from db import db_session
from app.models import Data

def load(data):
    db_session.bulk_insert_mappings(Data, data)
    db_session.commit()