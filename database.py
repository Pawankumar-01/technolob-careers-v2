import sqlalchemy
from sqlalchemy import create_engine,text
import os
db_connection_string = os.environ['db_connection_string']
engine = create_engine(db_connection_string)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    out=result.all()
    jobs=[dict(zip(result.keys(),row)) for row in out]
    return jobs
        
    