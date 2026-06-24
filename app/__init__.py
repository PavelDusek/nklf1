# coding: utf-8
"""
A flask web app to make life of a neurohospitalist easier.
"""

import os

from flask import Flask, render_template, redirect
from dotenv import load_dotenv, find_dotenv

from app.forms import KultivaceForm, BilanceForm, LaborForm, SonoForm
from app.labor import doLabor
from app.kultivace import doKultivace
from app.bilance import doBilance


def create_app():
    """
        A flask web application factory. Creates the Flask instance.
    """

    load_dotenv(find_dotenv())
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    @app.route("/", methods=["POST", "GET"])
    def index():
        return redirect("/kultivace")

    @app.route("/kultivace", methods=["POST", "GET"])
    def kultivace() -> str:
        vysledky = ""

        form = KultivaceForm()
        txt = form.text.data
        if txt:
            vysledky = doKultivace(txt)
        return render_template("kultivace.html", form=form, vysledky=vysledky)

    @app.route("/risk", methods=["GET"])
    def risk() -> str:
        return render_template("risk.html")

    @app.route("/bilance", methods=["POST", "GET"])
    def bilance() -> str:
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
                "p": sum((vysledek["p"] for vysledek in vysledky)),
                "v": sum((vysledek["v"] for vysledek in vysledky)),
                "c": sum((vysledek["c"] for vysledek in vysledky)),
            }
        return render_template(
            "bilance.html", form=form, vysledky=vysledky, summa=summa
        )

    @app.route("/labor", methods=["POST", "GET"])
    def labor() -> str:
        vysledky = ""

        form = LaborForm()
        txt = form.text.data
        if txt:
            vysledky = doLabor(txt)
        return render_template("labor.html", form=form, vysledky=vysledky)

    @app.route("/echo", methods=["GET"])
    def echo() -> str:
        return render_template("echo.html")

    @app.route("/ventilace", methods=["GET"])
    def ventilace() -> str:
        return render_template("ventilace.html")

    @app.route("/sono", methods=["POST", "GET"])
    def sono() -> str:
        form = SonoForm()
        return render_template("sono.html", form=form)

    # from .labor import labor
    # from .bilance import bilance
    # from .kultivace import kultivace

    return app


if __name__ == "__main__":
    app_instance = create_app()
    app_instance.run(debug=True)
    # app.run(debug=False)
    # app.run(host='0.0.0.0', port='80', debug=True)
    # app.run(host='0.0.0.0', port='8080', debug=True)
    # app.run(host="0.0.0.0", port="80", debug=False)
