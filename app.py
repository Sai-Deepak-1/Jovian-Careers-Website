from flask import Flask , render_template

app = Flask(__name__)


# route is part of url after the domain name
# ex : in goggle.com/search , "/search" is route
# the below is aka empty route that means the it is the home page
@app.route("/")
def hello_world():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
