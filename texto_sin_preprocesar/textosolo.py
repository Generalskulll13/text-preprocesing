# -*- coding: utf-8 -*-
import nltk.data
import re, string, unicodedata
import nltk
import spacy
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.util import ngrams
from nltk.stem.snowball import SnowballStemmer



def tokenize(text):
	texto2=text
	words = nltk.word_tokenize(texto2)
	return words

archivo=open("LLNcooperativa.txt",'r')
archivo6=open('dataset.csv','w')
archivo7=open('listadepalabras.txt','w')
listadenoticias = []
listadengrmas=[]
for linea in archivo.readlines():
	lineas= tokenize(linea)
	#lineas= ngram(lineas,3)
	listadenoticias.append(lineas)
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
topico=open("topicos.txt",'r')
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

