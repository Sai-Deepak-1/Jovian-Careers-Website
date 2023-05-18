from sqlalchemy import create_engine, text

db_url = "mysql+pymysql://ujzvsm6kx20vl2l45kt9:pscale_pw_ixfyATzrkRlmonBU57Ao0yBCkbrHYRVqRpbTlKwIZYZ@aws.connect.psdb.cloud/careers?charset=utf8mb4"

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
