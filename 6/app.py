from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
import json

app = Flask(__name__)
CORS(app)

app.config["MYSQL_HOST"] = "db"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "test"
app.config["MYSQL_DB"] = "myDB"


def create_tables():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute(
            """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE
        )
        """
        )
        mysql.connection.commit()
        cur.close()


mysql = MySQL(app)


@app.route("/")
def home():
    return jsonify({"message": "Flask API connected to MySQL!"})


@app.route("/add_weight_id", methods=["POST"])
def add_user():
    data = request.json
    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "Missing name or email"}), 400

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))

    mysql.connection.commit()
    cur.close()

    resp = jsonify(message="Data added successfully!")
    resp.status_code = 200
    return resp


if __name__ == "__main__":
    create_tables()
    app.run(host="0.0.0.0", port=8080, debug=True)
