# -*- coding: utf-8 -*-
import nltk.data
import re, string, unicodedata
import nltk
import spacy
from nltk import word_tokenize

def tokenize(text):
	words = nltk.word_tokenize(text)
	return words
def remove_punctuation(words):
    """Remove punctuation from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_words.append(new_word)
    return new_words
archivo=open("LTcooperativa.txt",'r')
archivo2=open('topicos.txt','w')
new_words=[]
for linea in archivo.readlines():
	lineas= tokenize(linea)
	lineas= remove_punctuation(lineas)
	first =lineas[0]
	new_words.append(first)
	archivo2.write(str(first))
	archivo2.write('\n')
lista_nueva = []
contador_pais=0
contador_entretencion=0
contador_mundo=0
contador_econmia=0
contador_tecnologia=0
contador_sociedad=0
contarod_corporativo=0
contardor_cultura=0
for indice in new_words:
    if indice == 'País':
    	contador_pais=contador_pais+1
    if indice == 'Entretención':
    	contador_entretencion=contador_entretencion+1
    if indice == 'Mundo':
    	contador_mundo=contador_mundo+1
    if indice == 'Economía':
    	contador_econmia=contador_econmia+1
    if indice == 'Tecnología':
    	contador_tecnologia=contador_tecnologia+1
    if indice == 'Sociedad':
    	contador_sociedad=contador_sociedad+1
    if indice == 'Corporativo':
    	contarod_corporativo=contarod_corporativo+1
    if indice == 'Cultura':
    	contardor_cultura=contardor_cultura+1
    if indice not in lista_nueva:
    	lista_nueva.append(indice)
    	
print('País: ')
print(contador_pais)
print('\n')
print('Entretención: ')
print(contador_entretencion)
print('\n')
print('Mundo: ')
print(contador_mundo)
print('\n')
print('Economía: ')
print(contador_econmia)
print('\n')
print('Tecnología: ')
print(contador_tecnologia)
print('\n')
print('Sociedad: ')
print(contador_sociedad)
print('\n')
print('Corporativo: ')
print(contarod_corporativo)
print('\n')
print('Cultura: ')
print(contardor_cultura)
print('\n')
