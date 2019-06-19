from wiktionaryparser import WiktionaryParser
from pattern.es import parse,tag
from pattern.web import Wiktionary

diccionario={}
teclado=input()
web = Wiktionary(language="es")
articulo = web.search(teclado)#PALABRA
if articulo is not None:
	s = list(filter(lambda x: x.title=="Español", articulo.sections))  #esto se debe hacer si articulo is not none
	etimologia = list(filter(lambda x: x.title=="Etimología", s[0].children))
	definicion=etimologia[0].content #DEFINICION  #si la palabra es plural la proceso antes de descartarla
	lista = ["Adjetivo","Verbo","Verbo intransitivo","Forma verbal","Verbo transitivo","Forma adjetiva","Sustantivo","Sustantivo masculino","Sustantivo femenino"]
	lista_verbos=["Verbo","Verbo intransitivo","Forma verbal","Verbo transitivo"]
	lista_sustantivos=["Sustantivo","Sustantivo masculino","Sustantivo femenino"]
	lista_adjetivos=["Adjetivo","Forma Adjetiva"]
	for tipo in lista:
		tipo_real = list(filter(lambda x: x.title==tipo, s[0].children))
		if tipo_real:
			clasificacion=tipo
	print(clasificacion)
	if clasificacion in lista_adjetivos: 
		clasificacion="Adjetivo"
	elif clasificacion in lista_sustantivos:
		clasificacion="Sustantivo"
	elif clasificacion in lista_verbos:
		clasificacion="Verbo"      
								   #aca no se cual sería la mejor forma de hacerlo
								   #puede que lo mejor sea un popup que diga palabra invalida, que no diga palabra invalida que diga otra cosa



teclado={"Palabra":teclado,"Definición":definicion,"Tipo":clasificacion}
print(teclado)
diccionario.update(teclado)
print(diccionario)
def de_pattern(teclado):
	palabra_tipo=tag(teclado,tokenize=True, encoding="utf-8")
	if palabra_tipo[0][1]=="NN":
		palabra_tipo=[teclado,"Sustantivo"]
	elif palabra_tipo[0][1]=="VB":
		palabra_tipo=[teclado,"Verbo"]
	elif palabra_tipo[0][1]=="JJ":
		palabra_tipo=[teclado,"Adjetivo"]
	else:
		palabra_tipo[0][1]="error" #preguntar por esto	
	return palabra_tipo
palabra_tipo=de_pattern("correr")
print(palabra_tipo)








#unificar los tipos dados por pattern y los tipos dados por wik y comparar
#de ahi salen los reportes
#
#guardar las palabras validad en una dicc
#hacer que sean por teclado
#
#exepciones
