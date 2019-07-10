# -*- coding: utf-8 -*-
import nltk.data
import re, string, unicodedata
import nltk
import spacy
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.util import ngrams
from nltk.stem.snowball import SnowballStemmer
lemmaDiccionario = {}
def lemmatize(word):
   return lemmaDiccionario.get(word, word + u'')
   
def lemmatize_words(words,archivo1):
	#nlp = spacy.load('es_core_news_md')
	new_words = []
	lem_words = []
	for palabra in words:
		new_word = lemmatize(palabra)
		new_words.append(new_word)
	#for token in nlp(str(new_words)):
	#	lem_word = token.lemma_
	#	lem_words.append(lem_word)
	archivo1.write(str(new_words))
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


def tokenize(text,diccionario):
	texto2=text
	for palabra in diccionario:
		texto2=texto2.replace(palabra[0],palabra[1])
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
        new_word=new_word.replace('_','')
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
archivo=open("Trigrama2/LLNcooperativa.txt",'r')
archivo1=open("Trigrama2/lema1.txt",'w')
archivo2=open('Trigrama2/prueba_final.txt','w')
archivo3=open('Trigrama2/stopwords_final.txt','w')
archivo4=open('Trigrama2/prueba_de_matriz.txt','w')
archivo5=open('Trigrama2/listadengrmas.txt','w')
archivo6=open('Trigrama2/dataset.csv','w')
archivo7=open('Trigrama2/listadepalabras.txt','w')
archivo8=open("Trigrama2/diccionarioespañol.txt",'r')
with open('Trigrama2/diccionariolemmatization.txt', 'rb') as fichero:
	datos = (fichero.read().decode('utf8').replace(u'\r', u'').split(u'\n'))
	datos = ([avance.split(u'\t') for avance in datos])
for avance in datos:
   if len(avance) >1:
      lemmaDiccionario[avance[1]] = avance[0]
listadenoticias = []
listadengrmas=[]
diccionarios=construye_diccionario(archivo8)
numero=0
for linea in archivo.readlines():
	lineas= tokenize(linea,diccionarios)
	salida2=identificar_stopwords(lineas)
	lineas= normalize(lineas)
	lineas = remove_stopwords(lineas)
	#lineas= lemmatize_words(lineas,archivo1)
	lineas= stem_words(lineas)
	lineas= ngram(lineas,3)
	listadenoticias.append(lineas)
	archivo2.write(str(lineas))
	archivo2.write('\n')
	archivo3.write(str(salida2))
	archivo3.write('\n')
	print(str(numero))
	numero=numero+1
for matriz in listadenoticias:
	print("estoyjuntando")
	for a1 in matriz:
		listadengrmas.append(a1)
		archivo4.write(str(a1))
		archivo4.write('\n')
lista_nueva = []
for indice in listadengrmas:
    print("estoy filtrando")
    if indice not in lista_nueva:
        lista_nueva.append(indice)
    	
archivo5.write(str(listadengrmas))
for palabra in lista_nueva:
	print("estoyalmacenando")
	archivo7.write(str(palabra))
	archivo7.write('\n')
topico=open("Trigrama2/topicos.txt",'r')
topicos=[]
for linea in topico.readlines():
	topicos.append(linea)
contador=0;
cuentalinea=1
for noticia in listadenoticias:
	print("estoyescribiendo")
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
archivo2.close()
archivo3.close()
archivo4.close()
archivo5.close()
archivo6.close()
archivo7.close()

