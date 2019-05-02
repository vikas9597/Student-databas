
import sqlite3

connection =sqlite3.connect('student_managements.db')
print("Database opened sucessfully.")

TABLE_NAME = "student_table"
STUDENT_ID = "student_id"
STUDENT_NAME = "student_name"
STUDENT_COLLAGE = "student_collage"
STUDENT_ADDRESS = "student_address"
STUDENT_PHONE = "student_phone"

connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_ID +
                   " INTEGER PRIMARY KEY AUTOINCREMENT, " + STUDENT_NAME + " TEXT, " +
                   STUDENT_COLLAGE + " TEXT, " + STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE + " INTEGER);")
print("Table created Sucessfully")


def data_add(name, collage, id, address, phone):
    connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " + STUDENT_ID + ", " +
                       STUDENT_COLLAGE + ", " + STUDENT_ADDRESS + ", " + STUDENT_PHONE + " ) VALUES ( '" + name + "', '" +
                       id + "', '" + collage + "', '" + address + "', '" + phone + "'); ")
    connection.commit()
    print(name, collage, id, address, phone)


def data_ret():
    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
    return cursor





