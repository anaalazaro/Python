#!/usr/bin/env python
import sys
import PySimpleGUI as sg



#palabras={'adjetivos':['bueno','malo','chico'],'verbos':['cantar','bailar','caminar'],'sustantivos':['montaña','casa','parque']}
#datos=["adjetivos","verbos","sustantivos"]
	
def sin_ayuda(palabras):
	cantAdjetivos=len(palabras['cantAdjetivos'])
	cantVerbos= len(palabras['cantVerbos'])
	cantSustantivos=len(palabras['cantSustantivos'])
	
	layout=[[sg.Text('Cantidad de palabras a encontrar: ')],
	        [sg.T('Cantidad de adjetivos: '+ str(cantAdjetivos)) ],
	        [sg.T('Cantidad de Verbos:  '+ str(cantVerbos))],
	        [sg.T('Cantidad de Susutantivos: '+ str(cantSustantivos))],
	        [sg.Button('Ok')]
	]
	window=sg.Window('').Layout(layout)
	event, values = window.Read()
	if event=='Ok':
		window.Disappear()
		
	window.Close()
	
def mostrar_defi(palabras):
    dic={}
    for i in palabras.values():
	    for e in i:
             defi= input('ingrese una definicion para '+ e+': ')
             dic[e]=defi	
    defi=""
    for d in dic.values():
        defi=defi+'\n'+d
           
    layout=[[sg.T('Definiciones de las palabras a encontrar:  '+ str(defi))],
       ]
    window=sg.Window('').Layout(layout)
    event, values = window.Read()
    window.Close()
     
	
def mostrar_pal(palabras):
    pal=""
    for i in palabras.values():
       p= ','.join(i)
       pal=pal+','+p
        
           
    layout=[[sg.T('Palabras a encontrar:  '+ str(pal))],
       ]
    window=sg.Window('').Layout(layout)
    event, values = window.Read()
    window.Close()
			



layout = [[ sg.Text('Ayuda') ],
           [sg.Button('Sin ayuda')],
          [ sg.Button('Mostrar Palabras')],
          [sg.Button('Mostrar Definiciones')],
          [sg.Button('Salir')]]

window = sg.Window('Ayudas disponibles').Layout(layout)

while True:
    event, values = window.Read()
    if event is None or event== 'Salir':
        break
    if event == 'Sin ayuda':
        
        sin_ayuda(palabras)
    if event== 'Mostrar Palabras':
         mostrar_pal(palabras)
    
    if event=='Mostrar Definiciones':
         mostrar_defi(palabras)	
