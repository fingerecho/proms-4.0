import requests
PROMS_BASE_URI = "http://localhost:5000"
PROMS_HOME_DIR = ".."
import os
from __init__ import w_l

def load_rs():
    # load the example ReportingSystem, System 01
    r = requests.post(
        PROMS_BASE_URI + '/function/lodge-reportingsystem',
        #data=open(os.path.join(PROMS_HOME_DIR, 'tests', 'example_data_rs_01.ttl'),
        #	"r",encoding="utf-8").read(),
        data = open("./report.reportingsystem.ttl","r",encoding="utf-8").read(),
        headers={'Content-Type': 'text/turtle'}
    )
    w_l(r.text)
    w_l(r.content.decode(encoding="utf-8"))
    print(r.content)
    print(r.status_code)
    #assert r.status_code == 201

if __name__ == '__main__':
	load_rs()