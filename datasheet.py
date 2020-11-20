import csv
from datetime import datetime

with open("data collected\\attendance list.csv", 'a+', newline='') as csvfile:
    field_names = ['Date', 'Name', 'Entry Time', 'Exit Time', 'Duration', 'Status']
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
