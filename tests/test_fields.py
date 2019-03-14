import pytest
import en_core_web_sm
nlp = en_core_web_sm.load()
import project1

from project1 import redactor
from project1 import main

def test_names():
    data = 'John'
    data1 = data
    data = nlp(data)
    ls = [(X.text, X.label_) for X in data.ents]
    name_test = redactor.reda_names(data1,'none',ls)
    assert name_test == '████'


def test_address():
    data = 'Elm Street, Norman, Oklahoma'
    data1 = data
    data = nlp(data)
    ls = [(X.text, X.label_) for X in data.ents]
    address_test = redactor.reda_address(data1,'none',ls)
    assert address_test == '██████████, ██████, ████████'

def test_dates():
    data = '20/01/1984'
    data1 = data
    data = nlp(data)
    ls = [(X.text, X.label_) for X in data.ents]
    date_test = redactor.reda_date(data1,'none',ls)
    assert date_test == '██████████'


def test_gender():
    data = 'MAN'
    gender_test = redactor.reda_gender(data,'none')
    assert len(gender_test) ==len('███')


def test_concept():
    data = 'drink'
    concept_test = redactor.reda_concept(data,'none','water')
    assert len(concept_test) == len('█████')

def test_phone():
    data = '405-489-4352'
    phone_test = redactor.reda_phone(data,'none')
    assert len(phone_test) ==len('████████████')



