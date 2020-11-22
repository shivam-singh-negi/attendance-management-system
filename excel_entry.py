import csv
from datetime import datetime

field_names = ['Date', 'Name', 'Entry Time', 'Exit Time', 'Duration', 'Status']

with open("data collected\\attendance list.csv", 'a+', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()


def make_attendance_entry(days, name):
    fields_names = ['Date', 'Name', 'Entry Time', 'Exit Time', 'Duration', 'Status']
    with open('data collected\\attendance list.csv', 'r+', newline='') as FILE:
        my_writer = csv.DictWriter(FILE, fieldnames=fields_names)
        all_lines = FILE.readlines()
        attendance_list = []

        now = datetime.now()
        dt_days = now.strftime('%d/%b/%Y')
        dt_time = now.strftime('%H:%M:%S')
        de_exit = "Waiting"
        duration = "Waiting"
        status = "Waiting"
        for line in all_lines:
            entry = line.split(',')
            attendance_list.append((entry[0], entry[1]))
        if (days, name) not in attendance_list:
            rows = {'Date': dt_days, 'Name': name, 'Entry Time': dt_time, 'Exit Time': de_exit, 'Duration': duration,
                    'Status': status}
            my_writer.writerow(rows)


