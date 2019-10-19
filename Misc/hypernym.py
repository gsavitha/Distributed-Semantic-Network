from nltk.corpus import wordnet as wn
from nltk.tokenize import RegexpTokenizer
import json
edges={}
noun={}
tokenizer = RegexpTokenizer(r'\w+')
edges=json.load(open('edges.json'))
for e in edges:
    if e not in noun:
        output=tokenizer.tokenize(e)
        for w in edges[e]:
            output.extend(tokenizer.tokenize(w))
        for w in output:
            if (w not in noun):
                hyp=""
                for ss in wn.synsets(w):
                    hyp=ss.hypernyms()
                    break
                print(hyp)
                if(len(hyp)):
                    hyp=hyp[0].lemma_names()[0]
                    noun[w]=hyp
json.dump(noun,open("hypernyms.json",'w'),sort_keys=True)
