from datetime import datetime
from pyproms import ProvActivity, ProvAgent, ProvEntity
from pyproms.prov_entity import ProvEntity
#from pyproms.proms_serviceentity import PromsServiceEntity
from pyproms.proms_reportingsystem import PromsReportingSystem
from pyproms.proms_report import PromsReport   #, ReportType
from pyproms.report_sender import ReportSender

from pyproms.proms_report_external import PromsExternalReport
def write_res(res,file="./log/test.html"):
  f = open(file,"a",encoding="utf-8")
  f.write(res)
  f.close()

# Ocean Color @ NCI identifier
uri_0 = "http://localhost:5000/function/lodge-reportingsystem/XXXXXX"
rs1 = PromsReportingSystem(None, uri=uri_0)
#uri='http://130.56.244.185/proms/id/reportingsystem/XXXXXX')
#print rs1.serialize_graph()

# PROV Entity 1
e1 = ProvEntity('Test PROV Entity',
                uri='http://go.to#wrtw',
                #wasAttributedTo='http://example.com/4'
                )
e1.set_uri('http://example.org/id/dataset/44')
#e1.set_downloadURL('http://other.com')
#print e1.serialize_graph(format="turtle")

# PROMS Entity 2
e2 = ProvEntity('Test PROMS Entity',
                 uri='http://go.to#wrtw',
                 #downloadURL='http://example.com/4'
                 )
e2.set_uri('http://example.org/id/dataset/45')
#e2.set_downloadURL('http://other.com')
#print e2.serialize_graph(format="turtle")

# PROV Entity g1
g1 = ProvEntity('Test PROV output Entity')
#print g1.serialize_graph(format="turtle")

# PROMS ServiceEntity
e3 = ProvEntity('Geofabric SimpleFeatures WMS request',
                        #serviceBaseUri='http://geofabric.bom.gov.au/simplefeatures/ows',
                        #query='request=GetMap&service=WMS&version=1.2&layers=ahgf_shcarto:AHGFWaterbody,ahgf_shcarto:AHGFMappedStream&format=image%2Fpng&WIDTH=500&HEIGHT=500&BBOX=146.815,-42.05,147.033,-41.825',
                        #queriedAtTime=datetime.now()
                        )
#print e3.serialize_graph(format="turtle")

# PROV Agent
ag1 = ProvAgent('Edward King',
                #name='Edward King',
                #mbox='edward.king@csiro.au'
                )
#print ag1.serialize_graph(format="turtle")

# PROV Activity - the OC processing event seen as a black box
a = ProvActivity('Ocean Colour processing workflow',
                  startedAtTime=datetime.strptime('2018-01-01T12:00:00', '%Y-%m-%dT%H:%M:%S'),
                  endedAtTime=datetime.strptime('2018-01-01T14:00:00', '%Y-%m-%dT%H:%M:%S'),
                  uri=None,
                  wasAssociatedWith=ag1,
                  used_entities=[e1, e2, e3],
                  generated_entities=[g1])
#print a1.serialize_graph(format="turtle")

# some ID from the OC system for reference, perhaps a job number
native_id = 'abc-123'
r1 = PromsReport('Test Report',
                 #ReportType.External,
                 #label=
                 rs1,
                 nativeId = native_id,
                 reportActivity=a,  # same as endingActivity for External Report
                 #a,  # same as startingActivity for External Report
                 #'Test External Report from OC'
                 #startedAtTime=datetime.strptime('2018-01-01T12:00:00', '%Y-%m-%dT%H:%M:%S'),
                 generatedAtTime=datetime.strptime('2018-01-01T14:00:00', '%Y-%m-%dT%H:%M:%S'),
                 )
with open('report.ttl', 'w') as f:
    f.write(str(r1.serialize_graph(),encoding="utf-8"))
f = open("report.ttl","r")
r2 = f.read()
f.close()

# try:
#     report_sender = ReportSender()
#     url = 'http://localhost:5000/function/lodge-report'
#     r = report_sender.post(url, r2)#r1)
#     #import pprint
#     #pprint.pprint(r.text)
#     write_res(r.text)
# except Exception as e:
#     print(str(e))

import requests

r = requests.post(
    url = "http://localhost:5000/function/lodge-report",
    data=open("./report.ttl","r").read(),
    headers={'Content-Type': 'text/turtle'}
)
print((r.content))


"""
        ('text/turtle', 'turtle'),
        ('application/rdf+xml', 'xml'),
        ('application/rdf xml', 'xml'),
        ('application/rdf+json', 'json-ld'),
        ('application/rdf json', 'json-ld'),
        ('application/json', 'json-ld'),
        ('text/ntriples', 'nt'),
        ('text/nt', 'nt'),
        ('text/n3', 'nt')
        """


