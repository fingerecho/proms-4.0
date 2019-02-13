# PROMS Server
PROMS Server is an application designed to manage provenance information sent from a series of "reporting systems" which map their processes to a constrained variant of the [PROV Data Model](https://www.w3.org/TR/prov-dm/). It consists of an HTTP API (Python Flask) that both enforces data policy for incoming provenance information and also makes that information available in multiple ways that may help with provenance consuming apps' development. 

PROMS Server works as an application layer on top of an RDF triplestore (graph database) and required a web server, such as Apache, to broker access to it online.

For pretty much everything you need to know about PROMS Server and the family of tools associated with it, see http://promsns.org/wiki/proms.


PROMS Server is jointly maintained by [CSIRO](http://www.csiro.au) and [Geoscience Australia](http://www.ga.gov.au).

### Contact

**Nicholas Car**  - Project Lead  
Geoscience Australia  
nicholas.car@ga.gov.au  


### Adding from fang
adding the config of uwsgi as the version 3.0
adding the config of nginx as the version 3.0

I setted the process numbers to 2 , this is a debug mode
set the process numbers to your CPU core number , when this procedure is online 

after your start this service , check out fuseki service is active
It is listend on port 3030

https://github.com/CSIRO-enviro-informatics/proms

中国溯源平台
https://www.ww315.cn