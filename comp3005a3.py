import psycopg2
from psycopg2 import Error

dbname = "a3"
user = "postgres"
password = "comp3005"
host = "localhost"
port = "5432"

# Function to establish a database connection
def connect():
    try:
        connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        return connection
    except Error as e:
        print("Error while connecting to PostgreSQL:", e)
        return None

# Function to retrieve and display all records from the students table
def getAllStudents():
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        for student in students:
            print(student)
    except Error as e:
        print("Error while retrieving students:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()

# Function to insert a new student record into the students table
def addStudent(first_name, last_name, email, enrollment_date):
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
            (first_name, last_name, email, enrollment_date)
        )
        connection.commit()
        print("Student added successfully")
    except Error as e:
        print("Error while adding student:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()

# Function to update the email address for a student with the specified student_id
def updateStudentEmail(student_id, new_email):
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE students SET email = %s WHERE student_id = %s",
            (new_email, student_id)
        )
        connection.commit()
        print("Email updated successfully")
    except Error as e:
        print("Error while updating email:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()

# Function to delete the record of the student with the specified student_id
def deleteStudent(student_id):
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute(
            "DELETE FROM students WHERE student_id = %s",
            (student_id,)
        )
        connection.commit()
        print("Student deleted successfully")
    except Error as e:
        print("Error while deleting student:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()


# getAllStudents()
# addStudent("LeBron", "James", "lebron.james@example.com", "2024-03-18")
# updateStudentEmail(7, "updated_email@example.com")
# deleteStudent(6)