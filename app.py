#Set up Flask
from flask import Flask, render_template
app= Flask(__name__)

#Set Routes for Flask App
@app.route("/")
def home():
    """ home page """
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=False)