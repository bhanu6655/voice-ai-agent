import sqlite3

conn = sqlite3.connect("appointments.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT,
    doctor_name TEXT,
    appointment_date TEXT,
    status TEXT
)
""")

conn.commit()

def book_appointment(patient, doctor, date):

    cursor.execute("""
    INSERT INTO appointments
    (patient_name, doctor_name, appointment_date, status)
    VALUES (?, ?, ?, ?)
    """, (patient, doctor, date, "Booked"))

    conn.commit()

def get_appointments():

    cursor.execute("SELECT * FROM appointments")

    return cursor.fetchall()