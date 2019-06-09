from datetime import datetime
from pyproms import ProvActivity, ProvAgent, ProvEntity
from pyproms.proms_entity import PromsEntity
from pyproms.proms_serviceentity import PromsServiceEntity
from pyproms.proms_reportingsystem import PromsReportingSystem
from pyproms.proms_report import PromsReport, ReportType
from pyproms.report_sender import ReportSender


# Ocean Color @ NCI identifier
rs1 = PromsReportingSystem(None, uri="http://localhost:5000/id/reportingsystem/XXXXXX")
#uri='http://130.56.244.185/proms/id/reportingsystem/XXXXXX')
#print rs1.serialize_graph()

# PROV Entity 1
e1 = ProvEntity('Test PROV Entity',
                uri='http://go.to#wrtw',
                downloadURL='http://example.com/4')
e1.set_uri('http://example.org/id/dataset/44')
e1.set_downloadURL('http://other.com')
#print e1.serialize_graph(format="turtle")

# PROMS Entity 2
e2 = PromsEntity('Test PROMS Entity',
                 uri='http://go.to#wrtw',
                 downloadURL='http://example.com/4')
e2.set_uri('http://example.org/id/dataset/45')
e2.set_downloadURL('http://other.com')
#print e2.serialize_graph(format="turtle")

# PROV Entity g1
g1 = ProvEntity('Test PROV output Entity')
#print g1.serialize_graph(format="turtle")

# PROMS ServiceEntity
e3 = PromsServiceEntity('Geofabric SimpleFeatures WMS request',
                        serviceBaseUri='http://geofabric.bom.gov.au/simplefeatures/ows',
                        query='request=GetMap&service=WMS&version=1.2&layers=ahgf_shcarto:AHGFWaterbody,ahgf_shcarto:AHGFMappedStream&format=image%2Fpng&WIDTH=500&HEIGHT=500&BBOX=146.815,-42.05,147.033,-41.825',
                        queriedAtTime=datetime.now())
#print e3.serialize_graph(format="turtle")

# PROV Agent
ag1 = ProvAgent('Edward King',
                name='Edward King',
                mbox='edward.king@csiro.au')
#print ag1.serialize_graph(format="turtle")

# PROV Activity - the OC processing event seen as a black box
a = ProvActivity('Ocean Colour processing workflow',
                  datetime.strptime('2015-01-01T12:00:00', '%Y-%m-%dT%H:%M:%S'),
                  datetime.strptime('2015-01-01T14:00:00', '%Y-%m-%dT%H:%M:%S'),
                  uri=None,
                  wasAssociatedWith=ag1,
                  used_entities=[e1, e2, e3],
                  generated_entities=[g1])
#print a1.serialize_graph(format="turtle")

# some ID from the OC system for reference, perhaps a job number
native_id = 'abc-123'
r1 = PromsReport('Test Report',
                 ReportType.External,
                 rs1,
                 native_id,
                 a,  # same as endingActivity for External Report
                 a,  # same as startingActivity for External Report
                 'Test External Report from OC')
with open('oc_report.ttl', 'w') as f:
    f.write(r1.serialize_graph())

try:
    report_sender = ReportSender()
    r = report_sender.post('http://130.56.244.185/proms/id/report/', r1)
    import pprint
    pprint.pprint(r.text)
except Exception, e:
    print e.message