import networkx as nx
import sys
import json
import pickle
import matplotlib.pyplot as plt
word=sys.argv[1]
edges=json.load(open("edges.json"))
rel=pickle.load(open('rel.pkl','rb'))
hypernym=json.load(open('hypernyms.json'))
count=1
for r in rel:
    print(r,rel[r])
    count+=1
    if(count==10):
        break
graph_edges=[]
e=word
hyp=[]
if e in hypernym:
    hyp.append([e,hypernym[e]])
if e in edges:
    for v in sorted(edges[e]):
        graph_edges.append([e,v,rel[e+","+v]])
        if v in hypernym:
            hyp.append([v,hypernym[v]])

hyp=[]
G=nx.Graph()
for x in graph_edges:
    for m in x[2]:
        G.add_edge(x[0],x[1],l=m)
for x in hyp:
    G.add_edge(x[0],x[1],color='blue')
nx.draw(G)
edge_labels = nx.get_edge_attributes(G,'l')
pos = nx.spring_layout(G, scale=2)
nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels)


plt.savefig('bank.png')
