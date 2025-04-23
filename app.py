from flask import Flask
import pymysql
import os

app = Flask(__name__)


def get_connection():
    return pymysql.connect(
        host=os.getenv("MYSQLHOST"),
        user=os.getenv("MYSQLUSER"),
        password=os.getenv("MYSQLPASSWORD"),
        database=os.getenv("MYSQLDATABASE"),
        port=int(os.getenv("MYSQLPORT", 3306))
    )


@app.route("/")
def index():
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT '¡Conectado a MySQL en Railway!'")
        result = cursor.fetchone()
    connection.close()
    return result[0]


if __name__ == "__main__":
    app.run()
