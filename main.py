import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, request, render_template, redirect, url_for, flash, abort, send_from_directory

# Load environment variables from .env file
load_dotenv()


# loading database credentials from environment variables
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

try:
    # adding db connection
    print(f"DB_HOST: {db_host}")
    print(f"DB_PORT: {db_port}")
    print(f"DB_NAME: {db_name}")
    print(f"DB_USER: {db_user}")
    print(f"DB_PASSWORD: {db_password}")
    connection = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    )
    
    print("Connection to the database was successful!")

except Exception as e:
    print("Failed to connect to the database.")
    print(f"Error: {e}")


app = Flask(__name__)
@app.route("/courses")
def courses():
    print("Courses route accessed.")

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM my_schema.coursesNew")
    coursesfetched = cursor.fetchall()

    print("Fetched Data:", coursesfetched)  # Debugging

    courses_list = []
    for row in coursesfetched:
        courses_list.append({
            "code": row[1],  # Course code
            "name": row[2],  # Course name
            "schedule": row[3],  # Course schedule
            "professor": row[4],  # Professor
            "description": row[5],  # Course description
            "prerequisites": row[6],  # Prerequisites
            "semester": row[7],  # Semester (e.g., Summer2024)
            "session_type": row[8]  # Session Type (e.g., Full, SessionI, SessionII)
        })

    print("Corrected Courses List:", courses_list)  # Debugging

    cursor.close()
    return render_template("courses.html", courses=courses_list)
@app.route("/")
def home():
    return redirect(url_for("courses"))

if __name__ == "__main__":
    app.run(debug=True)