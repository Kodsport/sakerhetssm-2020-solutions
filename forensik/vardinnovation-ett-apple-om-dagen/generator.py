import datetime
import numpy
import random
import string
import sys

F1 = "SSM{b4dd"
F2 = "0c7rst0p"
F3 = "pe3k1nn}"
A = string.ascii_lowercase + string.digits

def rnd(s):
    return ''.join(random.choice(A) for _ in range(len(s)))

DAYS = 29
FIRST_DAY = datetime.date(year=2020, month=2, day=1)
START_TIME = datetime.time(9)
DUR = datetime.timedelta(hours=8)
NVISITS_AVG = 20
NVISITS_STDDEV = 5
AVG_WAIT_MIN = datetime.timedelta(minutes=10)
AVG_WAIT_MAX = datetime.timedelta(minutes=60)
AREA_CODE_DIGITS = 2

all_visits = []

def do_gen(did, start, duration, nvisits, nvisits_stddev, area_digs):
    area_prefix = ([random.choice(range(1, 10))] + [random.choice(range(10)) for _ in range(4)])[:area_digs]
    for k in range(DAYS):

        date = FIRST_DAY + datetime.timedelta(days=k)
        visits = max(int(numpy.random.normal(nvisits, nvisits_stddev)), 1)
        cur_time = datetime.datetime.combine(date, start)
        end_time = datetime.datetime.combine(date, start) + duration

        visit_len = (duration // visits).seconds
        for _ in range(DAYS):
            if cur_time > end_time: break
            area_code = area_prefix + [random.choice(range(10)) for _ in range(5 - len(area_prefix))]
            area_code = ''.join(str(x) for x in area_code)
            visit_times = int(numpy.random.normal(visit_len, visit_len // 7))
            cur_time = cur_time + datetime.timedelta(seconds = visit_times)
            all_visits.append(f"{did},{cur_time},{area_code}")


def generate_normal(flag, f, t):
    did = flag[:f] + rnd(flag[f:t]) + flag[t:]
    do_gen(did, START_TIME, DUR, NVISITS_AVG, NVISITS_STDDEV, AREA_CODE_DIGITS)

# Unusually many journals
def generate1():
    did = F1
    NVISITS_AVG = 40
    do_gen(did, START_TIME, DUR, NVISITS_AVG, NVISITS_STDDEV, AREA_CODE_DIGITS)

# Checks journals all night
def generate2():
    did = F2
    START_TIME = datetime.time(0)
    DUR = datetime.timedelta(hours=24)
    do_gen(did, START_TIME, DUR, NVISITS_AVG, NVISITS_STDDEV, AREA_CODE_DIGITS)

# Checks journals everywhere
def generate3():
    did = F3
    do_gen(did, START_TIME, DUR, NVISITS_AVG, NVISITS_STDDEV, 0)

for i in range(999):
    generate_normal(F1, 4, 8)
generate1()

for i in range(999):
    generate_normal(F2, 0, 8)
generate2()

for i in range(999):
    generate_normal(F3, 0, 7)
generate3()

print("doctor_id,timestamp,patient_zip")
random.shuffle(all_visits)
for s in all_visits: print(s)
 
print(f"Flag is {F1}{F2}{F3}", file=sys.stderr)
