from flask import jsonify

from . import app
from .models import DBManager


RUTA = app.config.get("RUTA")

@app.route("/api/v1/movimientos/1")
def listar_movimientos():
    db = DBManager(RUTA)
    sql = "SELECT * from movimientos ORDER BY fecha, id"
    movimientos = db.consultaSQL(sql)
    return jsonify(movimientos)