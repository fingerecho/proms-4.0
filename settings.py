import os
import logging
import subprocess

VERSION = "v4.0"#subprocess.check_output(["git", "describe"]).split('-')[0].replace('v', '')
BASE_URI = 'http://localhost:5000'
ACTIVITY_BASE_URI = 'http://localhost:5000/activity/'
AGENT_BASE_URI = 'http://localhost:5000/agent/'
ENTITY_BASE_URI = 'http://localhost:5000/entity/'
PERSON_BASE_URI = 'http://localhost:5000/person/'
REPORT_BASE_URI = 'http://localhost:5000/report/'
REPORT_NAMED_GRAPH_BASE_URI = 'http://localhost:5000/report/'
REPORTINGSYSTEM_BASE_URI = 'http://localhost:5000/reportingsystem/'
REPORTINGSYSTEM_NAMED_GRAPH_BASE_URI = 'http://localhost:5000/reportingsystem/'
PINGBACK_BASE_URI = 'http://localhost:5000/pingback/'
PINGBACK_NAMED_GRAPH_BASE_URI = 'http://localhost:5000/pingback/'
PINGBACK_RESULTS_NAMED_GRAPH_BASE_URI = 'http://localhost:5000/pingbackresults/'

HOME_DIR = os.path.dirname(os.path.abspath(__file__))
#LOGFILE = '/var/log/proms/' + 'proms-v4.log'
LOGFILE = './log/' + 'proms-v4.log'
LOG_LEVEL = logging.DEBUG
DEBUG = True

#   Internal SPARQL endpoints
#SPARQL_QUERY_URI = 'http://vt.fyping.cn:3030/tdb/query'
#SPARQL_UPDATE_URI = 'http://vt.fyping.cn:3030/tdb/update'
#SPARQL_AUTH_USR = ''  # Ensure this matches any triplestore proxying settings (install-apache.sh)
#SPARQL_AUTH_PWD = ''  # Ensure this matches any triplestore proxying settings (install-apache.sh)
#SPARQL_TIMEOUT = 5  # Request Timeout in seconds

SPARQL_QUERY_URI = 'http://localhost:3030/tdb/query'
SPARQL_UPDATE_URI = 'http://localhost:3030/tdb/update'
SPARQL_AUTH_USR = ''  # Ensure this matches any triplestore proxying settings (install-apache.sh)
SPARQL_AUTH_PWD = ''  # Ensure this matches any triplestore proxying settings (install-apache.sh)
SPARQL_TIMEOUT = 5  # Request Timeout in seconds
