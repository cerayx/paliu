import arcpy
import os


def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]


def inserts(data, table):
    with arcpy.da.Editor(os.path.dirname(table)) as edit:
        with arcpy.da.InsertCursor(table, '*') as cur:
            for k in data:
                cur.insertRow(data[k])

def deletes(data, table):
    if data:
        bits = chunks(data.keys(), 20)
        for z in bits:
            query = '"TELEPHONE_NUMBER" IN ({})'.format(", ".join(z))
            print query
        # count = 0
        #print insertQuery
    #     with arcpy.da.UpdateCursor(ali_table, 'TELEPHONE_NUMBER', deleteQuery) as cur:
    #         for row in cur:
    #             if row[0] in delete_data:
    #                 count += 1
    #                 cur.deleteRow()
    #     print '{0} Rows deleted'.format(count)
    # else:
    #     print '0 rows deleted'

if __name__ == '__main__':
    pass
