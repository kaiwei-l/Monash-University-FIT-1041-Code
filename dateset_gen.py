import csv

def binary_search(target, lst, i, j):
    if i == j:
        return -1
    mid = (i + j) // 2
    if lst[mid] == target:
        return mid
    elif lst[mid] > target:
        return binary_search(target, lst, mid+1, j)
    else:
        return binary_search(target, lst, i, mid)


def mon_convertor(mon):
    if mon == "January":
        return "01"
    elif mon == "February":
        return "02"
    elif mon == "March":
        return "03"
    elif mon == "April":
        return "04"
    elif mon == "May":
        return "05"
    elif mon == "June":
        return "06"
    elif mon == "July":
        return "07"
    elif mon == "August":
        return "08"
    elif mon == "September":
        return "09"
    elif mon == "October":
        return "10"
    elif mon == "November":
        return "11"
    else:
        return "12"


def date_convertor_day(date):
    tmp = date.split()
    mon = mon_convertor(tmp[1])

    if int(tmp[0]) < 10:
        day = "0" + tmp[0]
    else:
        day = tmp[0]

    date = tmp[2] + mon + day
    return date


def date_convertor_mon(date):
    tmp = date.split()
    mon = mon_convertor(tmp[1])

    date = tmp[2] + mon
    return date


def date_convertor_year(date):
    tmp = date.split()
    date = tmp[2]
    return date

def timeline_gen_day():
    timeline = []
    for i in range(2016, 2000, -1):
        if i == 2016:
            for j in range(9, 0, -1):
                if j == 2:
                    for m in range(29, 0, -1):
                        if m < 10:
                            day = "0" + str(m)
                            mon = "02"
                            year = str(i)
                            date = year + mon + day
                            timeline.append(date)
                        else:
                            day = str(m)
                            mon = "02"
                            year = str(i)
                            date = year + mon + day
                            timeline.append(date)
                elif (j == 1) or (j == 3) or (j == 5) or (j == 7) or (j == 8) or (j == 10) or (j == 12):
                    if j < 10:
                        mon = "0" + str(j)
                    else:
                        mon = str(j)
                    for m in range(31, 0, -1):
                        if m < 10:
                            day = "0" + str(m)
                            year = str(i)
                            date = year + mon + day
                            timeline.append(date)
                        else:
                            day = str(m)
                            year = str(i)
                            date = year + mon + day
                            timeline.append(date)
                else:
                    if j < 10:
                        mon = "0" + str(j)
                    else:
                        mon = str(j)
                    for m in range(30, 0, -1):
                        if m < 10:
                            day = "0" + str(m)
                            year = str(i)
                            date = year + mon + day
                            timeline.append(date)
                        else:
                            day = str(m)
                            year = str(i)
                            date = year + mon + day
                            timeline.append(date)
        elif (i == 2004) or (i == 2008) or (i == 2012):
            for j in range(12, 0, -1):
                if j == 2:
                    for m in range(29, 0, -1):
                        if m < 10:
                            day = "0" + str(m)
                            mon = "02"
                            year = str(i)
                            date = year + mon + day
                            timeline.append(date)
                        else:
                            day = str(m)
                            mon = "02"
                            year = str(i)
                            date = year + mon + day
                            timeline.append(date)
                elif (j == 1) or (j == 3) or (j == 5) or (j == 7) or (j == 8) or (j == 10) or (j == 12):
                    if j < 10:
                        mon = "0" + str(j)
                    else:
                        mon = str(j)
                    for m in range(31, 0, -1):
                        if m < 10:
                            day = "0" + str(m)
                            year = str(i)
                            date = year + mon + day
                            timeline.append(date)
                        else:
                            day = str(m)
                            year = str(i)
                            date = year + mon + day
                            timeline.append(date)
                else:
                    if j < 10:
                        mon = "0" + str(j)
                    else:
                        mon = str(j)
                    for m in range(30, 0, -1):
                        if m < 10:
                            day = "0" + str(m)
                            year = str(i)
                            date = year + mon + day
                            timeline.append(date)
                        else:
                            day = str(m)
                            year = str(i)
                            date = year + mon + day
                            timeline.append(date)
        else:
            for j in range(12, 0, -1):
                if j == 2:
                    for m in range(28, 0, -1):
                        if m < 10:
                            day = "0" + str(m)
                            mon = "02"
                            year = str(i)
                            date = year + mon + day
                            timeline.append(date)
                        else:
                            day = str(m)
                            mon = "02"
                            year = str(i)
                            date = year + mon + day
                            timeline.append(date)
                elif (j == 1) or (j == 3) or (j == 5) or (j == 7) or (j == 8) or (j == 10) or (j == 12):
                    if j < 10:
                        mon = "0" + str(j)
                    else:
                        mon = str(j)
                    for m in range(31, 0, -1):
                        if m < 10:
                            day = "0" + str(m)
                            year = str(i)
                            date = year + mon + day
                            timeline.append(date)
                        else:
                            day = str(m)
                            year = str(i)
                            date = year + mon + day
                            timeline.append(date)
                else:
                    if j < 10:
                        mon = "0" + str(j)
                    else:
                        mon = str(j)
                    for m in range(30, 0, -1):
                        if m < 10:
                            day = "0" + str(m)
                            year = str(i)
                            date = year + mon + day
                            timeline.append(date)
                        else:
                            day = str(m)
                            year = str(i)
                            date = year + mon + day
                            timeline.append(date)

    timeline.insert(0, "Name")
    timeline.insert(0, "Class")
    with open('date_day.csv', 'a', newline='') as f:
        w = csv.writer(f)
        w.writerow(timeline)

    return timeline


def timeline_gen_mon():
    timeline = []
    for i in range(2016, 2000, -1):
        for j in range(12, 0, -1):
            if j < 10:
                mon = "0" + str(j)
                year = str(i)
                date = year + mon
                timeline.append(date)
            else:
                year = str(i)
                mon = str(j)
                date = year + mon
                timeline.append(date)

    timeline.insert(0, "Name")
    timeline.insert(0, "Class")
    with open('date_mon.csv', 'a', newline='') as f:
        w = csv.writer(f)
        w.writerow(timeline)

    return timeline


def timeline_gen_year():
    timeline = []
    for i in range(2016, 2000, -1):
        year = str(i)
        timeline.append(year)

    timeline.insert(0, "Name")
    timeline.insert(0, "Class")
    with open('date_year.csv', 'a', newline='') as f:
        w = csv.writer(f)
        w.writerow(timeline)

    return timeline


def dataset_day_gen():
    lst = []
    counter = 1
    with open('date1.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 10:
                tmp = [row[0], row[1]]

                for i in range(2, len(row)):
                    a = row[i].split(', ')
                    tmp.append(date_convertor_day(a[1]))

                lst.append(tmp)
                print(counter)
                counter += 1

    timeline_day = timeline_gen_day()

    day = []
    n = 0
    for line in lst:
        tmp = [0] * (len(timeline_day))
        tmp[0] = line[0]
        tmp[1] = line[1]
        for i in range(2, len(line)):
            index = binary_search(line[i], timeline_day, 2, len(timeline_day))
            if index != -1:
                tmp[index] += 1
        day.append(tmp)
        n += 1
        print(n)

    for line in day:
        with open('date_day.csv', 'a', newline='') as f:
            w = csv.writer(f)
            w.writerow(line)


def dataset_mon_gen():
    lst = []
    m = 1
    with open('date1.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 10:
                tmp = [row[0], row[1]]
                for i in range(2, len(row)):
                    a = row[i].split(', ')
                    tmp.append(date_convertor_mon(a[1]))

                lst.append(tmp)
                print(m)
                m += 1

    timeline_mon = timeline_gen_mon()

    day = []
    n = 1
    for line in lst:
        tmp = [0] * (len(timeline_mon))
        tmp[0] = line[0]
        tmp[1] = line[1]
        for i in range(2, len(line)):
            index = binary_search(line[i], timeline_mon, 2, len(timeline_mon))
            if index != -1:
                tmp[index] += 1
        day.append(tmp)
        print(n)
        n += 1

    for line in day:
        with open('date_mon.csv', 'a', newline='') as f:
            w = csv.writer(f)
            w.writerow(line)


def dataset_year_gen():
    lst = []
    m = 1
    with open('date1.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 10:
                tmp = [row[0], row[1]]
                for i in range(2, len(row)):
                    a = row[i].split(', ')
                    tmp.append(date_convertor_year(a[1]))

                lst.append(tmp)
                print(m)
                m += 1

    timeline_year = timeline_gen_year()

    day = []
    n = 1
    for line in lst:
        tmp = [0] * (len(timeline_year))
        tmp[0] = line[0]
        tmp[1] = line[1]
        for i in range(2, len(line)):
            index = binary_search(line[i], timeline_year, 2, len(timeline_year))
            if index != -1:
                tmp[index] += 1
        day.append(tmp)
        print(n)
        n += 1

    for line in day:
        with open('date_year.csv', 'a', newline='') as f:
            w = csv.writer(f)
            w.writerow(line)

dataset_day_gen()
dataset_mon_gen()
dataset_year_gen()
