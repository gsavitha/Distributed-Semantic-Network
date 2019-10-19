import markov_clustering as mc
import networkx as nx
import random
import json

G=nx.Graph()
edges=json.load(open('edges.json'))
nodes=set()
noun={}
renoun={}
f=open('nounmap.txt')
for l in f:
    x,y=l.strip().split(',')
    noun[int(x)]=y
count=0
labels={}
n_c=0
nset=set()
for e in edges:
    if e not in nset:
        nset.add(e)
        labels[n_c]=e
        n_c+=1
    for n in edges[e]:
        count+=1
        G.add_edge(e,n)
        if(n not in nset):
            nset.add(n)
            labels[n_c]=n
            n_c+=1
        if(count>2000):
            break
    if(count>2000):
        break
noun={}
renoun={}
#positions = {i:(random.random() * 2 - 1, random.random() * 2 - 1) for i in nodes}
matrix = nx.to_scipy_sparse_matrix(G)
result = mc.run_mcl(matrix,inflation=1.4)
clusters = mc.get_clusters(result)
f=open('clusters.txt','w')
count=0
for cl in clusters:
    f.write("\nCluster "+str(count)+"\n")
    count+=1
    for n in cl:
        f.write(labels[n]+"\n")
print(len(clusters))
print("&")
mc.draw_graph(matrix, clusters, node_size=40,with_labels=False,edge_color="silver")
p=input()
