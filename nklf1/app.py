# coding: utf-8
from flask import Flask, render_template, redirect
import pathlib
import os
from dotenv import load_dotenv

from forms import KultivaceForm, BilanceForm, LaborForm, SonoForm
from labor import doLabor
from kultivace import doKultivace
from bilance import doBilance

load_dotenv()
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
directory = pathlib.Path(os.path.dirname(__file__))

#######
# APP #
#######


@app.route("/", methods=["POST", "GET"])
def index() -> None:
    return redirect("/kultivace")


@app.route("/kultivace", methods=["POST", "GET"])
def kultivace() -> None:
    vysledky = ""

    form = KultivaceForm()
    txt = form.text.data
    if txt:
        vysledky = doKultivace(txt)
    return render_template("kultivace.html", form=form, vysledky=vysledky)


@app.route("/bilance", methods=["POST", "GET"])
def bilance() -> None:
    vysledky = [{"p": 0, "v": 0, "c": 0}]
    summa = {"p": 0, "v": 0, "c": 0}

    form = BilanceForm()
    txt = form.text.data
    spli = form.spli.data
    reg = form.reg.data
    temp = form.temp.data
    dat = form.dat.data

    if txt:
        vysledky = doBilance(txt, spli, reg, temp, dat)
        summa = {
            "p": sum([vysledek["p"] for vysledek in vysledky]),
            "v": sum([vysledek["v"] for vysledek in vysledky]),
            "c": sum([vysledek["c"] for vysledek in vysledky]),
        }
    return render_template("bilance.html", form=form, vysledky=vysledky, summa=summa)


@app.route("/labor", methods=["POST", "GET"])
def labor() -> None:
    vysledky = ""

    form = LaborForm()
    txt = form.text.data
    if txt:
        vysledky = doLabor(txt)
    return render_template("labor.html", form=form, vysledky=vysledky)


@app.route("/echo", methods=["GET"])
def echo() -> None:
    return render_template("echo.html")


@app.route("/ventilace", methods=["GET"])
def ventilace() -> None:
    return render_template("ventilace.html")


@app.route("/sono", methods=["POST", "GET"])
def sono() -> None:
    form = SonoForm()
    return render_template("sono.html", form=form)


if __name__ == "__main__":
     app.run(debug=True)
    # app.run(debug=False)
    # app.run(host='0.0.0.0', port='80', debug=True)
    # app.run(host='0.0.0.0', port='8080', debug=True)
    #app.run(host="0.0.0.0", port="80", debug=False)
