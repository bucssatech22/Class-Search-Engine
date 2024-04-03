import json
import mysql.connector
from config import DB_CONFIG

def create_database():
    """
        create MySQL database
    """
    db = mysql.connector.connect(**DB_CONFIG)

    cursor = db.cursor()

    with open("spring2024.json", 'r') as file:
        courses_data = json.load(file)
    for course in courses_data:
        credit = course.get('credit', 0)
        prereq = course.get('prereq', None)
        hub = course.get('hub', None)
        sql = "INSERT INTO courses_db (name, code, description, credit, prereq, hub) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (course['name'], course['code'], course['description'], credit, prereq, hub)
        cursor.execute(sql, val)

    db.commit()
    print(f"Database created or already exists.")

    cursor.close()
    db.close()

if __name__ == "__main__":
    create_database()