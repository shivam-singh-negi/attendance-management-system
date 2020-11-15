# Importing pandas library
import pandas as pd
from datetime import datetime


def make_attendance_exit(date, name):
    df = pd.read_csv("data collected\\attendance list.csv")
    for row in df.itertuples():
        if getattr(row, 'Date') == date and getattr(row, 'Name') == name and getattr(row, 'Status') == "Waiting":
            now = datetime.now()
            dt_time = now.strftime('%H:%M:%S')
            startDateTime = datetime.strptime(df.loc[row.Index, 'Entry Time'], '%H:%M:%S')
            endDateTime = datetime.strptime(dt_time, '%H:%M:%S')
            diff = endDateTime - startDateTime
            df.loc[row.Index, 'Exit Time'] = dt_time
            df.loc[row.Index, 'Duration'] = diff
            df.loc[row.Index, 'Status'] = "Present"
            break
    df.to_csv('data collected\\attendance list.csv', index=False)


make_attendance_exit("13/Nov/2020", "Jensen Ackles")
make_attendance_exit("15/Nov/2020", "Shivam singh")

