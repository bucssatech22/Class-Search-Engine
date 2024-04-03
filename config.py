import mysql.connector
def mydb():
    """
        Provide connection to the MySQL database.
    """
    return mysql.connector.connect(
        host = "application-portal-test.cl30flcyvsqv.us-east-1.rds.amazonaws.com",
        user = "admin",
        password = "testapplicationportal",
        database = "test_1"
    )

# alternative usage
DB_CONFIG = {
    'host': 'application-portal-test.cl30flcyvsqv.us-east-1.rds.amazonaws.com',
    'user': 'admin',
    'password': 'testapplicationportal',
    'database': 'test_1'
}