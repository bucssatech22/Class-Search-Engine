import json
import mysql.connector

db = mysql.connector.connect(
    host = "application-portal-test.cl30flcyvsqv.us-east-1.rds.amazonaws.com",
    user = "admin",
    password = "testapplicationportal",
    database = "test_1"
)

cursor = db.cursor()
with open('spring2024.json', 'r') as file:
    data = json.load(file)

for item in data:
    name = item.get('name')
    code = item.get('code')
    description = item.get('description')
    hub = item.get('hub')     
    credit = item.get('credit')
    prereq = item.get('prereq') 
    real_code=code[4:]
    college=code[:3]
    query = "INSERT INTO courses_cleverteam (college, code, name, description, hub, credit, prereq) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (college, real_code, name, description, hub, credit, prereq)
    cursor.execute(query, values)

db.commit()
cursor.close()
db.close()
