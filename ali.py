import os
import datetime
from collections import defaultdict


def function(bsdi_file):
    for line in bsdi_file:
        if line[0] in ('C', 'I', 'D'):
            change_date = datetime.datetime.strptime(
                line[190:196].strip(), "%m%d%y")
            stnum = int(line[11:21] or 0)
            data = (line[0], line[1:11], stnum, line[21:25], line[25:27],
                    line[27:67], line[67:73], line[73:105], line[105:107],
                    line[107:127], line[127:159], line[159:160], line[160:161],
                    line[161:165], line[165:168], line[168:170], line[170:180],
                    line[180:187], line[187:190], change_date, line[196:200],
                    line[200:205], line[205:239], line[239], line[240])
            yield data


def main(df):
    e = defaultdict(dict)
    with open(df, 'r') as f:
        for i in function(f):
             e[i[0]] = i[1:11]: i[1:]

    print len(e['C']), len(e['D']), len(e['I'])

if __name__ == '__main__':
    data_file = os.path.join(os.getcwd(), 'bdaily20150512')
    main(data_file)
