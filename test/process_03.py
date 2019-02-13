import time
import pyproms
from datetime import datetime
from rdflib import Graph

from py2neo.ogm import GraphObject, Property, Label, RelatedFrom
from py2neo import Graph as PoGraph
gh = PoGraph(auth=("neo4j","xiaohaidan"),host="vt.fyping.cn",port=7687,scheme="bolt",secure=False,user="neo4j")

class Agent(GraphObject):
    __primarykey__ = "uri"

    uri = Property()
    actedOnBehafOf = Property("Agent")

class Entity(GraphObject):
    __primarykey__ = "uri"
    
    uri = Property()
    comment = Property()

class Activity(GraphObject):
    __primarykey__ = "uri"

    uri = Property()
    startedAtTime = Property()
    endedAtTime = Property()
    wasAssociatedWith = RelatedFrom("Agent")
    wasInformedBy = RelatedFrom("Agent")

# declare Reporting System
rs = pyproms.ProvAgent('Fake NEXIS 01',
                                  uri='http://fake.com/rs/NEXIS',
                                  actedOnBehalfOf=pyproms.ProvAgent('Laura Stanford',
                                                                    uri='http://pid.geoscience.gov.au/person/u15873'))
agent_ = Agent()
agent_.uri = rs.uri
agent_.actedOnBehalfOf = rs.actedOnBehalfOf.actedOnBehalfOf



# input dataset 1
with open('input_dataset_01.txt', 'r') as f:
    text = f.read()
# prov log Dataset 01
e1 = pyproms.ProvEntity('Input Dataset 01',
                        'http://pid.geosceince.gov.au/dataset/1234')

entity_ = Entity()
entity_.uri = e1.uri
entity_.comment = e1.comment

# input dataset 2
# prov log Dataset 02
# from http://www.ga.gov.au/metadata-gateway/metadata/record/gcat_1f59af92-fd8e-a655-e053-12a3070aaa76/Source+Rocks+of+the+Cooper+Basin
# follow the distribution link, download the file
with open('input_dataset_02.txt', 'r') as f:
    text2 = f.read()
e2 = pyproms.ProvEntity('Input Dataset 02',
                        'http://pid.geosceince.gov.au/dataset/1f59af92-fd8e-a655-e053-12a3070aaa76')

entity_2 = Entity()
entity_2.uri = e2.uri
entity_2.comment = e2.comment

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
entity_out = Entity()
entity_out.uri = e_out.uri
entity_out.comment = e_out.comment

a = pyproms.ProvActivity('NEXIS processing',
                         startedAtTime=startedAtTime,
                         endedAtTime=endedAtTime,
                         wasAssociatedWith=rs,
                         used_entities=[e1, e2],
                         generated_entities=[e_out])
actity_a = Activity()
actity_a.uri = a.uri
actity_a.startedAtTime = a.startedAtTime
actity_a.endedAtTime = a.endedAtTime
actity_a.wasAssociatedWith = a.wasAssociatedWith
actity_a.wasInformedBy = a.wasInformedBy

gh.push(actity_a)
gh.push(entity_out)
gh.push(entity_2)
gh.push(entity_)
gh.push(agent_)
# Report generation
r = pyproms.PromsExternalReport('NEXIS Report',
                                wasReportedBy=pyproms.PromsReportingSystem('Fake RS'),
                                nativeId='NEXIS run #34',
                                reportActivity=a,
                                generatedAtTime=endedAtTime)#time.ctime())

with open('report.1908.ttl', 'wb') as f:
    f.write(r.get_graph().serialize(format='turtle'))
