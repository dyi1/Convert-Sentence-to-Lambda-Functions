import nltk 
from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget
from nltk import Tree, word_tokenize,load_parser
from nltk.corpus import verbnet as vn
from nltk.corpus import wordnet as wn
from nltk.corpus import verbnet 
from nltk.wsd import lesk

metaphor1 = " I run a race" 
metaphor2 = " I run an errand" 
parser = load_parser('NewGrammar.fcfg')
for tree in parser.parse(metaphor1.split()):
    lambdaexpression = (tree.label()['SEM'])
print(lambdaexpression)

parsed = lambdaexpression
swag =[]
verbs=[]
for p in parsed.predicates():
    print(p)
    swag.append(p)
for word,pos in nltk.pos_tag(nltk.word_tokenize(metaphor1)):
    initial = metaphor1.split
    if 'V' in pos: #Another way to focus on only verbs
            verbs.append(word)
print (verbs)

for word,pos in nltk.pos_tag(nltk.word_tokenize(metaphor1)):
    if "N" in pos:
        pos = "n"
    if "V" in pos:
        pos = "v"
    print (lesk(metaphor1, word, pos))## Trying to use for sense identification

for word in verbs:
    final = [sense for sense in vn.classids(word)]
    print (final)
    for sense in final:
        print(vn.pprint_themroles(sense)) ## Compare with all the given senses. 
