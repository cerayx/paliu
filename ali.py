import os
import datetime
from collections import defaultdict
import sde


class stats:
    def __init__(self, total, inserts, changes, deletes):
        self.reportedTotal = total
        self.projectedInserts = inserts
        self.projectedChanges = changes
        self.projectedDeletes = deletes
        self.init_analysis()

    def init_analysis(self):
        self.foc = (self.projectedInserts, self.projectedChanges,
                    self.projectedDeletes)
        print 'Inserts: {}\nChanges: {}\nDeletes: {}'.format(*self.foc)
        print self.reportedTotal, sum(self.foc)
        if self.reportedTotal != sum(self.foc):
            from sys import exit
            print 'counts do not match'
            exit(0)


def parse(bsdi_file, today, source_name):
    def strip_list(rec):
        return map(
            lambda x: x.strip() if isinstance(x, basestring) else x, rec)

    def concat(*data):
        if not isinstance(data, list) and not isinstance(data, tuple):
            # Check to catch strings, int, and floats types.
            data = data, ''
        attributes = map(str.strip, (str(x) for x in data if x is not None))
        attributes_list = (' '.join(x.split()) for x in attributes if x != '')
        return ' '.join(attributes_list)

    for line in bsdi_file:
        # parses body
        if line[0] in ('C', 'I', 'D'):
            change_date = datetime.datetime.strptime(
                line[190:196].strip(), "%m%d%y")
            stnum = int(line[11:21] or 0)
            address = concat(stnum, line[21:25], line[25:27], line[27:67])
            fullname_esn = concat(line[21:25], line[25:27], line[27:67],
                                  line[165:168])
            row = (line[0], '', line[1:11], stnum, line[21:25], line[25:27],
                   line[27:67], line[73:105], line[105:107], line[107:127],
                   line[127:159], line[159:160], line[160:161], line[161:165],
                   line[165:168], line[170:180], line[180:187], change_date,
                   line[196:200], line[200:205], address, today, source_name,
                   fullname_esn)
            # row does not include FILLER D, END OF RECORD, NEW LINE CHARACTER
            # positions.
            yield strip_list(row)
        elif line[0:3] == 'UHL':
            # parses header/first row
            row = line[0], '', line[0:3], line[5:11], line[11:61], line[61:67]
            yield strip_list(row)
        elif line[0:3] == 'UTL':
            # parses header/last row
            count = int(line[61:70]or 0)
            row = line[0], '', line[0:3], line[5:11], line[11:61], count
            yield strip_list(row)


def analysis(footer_count, *foc):
    print 'Inserts: {}\nChanges: {}\nDeletes: {}'.format(*foc)
    print footer_count, sum(foc)
    if footer_count != sum(foc):
        from sys import exit
        print 'counts do not match'
        exit(0)


def process(text_file):
    filename = os.path.basename(text_file)
    process_date = datetime.datetime.now()
    data = defaultdict(dict)
    with open(text_file, 'r') as text:
        for i in parse(text, process_date, filename):
            group_key, primary_key, values = i[0], i[2], i[1:]
            data[group_key][primary_key] = values

    analysis = (data['U']['UTL'][4], len(data['I']),
                len(data['C']), len(data['D']))
    return data['I'], data['C'], data['D'], analysis


def main(file, ali):
    insert_data, change_data, delete_data, numbers = process(file)
    data_counts = stats(*numbers)
    sde.deletes(delete_data, ali)
    sde.changes(change_data, ali)
    sde.inserts(insert_data, ali)


if __name__ == '__main__':
    data_file = os.path.join(os.getcwd(), 'bdaily20150512')
    t01_ali = r'Database Connections\2014 Test.sde\GIS.DBO.T01_ALI'
    main(data_file, t01_ali)
