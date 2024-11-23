import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, request, render_template, redirect, url_for, flash, abort, send_from_directory

# Load environment variables from .env file
load_dotenv()


# Retrieve database credentials from environment variables
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

try:
    # Test database connection
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
    try:
        #Query the database to retrieve student data
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM my_schema.courses")
        # Execute the SQL query to retrieve courses
        courses = cursor.fetchall()  # Fetch all rows from the query

        for course in courses:
            print(course)



        return render_template("courses.html", courses=courses)

    except Exception as e:
        print(f"Error fetching student data: {e}")
        abort(500, description="Error fetching data from the database.")

if __name__ == "__main__":
    app.run(debug=True)