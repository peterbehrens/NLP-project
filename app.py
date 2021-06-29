import flask
from flask.helpers import url_for
from crawler import Crawler
from flask import request, render_template, redirect
from model import Model

app = flask.Flask(__name__)
Crawler = Crawler()
Classifier = Model()

app.config["DEBUG"] = True


@app.route("/search/<company>")
def search(company):
    snippet = Crawler.getSnippet(company)
    sector = Classifier.predict(snippet)
    return render_template("company.html", company=company, snippet = snippet, sector = sector)

@app.route('/', methods=['POST', "GET"])
def my_form():
    if request.method == "POST":
        text = request.form['keyword']

        return redirect(url_for("search", company=text))
    else:
        text = request.args.get("keyword")
        return render_template("index.html")

 

if __name__ == '__main__':
    app.run(port=5000)
