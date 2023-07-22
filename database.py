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


def load_job(id):
    with engine.connect() as con:
        res = con.execute(text("select * from jobs where id = :val"),
                          {"val": id})
        row = res.all()
        if len(row) == 0:
            return None
        else:
            return row[0]._asdict()

def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")

        conn.execute(query, {
            "job_id": job_id,
            "full_name": data['full_name'],
            "email": data['email'],
            "linkedin_url": data['linkedin_url'],
            "education": data['education'],
            "work_experience": data['work_experience'],
            "resume_url": data['resume_url']
        })
