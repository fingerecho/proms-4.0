import time
import pyproms
from datetime import datetime
from rdflib import Graph

# declare Reporting System
rs = pyproms.ProvAgent('Fake NEXIS 01',
                      uri='http://fake.com/rs/NEXIS',
                      actedOnBehalfOf=pyproms.ProvAgent('Laura Stanford',
                      uri='http://pid.geoscience.gov.au/person/u15873'))

# input dataset 1
with open('input_dataset_01.txt', 'r') as f:
    text = f.read()
# prov log Dataset 01
e1 = pyproms.ProvEntity('Input Dataset 01',
                        'http://pid.geosceince.gov.au/dataset/1234')

# input dataset 2
# prov log Dataset 02
# from http://www.ga.gov.au/metadata-gateway/metadata/record/gcat_1f59af92-fd8e-a655-e053-12a3070aaa76/Source+Rocks+of+the+Cooper+Basin
# follow the distribution link, download the file
with open('input_dataset_02.txt', 'r') as f:
    text2 = f.read()
e2 = pyproms.ProvEntity('Input Dataset 02',
                        'http://pid.geosceince.gov.au/dataset/1f59af92-fd8e-a655-e053-12a3070aaa76')

# fake processing
# prov log Activity
startedAtTime = datetime.now()
output = text + '\n'
time.sleep(3)
output += text2
time.sleep(3)
endedAtTime = datetime.now()

# output dataset 1
with open('output_dataset_01.txt', 'w') as f:
    f.write(output)
e_out = pyproms.ProvEntity('Output Dataset',
                           'http://pid.geosceince.gov.au/dataset/xyz',
                           #wasAttributedTo=rs,
                           #created=endedAtTime
                           )

a = pyproms.ProvActivity('NEXIS processing',
                         startedAtTime=startedAtTime,
                         endedAtTime=endedAtTime,
                         wasAssociatedWith=rs,
                         used_entities=[e1, e2],
                         generated_entities=[e_out])

# Report generation
r = pyproms.PromsExternalReport('NEXIS Report',
                                wasReportedBy=pyproms.PromsReportingSystem('Fake RS'),
                                nativeId='NEXIS run #34',
                                reportActivity=a,
                                generatedAtTime=endedAtTime)#time.ctime())

with open('report.ttl', 'wb') as f:
    f.write(r.get_graph().serialize(format='turtle'))
