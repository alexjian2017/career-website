import os
from sqlalchemy import create_engine, text
import pymysql

db_connection_str = os.environ['db_connection_str']
engine = create_engine(
  db_connection_str,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result:
      jobs.append(row._asdict())
  return jobs

def job_detail_from_db(id:int):
  with engine.connect() as conn:
    result = conn.execute(
      text(f"select * from jobs where id = {id}"))
    if not result:
      return None
    for row in result:
      return row._asdict()

def application_to_db(id, data):
  query = f"insert into applications (job_id,full_name,email,education,work_experience,resume_url) values ({id},'{data['name']}','{data['email']}','{data['education']}','{data['work_experience']}','{data['resume_url']}')"
  try:
    with engine.connect() as conn:    
      conn.execute(text(query))
    return 1
  except pymysql.MySQLError as err:
    print(type(err), err)
    return 0
    

