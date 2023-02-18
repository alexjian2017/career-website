import os
from sqlalchemy import create_engine, text


# engine = create_engine("mysql+pymysql://user:pass@some_mariadb/dbname?charset=utf8mb4")
# db_connection_str = "mysql+pymysql://svmruw22q44m9knjcmmo:pscale_pw_V4djln1UBmoYKmusswD85CoPCuC2msUNZe5iBdogiyD@ap-northeast.connect.psdb.cloud/newcareer?charset=utf8mb4"
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
