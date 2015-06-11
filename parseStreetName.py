import re


def getsdir(value):
    address = value.strip()
    pdir = re.compile(r'\s\b(N|S|E|W)\b$')
    match = pdir.search(address)
    if match:
        post_dir = (match.group()).strip()
        address = address[:match.start()].strip()
        return address, post_dir
    else:
        return address, ''


def getstype(value):
    def usps(name):
        att = {'AV': 'AVE', 'BEND': 'BND',  'BR': 'BRG', 'COMMON': 'CMN',
               'COMMONS': 'CMNS', 'CRSG': 'XING', 'EXPWY': 'EXPY', 'FRWY': 'FWY',
               'GRDN': 'GDN', 'GREEN': 'GRN', 'GROVE': 'GRV', 'HT': 'HTS', 'ISL': 'IS',
               'JCTN': 'JCT', 'LDG': 'LNDG', 'MALL': 'MALL', 'MEADOWS': 'MDWS',
               'NK': 'NCK', 'PK': 'PARK', 'PKE': 'PIKE', 'RT': 'RTE', 'TR': 'TRL',
               'TRAILS': 'TRL', 'TRC': 'TRCE', 'TRNPK': 'TPKE', 'VIEW': 'VW',
               'WK': 'WALK'}
        if name in att:
            return att[name]
        else:
            return name
    street_type = re.compile(r'\b(ALY|ANX|ARC|AV|BDWK|BEND|BLK|BLVD|BR|'
                                r'BTM|BYP|CIR|COMMON|COMMONS|CRES|CRK|'
                                r'CRSG|CSWY|CT|CTR|CV|DR|ESPLND|EST|'
                                r'EXPWY|EXT|FRK|FRWY|GRDN|GREEN|GROVE|'
                                r'HBR|HL|HLS|HOLW|HT|HTS|HWY|ISL|JCTN|'
                                r'LDG|LK|LN|LOOP|MALL|MEADOW|MEADOWS|'
                                r'MKT|MNR|MT|MTN|NK|PASS|PATH|PD|PK|'
                                r'PKE|PKWY|PL|PLZ|PR|PROM|PT|RD|RDG|'
                                r'RDWY|ROW|RT|RUN|SQ|ST|STA|TER|THRWY|'
                                r'TR|TRAILS|TRC|TRNPK|VIEW|VLG|WAY|'
                                r'WHF|WK|YD)\b$')
    match3 = street_type.search(value)
    if match3:
        type = match3.group()
        address = value[:match3.start()].strip()
        return address, usps(type)
    else:
        return value, ''


def main(name):
    address, postdir = getsdir(name)
    stname, type = getstype(address)
    return stname, type, postdir

if __name__ == '__main__':
    import arcpy
    arcpy.env.workspace = r'Database Connections\SCECD.sde'
    t01_ali = 'T01_ALI'
    with arcpy.da.Editor(arcpy.env.workspace) as edit:
        with arcpy.da.UpdateCursor(t01_ali, ['STREET_NAME', 'NAME', 'TYPE', 'SUFDIR']) as cur:
            for row in cur:
                row[1], row[2], row[3] = main(row[0])
                cur.updateRow(row)