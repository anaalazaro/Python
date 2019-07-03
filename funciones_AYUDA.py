import sys
import PySimpleGUI as sg
	
def sin_ayuda(diccionario):
    cantSustantivos=0
    cantVerbos=0
    cantAdjetivos=0
    for k,v in diccionario.items():
        if v['Tipo']=='Sustantivo':
            cantSustantivos+=1
        if v['Tipo']=='Adjetivo':
            cantAdjetivos+=1
        if v['Tipo']=='Verbo':
            cantVerbos+=1
    layout=[[sg.Text('Cantidad de palabras a encontrar: ')],
	        [sg.T('Cantidad de adjetivos: '+ str(cantAdjetivos)) ],
	        [sg.T('Cantidad de Verbos:  '+ str(cantVerbos))],
	        [sg.T('Cantidad de Susutantivos: '+ str(cantSustantivos))],
	        [sg.Button('Ok')]
	]
    return layout

def mostrar_defi(diccinario):
    defi=""
    for i,j in diccionario.items():
        defi=defi+ '\n' + j['Definición']
        
           
    layout=[[sg.T('Definiciones de las palabras a encontrar:  '+ str(defi))],
       ]
    return layout
    
     
def mostrar_pal(diccionario):
    pal=""
    for i,j in diccionario.items():
       pal=pal+'\n'+i
        
           
    layout=[[sg.T('Palabras a encontrar:  '+ str(pal))],
       ]
    return layout

def mostrar_defi_pal(diccionario):
    ayuda=""
    for i,j in diccionario.items():
        ayuda= ayuda + '\n'+ i +':'+j['Definición']
    print(ayuda)
    
    layout=[[sg.T('Palabras a encontrar:  '+ str(ayuda))],
       ]
    return layout
