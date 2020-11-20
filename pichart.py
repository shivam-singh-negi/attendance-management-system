import csv
from matplotlib import pyplot as plt


def func(name):
    date = []
    names = []
    with open("C:\\Users\\me lenovo\\Desktop\\attendence management system\\data collected\\attendance list.csv", newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if not(row['Date'] == "Date"):
                date.append(row['Date'])
                names.append(row['Name'])
    res = []
    for i in date:
        if i not in res:
            res.append(i)
    a = len(res)
    count = 0
    for i in names:
        if i == name:
            count = count + 1
    present = (count / a) * 100
    print("Showing attendance of ", name)
    print("total Number of working days", a)
    print("Number of persents", count)
    absent = 100.00 - present
    print("total Number of absents ", a-count)
    data = [present, absent]
    att = ["Present\n"+str(count)+" Days", "Absent\n"+str(a-count)+" Days"]
    fig = plt.figure(figsize=(5, 3))
    plt.pie(data, labels=att)
    plt.show()
    return


