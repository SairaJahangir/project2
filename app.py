from flask import Flask, render_template, make_response
from database import retrieve_table 


app = Flask(__name__)

# creates connection to our homepage
@app.route("/")
def homepage():
    return 'Homepage check'
    # return render_template('home.html') 

# returns connectiontion to our first plot
@app.route("/plot1")
def plot1():
    return 'Plot 1 check'
    # return render_template('plot1.html')

# returns connectiontion to our first plot
@app.route("/plot2")
def plot2():
    return 'Plot 2 check'
    # return render_template('plot2.html')

# returns connectiontion to our first plot
@app.route("/plot3")
def plot3():
    return 'Plot 3 check'
    # return render_template('plot3.html')


# REST endpoints --> Connects flask server to the database

@app.route("/table/<table_name>")
def table(table_name):
    """
    NOT SURE IF NECESSARY
    Serve a database table as CSV.
    Based on https://stackoverflow.com/a/26998089/240490
    """
    data = retrieve_table(table_name)
    si = io.StringIO()
    cw = csv.writer(si)
    cw.writerows(data)
    output = make_response(si.getvalue())
    output.headers["Content-type"] = "text/csv"
    return output

    # can also try return data or return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
