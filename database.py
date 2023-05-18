from sqlalchemy import create_engine, text
import os
db_url = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_url,
                       connect_args={
                           "ssl": {
                               "ssl_ca": "ca.pem",
                               "ssl_cert": "client-cert.pem",
                               "ssl_key": "client-key.pem"
                           }
                       })


def load_jobs():
    with engine.connect() as con:
        res = con.execute(text("select * from jobs"))
        jobs = []
        for row in res.all():
            jobs.append(row._asdict())
        return jobs
