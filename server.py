from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('index.html')

#Routing via Inheritance
@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)