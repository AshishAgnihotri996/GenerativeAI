#paragrapg below
# corpus ="""hello welcome to ashish agnihotri tutotrials, please do watch the entire course to become expert in NLP."""
# print(corpus)

# sentence to paragraph
from nltk.tokenize import sent_tokenize
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')

corpus = """hello welcome to ashish agnihotri tutorials. please do watch the entire course! to become expert in NLP."""

sentences = sent_tokenize(corpus)
print(sentences)

#paragraph into words

#sentence into words

from nltk.tokenize import word_tokenize, wordpunct_tokenize

d =word_tokenize(corpus)
print(d)

b =wordpunct_tokenize(corpus)
print(b)

from nltk import TreebankWordTokenizer

tk = TreebankWordTokenizer()
c =tk.tokenize(corpus)
print(c)
