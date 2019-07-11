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
    layout=[
	        [sg.Multiline('Cantidad de adjetivos: '+ str(cantAdjetivos)+ '\n'+'Cantidad de Verbos:  '+ str(cantVerbos)+'\n'+'Cantidad de Susutantivos: '+ str(cantSustantivos), disabled=True) ],
	        ]
    return layout

def mostrar_defi(diccionario):
    defi=""
    for i,j in diccionario.items():
        defi=defi+ '\n' + j['Definición']
        
           
    layout=[[sg.Multiline('Definiciones de las palabras a encontrar:  '+ str(defi), disabled=True)],
       ]
    return layout
    
     
def mostrar_pal(diccionario):
    pal=""
    for i,j in diccionario.items():
       pal=pal+'\n'+i
        
           
    layout=[[sg.Multiline('Palabras a encontrar:  '+ str(pal),disabled=True)],
       ]
    return layout

def mostrar_defi_pal(diccionario):
    ayuda=""
    for i,j in diccionario.items():
        ayuda= ayuda + '\n'+ i +':'+j['Definición']
    print(ayuda)
    
    layout=[[sg.Multiline('Palabras a encontrar:  '+ str(ayuda), disabled=True)],
       ]
    return layout
