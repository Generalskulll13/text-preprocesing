# -*- coding: utf-8 -*-
import nltk.data
import re, string, unicodedata
import nltk
import spacy
import threading
import time
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.util import ngrams
from nltk.stem.snowball import SnowballStemmer
import spacy
cuentahebra=0
listadenoticias = []
def lemmatize_words(words):
	nlp = spacy.load('es_core_news_md')
	text1=" ".join(words)
	new_words=[]
	for token in nlp(text1):
		new_words.append(token.lemma_)
	return new_words
def tokenize(text):
	words = nltk.word_tokenize(text)
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
class myThread (threading.Thread):
	def __init__(self, threadID, name, counter,linea,nhebra):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
		self.linea=linea
		self.nhebra=nhebra
	def run(self):
		multithread(self.linea, self.nhebra)
    	# Free lock to release next thread

def multithread(linea,nhebra):
	global cuentahebra
	lineas= lemmatize_words(linea)
	lineas= stem_words(lineas)
	print("entre a la hebra")
	print(str(cuentahebra))
	#lineas= ngram(lineas,3)
	print("hola")
	while nhebra!= cuentahebra:
		print(str(nhebra))
	global listadenoticias
	listadenoticias.append(lineas)
	print(len(listadenoticias))
	cuentahebra = cuentahebra+1
	return listadenoticias
def main():
	global listadenoticias
	inicio=time.time()
	archivo=open("flujo_estandar/LLNcooperativa.txt",'r')
	archivo6=open('flujo_estandar/dataset.csv','w')
	archivo7=open('flujo_estandar/listadepalabras.txt','w')
	listadengrmas=[]
	contador=0
	nhebra=0
	threads = []
	for linea in archivo.readlines():
		lineas= tokenize(linea)
		lineas= normalize(lineas)
		lineas = remove_stopwords(lineas)
		thread1 = myThread(1, "Thread", 1,lineas,nhebra)
		thread1.start()
		nhebra=nhebra+1
		threads.append(thread1)
	for t in threads:
   		t.join()

	for matriz in listadenoticias:
		for a1 in matriz:
			listadengrmas.append(a1)
	lista_nueva=[]
	for indice in listadengrmas:
		if indice not in lista_nueva:
			listadengrmas.append(indice)

	print(len(lista_nueva))
	print(len(listadengrmas))
	for palabra in lista_nueva:
		archivo7.write(palabra)
		archivo7.write('\n')
	topico=open("flujo_estandar/topicos.txt",'r')
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
	print(str(time.time()-inicio))
if __name__ == "__main__":
    main()

