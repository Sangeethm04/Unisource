import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, request, render_template, redirect, url_for, flash, abort, send_from_directory

# Load environment variables from .env file
load_dotenv()

# Retrieve database credentials from environment variables
db_name = "unisourcedb"
db_user = "unisourcedbuser"
db_password = "deuce-unpainted-egotistic-ranting"
db_host = "ubuunisrcdev01.cse.lehigh.edu"
db_port = 5432

try:
    # Test database connection
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

finally:
    if 'connection' in locals() and connection:
        connection.close()
        print("Connection closed.")

app = Flask(__name__)
@app.route("/courses")
def courses():
    try:
        # Query the database to retrieve student data
        #result = db.session.execute(text("SELECT * FROM users"))
        #students = result.fetchall()  # Fetch all rows

        return render_template("courses.html")

    except Exception as e:
        print(f"Error fetching student data: {e}")
        abort(500, description="Error fetching data from the database.")