import pyrebase

config = {
    "apiKey" : "AIzaSyB2Wkz-gi-dOMCS3GmrrVatCTtZQY8iSL4",
    "authDomain": "python-demo-96782.firebaseapp.com",
    "databaseURL": "https://python-demo-96782.firebaseio.com",
    "storageBucket": "python-demo-96782.appspot.com",
}
connection = pyrebase.initialize_app(config)
firebase = connection.database()

def data_add(name, id, course, phone, address):
    new_student_record = {
        'name' : name,
        'id' : id,
        'course' : course,
        'phone' : phone,
        'address' : address
    }

    firebase.child("StudentsManagement").child("Student").push(data=new_student_record)
    print("New value inserted successfully.")


def data_ret():
    students_record = firebase.child("StudentsManagement").child("Student").get()
    return students_record