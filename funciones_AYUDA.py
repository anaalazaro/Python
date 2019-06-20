import sys
import PySimpleGUI as sg
	
def sin_ayuda(palabras):
    cantAdjetivos=len(palabras['cantAdjetivos'])
    cantVerbos= len(palabras['cantVerbos'])
    cantSustantivos=len(palabras['cantSustantivos'])
	
    layout=[[sg.Text('Cantidad de palabras a encontrar: ')],
	        [sg.T('Cantidad de adjetivos: '+ str(cantAdjetivos)) ],
	        [sg.T('Cantidad de Verbos:  '+ str(cantVerbos))],
	        [sg.T('Cantidad de Susutantivos: '+ str(cantSustantivos))],
	        [sg.Button('Ok')]]

    return layout

def mostrar_defi(palabras):
    dic={}
    for i in palabras.values():
	    for e in i:
             defi= input('Ingrese una definicion para '+ e+': ')
             dic[e]=defi	
    defi=""
    for d in dic.values():
        defi=defi+'\n'+d
           
    layout=[[sg.T('Definiciones de las palabras a encontrar:  '+ str(defi))]
       ]
    return layout
     
	
def mostrar_pal(palabras):
    pal=""
    for i in palabras.values():
       p= ','.join(i)
       pal=pal+','+p
        
           
    layout=[[sg.T('Palabras a encontrar:  '+ str(pal))],
       ]
    return layout
