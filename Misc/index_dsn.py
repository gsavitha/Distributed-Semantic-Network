import os
import operator
import json
import pysolr

solr = pysolr.Solr('http://localhost:8983/solr/dsn')
edges=json.load(open('edges.json'))
hypernym=json.load(open('hypernyms.json'))
solr_insert=[]
for e in edges:
    results=solr.search(q='id:\"'+e+'\"')
    hyp=''
    if e in hypernym:
        hyp=hypernym[e]
        del hypernym[e]
        #print(hyp)
    solr_insert.append({"id":e,"edges":edges[e],"hypernym":hyp})
solr.add(solr_insert)
solr_insert=[]
for h in hypernym:
    solr_insert.append({"id":h,"edges":[],"hypernym":hyp})
solr.add(solr_insert)
