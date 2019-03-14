# cs5293sp19-project1
Text Redactor

The project's motive is to redact sensitive information from documents by detecting senstive elements from the given input such as names, address,gender and phone numbers and also redact information related to a given concept.

The functions used to redact each of the elements above the following functions were used.

The input for the project is a group of textfiles and the output is the redacted text files.

reda_name function:

The function uses the package spacy to obtain the tag 'PERSON' for the names of people according to context and redacts these accordingly.

reda_address function:

The function uses the package spacy to obtain the tags 'GPE' and 'LOC' for addresses(USA) according to context and redacts these accordingly.

reda_date function:

The function uses the package spacy to obtain the 'DATE' tag, it identifies the date formats like '12 November 1989' and 12/03/2013 and 13-09-2000  and redacts them accordingly.

reda_gender function:

The function compares tokens after tokenizing using the tokeize function from nltk to a given set of gender identifying terms and redacts the text if found in the set.

reda_phone function:

The function uses a regular expression to search for a phone number of various formats of American phone numbers of formats xxx-xxx-xxxx or (xxx) xxx xxxx or xxxxxxxxxx etc.

reda_concept function:

The function uses the thesaurus package to find synonyms and related words, and search for them in the tokenized text and redact accordingly in the text.

Expected input : pipenv run python redactor.py --input '*.txt' \
                    --input 'otherfiles/*.txt' \
                    --names --dates --addresses --phones --genders \
                    --concept 'kids' \
                    --output 'files/' --stats stdout

