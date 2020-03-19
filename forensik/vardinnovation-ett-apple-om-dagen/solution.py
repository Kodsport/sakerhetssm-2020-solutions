#!/bin/env python3
from datetime import datetime
import sys

f = open("journal_access.csv")
f.readline()

text = f.read()

d = {}
for line in text.strip().split("\n"):
    [a, b, c] = line.split(",")

    if a not in d:
        d[a] = {"t": [], "z": []}

    d[a]["t"].append(b)
    d[a]["z"].append(c)

'''
# Look at earliest and latest access for each doctor.
for (k, v) in d.items():
    dates = [datetime.strptime(date[11:], "%H:%M:%S") for date in v["t"]]
    dates.sort()
    dmin, dmax = dates[0], dates[-1]
    print(k, dmin.strftime("%H:%M:%S"), dmax.strftime("%H:%M:%S"))
# gave too many results
'''

'''
# look at zip codes.
for (doc_id, v) in d.items():
    count = {}
    for z in v["z"]:
        if z not in count:
            count[z] = 0
        count[z] += 1

    #c = [(v, k) for (k, v) in count.items()]
    c = list(count.items())
    c.sort()
    if c[0][0][:2] != c[-1][0][:2]:
        #print(doc_id, c[0][0], c[-1][0])
        print(doc_id, ('\n' + doc_id + ' ').join([k for (k, v) in c]))
# doctors generally have consecutive zip codes.
# The 2 first digits of each zip code are the same for legitimate access. 
# pe3k1nn} <--- accesses very many different zip codes
'''

'''
# look if people work on weekends
for (k, v) in d.items():
    dates = [datetime.strptime(date, "%Y-%m-%d %H:%M:%S") for date in v["t"]]
    weekend = [date for date in dates if int(date.strftime("%w")) in [0, 6]]
    if len(weekend):
        print(k, len(weekend), weekend[0].strftime("%m-%d %A %H:%M:%S"))
    #print(k, dmin.strftime("%Y-%m-%d %H:%M:%S"))
# everyone works on weekends. Crazy doctors.
'''

# look at average worktime per day.
for (k, v) in d.items():
    dates = [datetime.strptime(date, "%Y-%m-%d %H:%M:%S") for date in v["t"]]
    days = [None]*30
    for date in dates:
        if date.month != 2:
            print(k, "strange date:", date)
            continue
        day = date.day
        if days[day] == None:
            days[day] = []
        days[day].append(date)

    worktime = []
    noneDays = 0
    for l in days:
        if l == None:
            noneDays += 1
            continue
        l.sort()
        worktime.append((l[-1] - l[0]).total_seconds())

    average = sum(worktime)/(len(worktime) - noneDays)/60/60
    if average >= 7 and average <= 8.5:
        continue
    print(k, average)
# most doctors work between 7 and 8.5 hours a day.
# except two that work 5 hours and 23 hours.
# SSM{b4dd
# 0c7rst0p


# maybe flag?
# SSM{b4dd0c7rst0ppe3k1nn}
