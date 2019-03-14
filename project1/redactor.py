import nltk
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()
import re
from nltk.corpus import wordnet as wn
import thesaurus as th
from thesaurus import Word
import glob
import sys

#Read Text
def read_text(filename):
    with open(filename, 'r') as myfile:
        data=myfile.read().replace('\n', '')
    return(data)


#Names
def reda_names(data3,filename):
    for i in range (len(ls)):
        if ls[i][1] == 'PERSON':
            stats.append([ls[i][0],len(ls[i][0]),filename,'type:Name'])
            data3 = data3.replace(ls[i][0],'█'*len(ls[i][0]))
    return(data3)
        

    
#Location
def reda_address(data3,filename):
    for i in range (len(ls)):
        if ls[i][1] == 'GPE':
            stats.append([ls[i][0],len(ls[i][0]),filename,'type:Address'])
            data3 = data3.replace(ls[i][0],'█'*len(ls[i][0]))
        
    for i in range (len(ls)):
        if ls[i][1] == 'FAC':
            stats.append([ls[i][0],len(ls[i][0]),filename,'type:Address'])
            data3 = data3.replace(ls[i][0],'█'*len(ls[i][0]))
    return(data3)
        

#Date
def reda_date(data3,filename):
    for i in range (len(ls)):
        if ls[i][1] == 'DATE':
            stats.append([ls[i][0],len(ls[i][0]),filename,'type:Date'])
            data3 = data3.replace(ls[i][0],'█'*len(ls[i][0]))
    return(data3) 


        
#Gender
def reda_gender(data3,filename):
    tokens = nltk.word_tokenize(data3)
    genders=['he','she','him','her','his','hers','male','female','man','woman','men','women','boy','girl','lad','lass','dame','congressmen','congresswoman']
    for i in genders:
        for j in range (len(tokens)):
            if i.lower() == tokens[j].lower():
                stats.append([tokens[j],len(tokens[j]),filename,'type:Gender'])
                tokens[j] = '█'*len(i)
                
    reda = ''
    for i in tokens:
        reda = reda+i+' '
    data3 = reda
    
    return(data3)


#Concept
def reda_concept(data3,filename,concept):
    tokens = nltk.word_tokenize(data3)
    w = Word(concept)
    concept=w.synonyms()
    for i in concept:
        for j in range (len(tokens)):
            if i.lower() == tokens[j].lower():
                stats.append([tokens[j],len(tokens[j]),filename,'type:Concept'])
                tokens[j] = '█'*len(i)
    
    reda = ''
    for i in tokens:
        reda = reda+i+' '
    data3 = reda
    
    return(data3)
    
            
#Phone Number
def reda_phone(data3,filename):
    tokens = nltk.word_tokenize(data3)
    for i in range (len(tokens)):
        match = re.search('^\(?([0-9]{3})\)?[-.●]?([0-9]{3})[-.●]?([0-9]{4})$',tokens[i])
        if match:
            stats.append([tokens[i],len(tokens[i]),filename,'type:Phone number'])
            tokens[i] = re.sub('^\(?([0-9]{3})\)?[-.●]?([0-9]{3})[-.●]?([0-9]{4})$','█'*len(tokens[i]),tokens[i])

    reda = ''
    for i in tokens:
        reda = reda+i+' '
    data3 = reda
    
    return(data3)




arg_ls = sys.argv
files=[]
stats=[]

for i in range(len(arg_ls)):

    if arg_ls[i] == '--input':
        files.extend(glob.glob(arg_ls[i+1]))


for i in files:
    data = read_text(i)

    data1 = nlp(data)
    ls = [(X.text, X.label_) for X in data1.ents]

    for j in range(len(arg_ls)):
        if arg_ls[j] == '--names':
            data = reda_name(data,arg_ls[j])

        if arg_ls[j] == '--addresses':
            data = reda_address(data,arg_ls[j])

        if arg_ls[j] == '--dates':
            data = reda_date(data,arg_ls[j])

        if arg_ls[j] == '--phones':
            data = reda_phone(data,arg_ls[j])

        if arg_ls[j] == '--concept':
            data = reda_concept(data,arg_ls[j],arg_ls[j+1])

        if arg_ls[j] == '--genders':
            data = reda_gender(data,arg_ls[j])

        if arg_ls[j] == '--output':
            file = open(i.split('.')[0]+'.redacted.txt','w')

            file.write(data)
            file.close()
