from flask import Flask, render_template
app = Flask(_name_)
@app.route("/home")
def homepage():
	return render_template("home.html", title="HOME PAGE")
@app.route("/cse")
def cse():
	return render_template("cse.html", title="cse")
@app.route("/ece")
def ece():
	return render_template("ece.html", title="ece")
@app.route("/eee")
def eee():
	return render_template("eee.html", title="eee")
if _name_ == "_main_":
	app.run(debug=True)