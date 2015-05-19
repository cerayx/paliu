import arcpy
import os


def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i + n]


def inserts(data, table):
    with arcpy.da.Editor(os.path.dirname(table)) as edit:
        with arcpy.da.InsertCursor(table, '*') as cur:
            for k in data:
                cur.insertRow(data[k])


def deletes(data, table):
    if data:
        bits = chunks(data.keys(), 1000)
        for z in bits:
            query = '"TELEPHONE_NUMBER" IN ({})'.format(", ".join(z))
            with arcpy.da.UpdateCursor(table, 'TELEPHONE_NUMBER', query) as cur:
                for row in cur:
                    if row[0] in data.iterkeys():
                        # count += 1
                        cur.deleteRow()


def changes(data, table):
    deletes(data, table)
    inserts(data, table)


if __name__ == '__main__':
    pass
