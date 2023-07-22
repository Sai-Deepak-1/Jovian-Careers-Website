from flask import Flask, render_template, jsonify, request
from database import load_jobs, load_job

app = Flask(__name__)

# Jobs = [{
#     'id': 1,
#     'title': 'Data Analyst',
#     'location': 'Hyderabad, India',
#     'salary': 'Rs. 15,00,000'
# }, {
#     'id': 2,
#     'title': 'Full Stack',
#     'location': 'Kolkata, India',
#     'salary': 'Rs. 25,00,000'
# }, {
#     'id': 3,
#     'title': 'Java Dev',
#     'location': 'Delhi, India',
#     'salary': 'Rs. 45,00,000'
# }, {
#     'id': 4,
#     'title': 'AI Dev',
#     'location': 'New York, U.S.A',
#     'salary': '$ 1,00,000'
# }]


# route is part of url after the domain name
# ex : in goggle.com/search , "/search" is route
# the below is aka empty route that means the it is the home page
@app.route("/")
def hello_world():
    jobs = load_jobs()
    return render_template('home.html', jobs=jobs, company="Sai Industries")


@app.route("/jobs/<id>")
def jobid(id):
    job = load_job(id)
    # return jsonify(job)
    if not job:
        return 'Not Found', 404
    return render_template('jobfile.html', job=job, company="Sai Industries")


@app.route("/api/jobs")
def job_list():
    #jsonify is a function in flask which gives us json as an output
    jobs = load_jobs()
    return jsonify(jobs)

@app.route("/job/<id>/apply" , methods = ['post'])
def apply_to_job(id):
    data = request.form
    # u can store this in db / send an email
    return jsonify(data)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
