import logging
from pyproms import *
import os
from datetime import datetime
import requests
import json

def insert(g, named_graph_uri=None):
    """ Securely insert a named graph into the DB"""
    if named_graph_uri:
        data = {'update': 'INSERT DATA { GRAPH <' + named_graph_uri + '> { ' + g.serialize(format='nt').decode("utf-8") + ' } }'}
    else:  # insert into default graph
        data = {'update': 'INSERT DATA { ' + g.serialize(format='nt').decode("utf-8") + ' }'}
    auth = ("","")#(settings.SPARQL_AUTH_USR, settings.SPARQL_AUTH_PWD)
    headers = {'Accept': 'text/turtle'}
    try:
        r = requests.post("http://localhost:3030/tdb/update", headers=headers, data=data, auth=auth, timeout=1)
        if r.status_code != 200 and r.status_code != 201:
            raise Exception('The INSERT was not successful. The SPARQL database\' error message is: ' + r.content)
        return True
    except requests.ConnectionError as e:
        raise Exception()


def make_basic_report():
    # Example Agents, could be people or Organisations
    ag = ProvAgent("Agent Orange")
    agx = ProvAgent("Agent X")

    # A ReportingSystem (Agent subclass)
    # This is the system that actually generates the Reports
    rs = PromsReportingSystem('test-lsu')
    #rs.set_uri(uri="http://localhost:5000/reportingsystem/c2f3513b-74c8-47c6-b486-4fda722270e5")
    rs.set_uri(uri="http://localhost:5000/reportingsystem/84a3bcfe-bdb6-4029-906d-e527182628c3")

    # The single Activity, as Basic Reports only allow 1
    startedAtTime = datetime.strptime('2014-06-25T12:13:14', '%Y-%m-%dT%H:%M:%S')
    endedAtTime = datetime.strptime('2014-06-25T12:13:24', '%Y-%m-%dT%H:%M:%S')
    report_activity = ProvActivity('Test Activity',
                                   startedAtTime,
                                   endedAtTime,
                                   wasAssociatedWith=agx,
                                   comment='A test Activity')
    generatedAtTime = datetime.strptime('2014-06-25T12:13:34', '%Y-%m-%dT%H:%M:%S')

    # make the Report
    r = PromsBasicReport('Test Basic Report PyPROMS',
                         rs,  # this is the Reporting System
                         'test-lsu',  # this could be anything that the Reporting System uses to keep track of Reports
                         report_activity,
                         generatedAtTime,
                         comment='This is an example Basic Report')

    return r


def test_report_send():
    rs = ReportSender()
    #post a report file
    # r = rs.post(
    #     'http://localhost:5000/function/lodge-report',
    #     'report.ttl',
    #     #os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'examples', 'example_report_basic.ttl')
    # )
    # print(r.status_code)
    # print(r.text)
    # assert r.status_code == 201

    # post a Report object
    r = rs.post(
        proms_report_lodging_uri='http://localhost:5000/function/lodge-report',
        report = make_basic_report()
    )
    print(r.status_code)
    print(r.text)
    #assert r.status_code == 201

def test_sparql_query():
    def query(sparql_query, format_mimetype='application/sparql-results+json'):
        """ Make a SPARQL query"""
        auth = ('','')
        data = {'query': sparql_query}
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': format_mimetype
        }
        try:
            r = requests.post('http://localhost:3030/tdb/query', auth=auth, data=data, headers=headers, timeout=1)
            return json.loads(r.text)
        except Exception as e:
            raise e
    sql = """
        SELECT ?subject ?predicate ?object
        WHERE {
          ?subject ?predicate ?object
        }
        LIMIT 25
    """
    res = query(sql)
    print(res)

def test_sparql_insert():
    def insert(g, named_graph_uri=None):
        """ Securely insert a named graph into the DB"""
        if named_graph_uri:
            data = {'update': 'INSERT DATA { GRAPH <' + named_graph_uri + '> { ' + g.serialize(format='nt').decode("utf-8") + ' } }'}
        else:  # insert into default graph
            data = {'update': 'INSERT DATA { ' + g.serialize(format='nt').decode("utf-8") + ' }'}
        auth = ("","")#(settings.SPARQL_AUTH_USR, settings.SPARQL_AUTH_PWD)
        headers = {'Accept': 'text/turtle'}
        try:
            r = requests.post("http://localhost:3030/tdb/update", headers=headers, data=data, auth=auth, timeout=1)
            if r.status_code != 200 and r.status_code != 201:
                raise Exception('The INSERT was not successful. The SPARQL database\' error message is: ' + r.content)
            return True
        except requests.ConnectionError as e:
            raise Exception()
    from rdflib import RDF, RDFS
    from rdflib import Graph, BNode
    g=Graph()                         
    a=BNode('foo')                    
    b=BNode('bar')                    
    c=BNode('baz')                    
    g.add((a,RDF.first,RDF.type))     
    g.add((a,RDF.rest,b))             
    g.add((b,RDF.first,RDFS.label))   
    g.add((b,RDF.rest,c))             
    g.add((c,RDF.first,RDFS.comment)) 
    g.add((c,RDF.rest,RDF.nil))
    
    from rdflib import RDF, RDFS
    from rdflib import Graph, BNode
    named_graph_uri = "http://localhost:5000/reportingsystem/d4ec6c2a-f305-4c7b-bbb7-a230d56f1eb7"
    insert(g,named_graph_uri=named_graph_uri)

if __name__ == '__main__':
    logging.basicConfig()

    #test_report_send()
    #result = make_basic_report()
    #if insert(result.get_graph()):print("insert successfully")
    #print(type(result))
    test_report_send()
    #test_sparql_query()
    #test_sparql_insert()
