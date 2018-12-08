import os, csv, re, operator
from datetime import datetime
from collections import Counter

script_dir = os.path.dirname(__file__)

data = []
input1 = 'input/day04.csv'

with open(os.path.join(script_dir, input1)) as f:
    for row in f:
        data.append(row)

def orderdata(data):
    ordereddata = []
    for i in data:
        matches = re.search(r'\[(.*)\] (.*)', i)
        datetime_object = datetime.strptime(matches.group(1), '%Y-%m-%d %H:%M')
        ordereddata.append([datetime_object, matches.group(2)])

    return sorted(ordereddata,key = lambda l:l[0])

def arrangedata(data):
    timer, guard = 0, 0
    logs = {}
    for log in data:
        hour, minute = log[0].hour, log[0].minute
        if '#' in log[1]:
            guard = int(re.search('(\d+)', log[1]).group(1))
        if hour == 0:
            if guard not in logs: logs[guard] = []
            if 'sleep' in log[1]:
                timer = minute
            if 'wakes' in log[1]:
                for i in range(timer,minute):
                    logs[guard].append(i)
    for guard, sleeplist in logs.items():  logs[guard] = Counter(sleeplist)
    return logs

def part1(timedata: list):
    logs = arrangedata(timedata)

    maxkey, maxvalue = 0, 0
    for key, value in logs.items():
        som = sum(value.values())
        if sum(value.values()) > maxvalue:
            maxvalue = som
            maxkey = key
    
    # map(lambda x: x , logs[maxkey]):
    maxminute = max(logs[maxkey].items(), key=operator.itemgetter(1))[0]
    return maxminute*maxkey

def part2(timedata: list):
    logs = arrangedata(timedata)

    maxkey, maxamountminute = 0, 0
    for key, value in logs.items():
        #print(value.values())
        maxmin = max(value.values()) if value.values() else -1
        if maxmin > maxamountminute:
            maxamountminute = maxmin
            maxkey = key
    #print(maxkey, logs[maxkey].values())

    maxminute = max(logs[maxkey].items(), key=operator.itemgetter(1))[0]

    return maxminute*maxkey

if __name__ == "__main__":
    
    testdata = [
'[1518-11-01 00:00] Guard #10 begins shift',
'[1518-11-01 00:05] falls asleep',
'[1518-11-01 00:25] wakes up',
'[1518-11-01 00:30] falls asleep',
'[1518-11-01 00:55] wakes up',
'[1518-11-01 23:58] Guard #99 begins shift',
'[1518-11-02 00:40] falls asleep',
'[1518-11-02 00:50] wakes up',
'[1518-11-03 00:05] Guard #10 begins shift',
'[1518-11-03 00:24] falls asleep',
'[1518-11-03 00:29] wakes up',
'[1518-11-04 00:02] Guard #99 begins shift',
'[1518-11-04 00:36] falls asleep',
'[1518-11-04 00:46] wakes up',
'[1518-11-05 00:03] Guard #99 begins shift',
'[1518-11-05 00:45] falls asleep',
'[1518-11-05 00:55] wakes up',
    ]

    assert part1(orderdata(testdata)) == 240

    print(part1(orderdata(data)))

    assert part2(orderdata(testdata)) == 4455

    print(part2(orderdata(data)))