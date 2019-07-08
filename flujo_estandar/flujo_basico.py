# -*- coding: utf-8 -*-
import nltk.data
import re, string, unicodedata
import nltk
import spacy
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.util import ngrams
from nltk.stem.snowball import SnowballStemmer
nlp = spacy.load('es_core_news_md')
   
def lemmatize_words(words):
	
	text1=" ".join(words)
	new_words=[]
	for token in nlp(text1):
		new_words.append(token.lemma_)
	return new_words
def construye_diccionario(file):
	diccionario=[]
	for lineas in file.readlines():
		linea=lineas.split()
		linea[0]=linea[0].replace('_',' ')
		linea[0]=linea[0].replace('\n','')
		linea[1]=linea[1].replace('_',' ')
		linea[1]=linea[1].replace('\n',' ')
		diccionario.append(linea)
	return diccionario


def tokenize(text):
	texto2=text
	words = nltk.word_tokenize(texto2)
	return words
def to_lowercase(words):
    """Convert all characters to lowercase from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = word.lower()
        new_words.append(new_word)
    return new_words

def remove_punctuation(words):
    """Remove punctuation from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_words.append(new_word)
    return new_words

def remove_stopwords(words):
    """Remove stop words from list of tokenized words"""
    new_words = []
    for word in words:
        if word not in stopwords.words('spanish'):
            new_words.append(word)  
    return new_words
def identificar_stopwords(words):
    """Remove stop words from list of tokenized words"""
    new_words = []
    for word in words:
        if word in stopwords.words('spanish'):
            new_words.append(word)
    return new_words

def stem_words(words):
    """Stem words in list of tokenized words"""
    spanishStemmer=SnowballStemmer("spanish", ignore_stopwords=True)
    stems = []
    for word in words:
        stem = spanishStemmer.stem(word)
        stems.append(stem)
    return stems
def normalize(words):
    words = to_lowercase(words)
    words = remove_punctuation(words)
    
    return words
def ngram(words,n):
	output = list(ngrams(words, n))
	return output
archivo=open("Flujo_experimental_1/LLNcooperativa.txt",'r')
archivo6=open('Flujo_experimental_1/dataset.csv','w')
archivo7=open('Flujo_experimental_1/listadepalabras.txt','w')
listadenoticias = []
listadengrmas=[]
cuentaproduccion=0
for linea in archivo.readlines():
	lineas= tokenize(linea)
	lineas= normalize(lineas)
	lineas = remove_stopwords(lineas)
	lineas= lemmatize_words(lineas)
	lineas= stem_words(lineas)
	#lineas= ngram(lineas,3)
	listadenoticias.append(lineas)
	print(str(cuentaproduccion))
	cuentaproduccion=cuentaproduccion+1
for matriz in listadenoticias:
	for a1 in matriz:
		listadengrmas.append(a1)
lista_nueva = []
for indice in listadengrmas:
    if indice not in lista_nueva:
        lista_nueva.append(indice)
    	
for palabra in lista_nueva:
	archivo7.write(palabra)
	archivo7.write('\n')
topico=open("Flujo_experimental_1/topicos.txt",'r')
topicos=[]
for linea in topico.readlines():
	topicos.append(linea)
contador=0;
cuentalinea=1
for noticia in listadenoticias:
	archivo6.write(str(cuentalinea))
	archivo6.write(',')
	for ngr in lista_nueva:
		if ngr in noticia:
			archivo6.write('1,')
		else:
			archivo6.write('0,')
	archivo6.write(topicos[contador])
	cuentalinea=cuentalinea+1
	contador=contador+1
archivo.close()
archivo6.close()
archivo7.close()

