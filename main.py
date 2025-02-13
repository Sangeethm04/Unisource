import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for

# Load environment variables from .env file
load_dotenv()

# Loading database credentials from environment variables
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

try:
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
    # Query the new courses table (adjust the schema/table name as needed)
    cursor.execute("SELECT * FROM my_schema.courses")
    courses_fetched = cursor.fetchall()
    print("Fetched Data:", courses_fetched)

    courses_list = []
    for row in courses_fetched:
        courses_list.append({
            "CRN": row[0],
            "Course": row[1],
            "Course_Title": row[2],
            "Status": row[3],
            "Enrollment_Capacity": row[4],
            "Enrollment": row[5],
            "Waitlist_Capacity": row[6],
            "Waitlist_Enrollment": row[7],
            "Projected_Enrl": row[8],
            "Meeting_Desc": row[9],
            "Days": row[10],
            "Time": row[11],
            "BldgRoom": row[12],
            "Class_Room_Attributes": row[13],
            "Rec_Mtg_Desc": row[14],
            "Recitation_Days": row[15],
            "Recitation_Time": row[16],
            "Recitation_BldgRoom": row[17],
            "Rec_Room_Attributes": row[18],
            "Lab_Mtg_Desc": row[19],
            "Lab_Days": row[20],
            "Lab_Time": row[21],
            "Lab_BldgRoom": row[22],
            "Lab_Room_Attributes": row[23],
            "Credit_Hours": row[24],
            "Bill_Hours": row[25],
            "Primary_Instructor": row[26],
            "Primary_Instructor_LIN": row[27],
            "Secondary_Instructors": row[28],
            "Attributes": row[29],
            "Part_of_Term": row[30],
            "Schedule_Code": row[31],
            "Special_Approval": row[32],
            "Cross_List_Code": row[33],
            "Link_Identifier": row[34],
            "Link_Connector": row[35],
            "Tuition_Fees": row[36],
            "Campus_Code": row[37],
            "Instructional_Method": row[38],
            "Grade_Mode": row[39],
            "Long_Title": row[40],
            "Modalities": row[41],
            "Long_Text": row[42],
            "Short_Text": row[43]
        })

    print("Courses List:", courses_list)
    cursor.close()
    return render_template("courses.html", courses=courses_list)

@app.route("/")
def home():
    return redirect(url_for("courses"))

if __name__ == "__main__":
    app.run(debug=True)