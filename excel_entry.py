import csv
from datetime import datetime


def make_attendance_entry(name):
    with open('data collected\\attendance list.csv', 'r+') as FILE:
        all_lines = FILE.readlines()
        attendance_list = []
        for line in all_lines:
            entry = line.split(',')
            attendance_list.append(entry[0])
        if name not in attendance_list:
            now = datetime.now()
            dt_string = now.strftime('%d/%b/%Y , %H:%M:%S')
            FILE.writelines(f'\n{name},{dt_string}')
