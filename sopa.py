import sys
import PySimpleGUI as sg
import random
import string
import funciones_SOPA as fs
import configuracion as cnfig
import funciones_AYUDA as fa
import Wik_y_pattern as wp

"""
    Abre la ventana de Configuración al comenzar, permite configurar todos los valores y al cerrarla
    genera la sopa de letras acorde a los valores ingresados y se asegura de que sea jugable.
    Aún no están bien implementadas las muestras de ayuda ni la corrección de las palabras coloreadas
    al presionar "Corregir".

"""

datos_configurados = cnfig.Config()
#palabras_validas = datos_configurados['palabras']
#print(palabras_validas)
filas_validas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
columnas_validas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

BOX_SIZE = 25

if datos_configurados['ayuda']['sin_ayuda']:
    ayuda_layout=fa.sin_ayuda(datos_configurados['diccionario'])
elif datos_configurados['ayuda']['definiciones']:
    ayuda_layout=fa.mostrar_defi(datos_configurados['diccionario'])
elif datos_configurados['ayuda']['palabras']:
    ayuda_layout=fa.mostrar_pal(datos_configurados['diccionario'])
else:
    ayuda_layout=fa.mostrar_defi_pal(datos_configurados['diccionario'])

#ayuda_layout_general = [sg.Frame('Ayuda', ayuda_layout, font='Any 10', title_color='cadet blue')]

#if ayuda['sin_ayuda']:
#    ayuda_layout = fa.sin_ayuda(datos_configurados['palabras'])
#elif ayuda['con_definiciones']:
#    ayuda_layout = fa.mostrar_defi(datos_configurados['palabras'])
#elif ayuda['con_palabras']:
#    ayuda_layout = fa.mostrar_pal(datos_configurados['palabras'])
#else:
#    ayuda_layout = [[fa.mostrar_pal(datos_configurados['palabras'])],[fa.mostrar_defi(datos_configurados['palabras'])]]

#Intenté darle un valor al color del botón pero hay un problema con las librerías, por lo que lo dejé con el color por default
botones_color_layout = [
                  [sg.DummyButton("Sustantivos", key='color_Sustantivo')], [sg.DummyButton("Adjetivos", key='color_Adjetivo')], [sg.DummyButton("Verbos", key='color_Verbo')]
               ]

layout = [
            [sg.Graph((600,600), (0,400), (450,0), key='_GRAPH_', change_submits=True, drag_submits=False), 
             sg.Frame('Colores disponibles', botones_color_layout, font='Any 10', title_color='cadet blue')],
            [sg.Frame('Ayuda', ayuda_layout, font='Any 10', title_color='cadet blue')],
            [sg.Button('Corregir'), sg.Button('Exit')]
         ]

window = sg.Window('Sopa de letras educativa', ).Layout(layout).Finalize()

g = window.FindElement('_GRAPH_')

letras=[[j for j in range(16)]for i in range(16)]
colores=[[j for j in range(16)]for i in range(16)]

	

for row in range(16):
    for col in range(16):
            g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black')
            location= (col * BOX_SIZE + 18, row * BOX_SIZE + 17)
            if datos_configurados['tipografia']['caps'] =="mayuscula":
                letra = '{}'.format(random.choice(string.ascii_uppercase))
            if datos_configurados['tipografia']['caps'] =="minuscula":
                letra = '{}'.format(random.choice(string.ascii_lowercase))
            g.DrawText(letra,location , font=datos_configurados['tipografia']['font'])
            letras[row][col]=letra ## se llena segun la orientacion
            colores[row][col]=""   ## se llena segun la orientacion

if datos_configurados['orientacion'] =="vertical":
    for palabra in datos_configurados['palabras']:
        columnas_validas=fs.insertar_palabra_vertical(BOX_SIZE,palabra,letras,g,columnas_validas,datos_configurados['tipografia']['font'])
else:
    for palabra in datos_configurados['palabras']:
        filas_validas=fs.insertar_palabra_horizontal(BOX_SIZE,palabra,letras,g,filas_validas,datos_configurados['tipografia']['font'])
		
color_seleccionado = 'grey'
           
while True:             # Event Loop
    event, values = window.Read()
    print(event,"event")
    print(values,"values")
    print(event, values,)
    if event is None or event == 'Exit':
        break
    mouse = values['_GRAPH_']
    
#A continuación se asignaría el color que se utilizará al pintar las letras, en relación al botón que se presione,
#pero hay problemas con las librerías:

#    if event == 'Sustantivos':
#        color_seleccionado=color_S
#    if event == 'Adjetivos':
#        color_seleccionado=color_A
#    if event == 'Verbos':
#        color_seleccionado=color_V
    if event == '_GRAPH_':
        if mouse == (None, None):
            continue
        box_x = mouse[0]//BOX_SIZE
        box_y = mouse[1]//BOX_SIZE
        arriba_izq = (box_x * BOX_SIZE +5, box_y * BOX_SIZE +3 )
        abajo_derecha=(box_x * BOX_SIZE +30, box_y * BOX_SIZE +28)
        letter_location = (box_x * BOX_SIZE + 18, box_y * BOX_SIZE + 17)
        #print(box_x, box_y)
        if (colores[box_y][box_x]=="spring green"):
            g.DrawRectangle(top_left=arriba_izq,bottom_right=abajo_derecha, line_color='black',fill_color="grey")
            g.DrawText('{}'.format(letras[box_y][box_x]), letter_location, font=datos_configurados['tipografia']['font']) # aca tambien se modifica la font
            colores[box_y][box_x]="grey"
        else:
            g.DrawRectangle(top_left=arriba_izq,bottom_right=abajo_derecha, line_color='black',fill_color="spring green")#aca se cmbia el color segun los 3 colores
            g.DrawText('{}'.format(letras[box_y][box_x]), letter_location, font=datos_configurados['tipografia']['font'])  					#la font tambien es una variable y se modifica  
            colores[box_y][box_x]="spring green"
        #NOTA: Se utiliza el color "spring green" en lugar del parámetro que recibe el color seleccionado por problemas
        #con las librerías.
    #El evento de Corrección no funciona correctamente por problemas con "index out of range" dentro del módulo funciones_SOPA:
    if event is 'Corregir':
        if datos_configurados['orientacion'] =="vertical":
            for i in datos_configurados['palabras']:
                if fs.procesar_vertical(letras,colores,'vertical',datos_configurados['colores'])[i][0] in datos_configurados['palabras']:
                    if fs.procesar_vertical(letras,colores,'vertical',datos_configurados['colores'])[i][1] == wp.de_pattern(i):
                        sg.PopupOK('Acertaste la palabra' + i + ' y el tipo de palabra.')
                    else:
                        sg.PopupOK('Acertaste la palabra' + i + ' pero no el tipo de palabra.')
                else:
                    sg.PopupOK('No acertaste la palabra ' + i)       
        if datos_configurados['orientacion'] =="horizontal":
            for i in datos_configurados['palabras']:
                if fs.procesar_horizontal(letras,colores,'horizontal',datos_configurados['colores'])[i][0] in datos_configurados['palabras']:
                    if fs.procesar_horizontal(letras,colores,'horizontal',datos_configurados['colores'])[i][1] == wp.de_pattern(i):
                        sg.PopupOK('Acertaste la palabra' + i + ' y el tipo de palabra.')
                    else:
                        sg.PopupOK('Acertaste la palabra' + i + ' pero no el tipo de palabra.')
                else:
                    sg.PopupOK('No acertaste la palabra ' + i)
        break
window.Close()
