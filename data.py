import csv
import psycopg2
import os


DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USERNAME")
DB_PASS = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")
CSV_FILE_PATH = "courses.csv" 

def main():

    columns = [
        "crn",
        "course",
        "course_title",
        "status",
        "enrollment_capacity",
        "enrollment",
        "waitlist_capacity",
        "waitlist_enrollment",
        "projected_enrl",
        "meeting_desc",
        "days",
        "time",
        "bldgroom",
        "class_room_attributes",
        "rec_mtg_desc",
        "recitation_days",
        "recitation_time",
        "recitation_bldgroom",
        "rec_room_attributes",
        "lab_mtg_desc",
        "lab_days",
        "lab_time",
        "lab_bldgroom",
        "lab_room_attributes",
        "credit_hours",
        "bill_hours",
        "primary_instructor",
        "primary_instructor_lin",
        "secondary_instructors",
        "attributes",
        "part_of_term",
        "schedule_code",
        "special_approval",
        "cross_list_code",
        "link_identifier",
        "link_connector",
        "tuition_fees",
        "campus_code",
        "instructional_method",
        "grade_mode",
        "long_title",
        "modalities",
        "long_text",
        "short_text"
    ]

   
    insert_query = f"""
        INSERT INTO my_schema.courses ({", ".join(columns)})
        VALUES ({", ".join(["%s"] * len(columns))})
        ON CONFLICT (crn) DO NOTHING;
    """

    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            port=DB_PORT  
        )
        cursor = conn.cursor()

        # Open CSV file and read each row
        with open(CSV_FILE_PATH, mode="r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                # Normalize the CSV header keys: convert to lowercase and replace spaces with underscores.
                normalized_row = {key.lower().replace(" ", "_"): value for key, value in row.items()}
                # Debug: print the normalized row to verify
                print("Normalized row:", normalized_row)

                # Build  list of values in   the correct column order
                values = []
                for col in columns:
                    val = normalized_row.get(col, "").strip()  #Get the value for the key
                    if val == "":
                        val = None  # Treat empty string as NULL
                    else:
                        #Convert certain fields to integers if appropriate.
                        if col in [
                            "crn",
                            "enrollment_capacity",
                            "enrollment",
                            "waitlist_capacity",
                            "waitlist_enrollment",
                            "projected_enrl",
                            "credit_hours",
                            "bill_hours"
                        ]:
                            try:
                                val = int(val)
                            except ValueError:
                                # If conversion fail do the loggingg it or set to None
                                val = None
                    values.append(val)

                # Execute the insert for the current row
                cursor.execute(insert_query, values)

        
        conn.commit()
        print("Data inserted successfully!")

    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        # Close cuser  asnd connecti
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    main()