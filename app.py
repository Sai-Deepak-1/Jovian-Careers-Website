from flask import Flask, render_template

app = Flask(__name__)

Jobs = [
    {
        'id' : 1,
        'title' : 'Data Analyst',
        'location' : 'Hyderabad, India',
        'salary' : 'Rs. 15,00,000'
    },
    {
        'id' : 2,
        'title' : 'Full Stack',
        'location' : 'Kolkata, India',
        'salary' : 'Rs. 25,00,000'
    },
    {
        'id' : 3,
        'title' : 'Java Dev',
        'location' : 'Delhi, India',
        'salary' : 'Rs. 45,00,000'
    },
    {
        'id' : 4,
        'title' : 'AI Dev',
        'location' : 'New York, U.S.A',
        'salary' : '$ 1,00,000'
    }
]

# route is part of url after the domain name
# ex : in goggle.com/search , "/search" is route
# the below is aka empty route that means the it is the home page
@app.route("/")
def hello_world():
    return render_template('home.html',jobs = Jobs,company="PSD Industries")

@app.route("/api/jobs")
def job_list():
    return Flask.jsonify(Jobs)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
