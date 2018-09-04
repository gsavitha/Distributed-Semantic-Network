import json
import pickle
f=open('triplets.txt','r')
edges={}
rel={}
for l in f:
    l=l.strip().split(',')
    if(len(l)!=3):
        continue
    if l[0] in edges:
        if l[2] not in edges[l[0]]:
            edges[l[0]].append(l[2])
        if(l[0]+","+l[2] in rel):
            if l[1] not in rel[l[0]+","+l[2]]:
                rel[l[0]+","+l[2]].append(l[1])
        else:
            rel[l[0]+","+l[2]]=[l[1]]
    else:
        edges[l[0]]=[l[2]]
        rel[l[0]+","+l[2]]=[l[1]]
print(len(edges))
fp1=open('edges.json','w')
json.dump(edges,fp1,sort_keys=True)
fp2=open('rel.json','w')
json.dump(rel,fp2,sort_keys=True)
fp3=open('rel.pkl','wb')
pickle.dump(rel,fp3)
