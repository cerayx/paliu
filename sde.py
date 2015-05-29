import arcpy
import os


def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i + n]


def inserts(idata, table):
    count = 0
    with arcpy.da.Editor(os.path.dirname(table)) as edit:
        with arcpy.da.InsertCursor(table, '*') as cur:
            for k in idata:
                cur.insertRow(idata[k])
                count += 1
        return count


def deletes(ddata, table):
    count = 0
    if ddata:
        bits = chunks(ddata.keys(), 1000)
        for z in bits:
            qry = '"TELEPHONE_NUMBER" IN ({})'.format(", ".join(z))
            with arcpy.da.UpdateCursor(table, 'TELEPHONE_NUMBER', qry) as cur:
                for row in cur:
                    count += 1
                    cur.deleteRow()
        return count
    else:
        return count


def changes(cdata, table):
    return [deletes(cdata, table), inserts(cdata, table)]


if __name__ == '__main__':
    pass
