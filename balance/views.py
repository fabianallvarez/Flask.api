from . import app


@app.route("/")
def inicio():
    return " Vamos a por la API"
