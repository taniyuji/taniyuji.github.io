from flask import Flask,render_template 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="test", name="yuji")

@app.route("/messenger")
def messenger():
    return render_template("messenger.html")


if __name__ == "__main__":
    app.run(debug=True)