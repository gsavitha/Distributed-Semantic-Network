import json
edges=json.load(open('edges.json'))
noun=set()
for e in edges:
    noun.add(e)
    for m in edges[e]:
        noun.add(m)
f=open("nounmap.txt",'w')
count=0
for n in sorted(noun):
    f.write(str(count)+","+n+"\n")
    count+=1
