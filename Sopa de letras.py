import sys
import PySimpleGUI as sg
import random
import string

"""

    Genera la sopa de letras y se asegura de que sea jugable

"""


BOX_SIZE = 25


layout = [
            [sg.Text('Crossword Puzzle Using PySimpleGUI'), sg.Text('', key='_OUTPUT_')],
            [sg.Graph((600,600), (0,400), (450,0), key='_GRAPH_', change_submits=True, drag_submits=False)],
            [sg.Button('Show'), sg.Button('Exit')]
         ]

window = sg.Window('Window Title', ).Layout(layout).Finalize()

g = window.FindElement('_GRAPH_')

letras=[[j for j in range(16)]for i in range(16)]
colores=[[j for j in range(16)]for i in range(16)]

	

for row in range(16):
    for col in range(16):
            g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black')
            location= (col * BOX_SIZE + 18, row * BOX_SIZE + 17)
            letra = '{}'.format(random.choice(string.ascii_uppercase))
            g.DrawText(letra,location , font='Courier 25')
            letras[row][col]=letra ## se llena segun la orientacion 
            colores[row][col]=""   ## se llena segun la orientacion

if orientacion =="vertical":
	for palabra in palabras_validas:
		insertar_palabra_vertical(palabra,letras,g)
else: insertar_palabra_horizontal(palabra,letras,g)
           
while True:             # Event Loop
    event, values = window.Read()
    print(event,"event")
    print(values,"values")
    print(event, values,)
    if event is None or event == 'Exit':
        break
    mouse = values['_GRAPH_']

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
            g.DrawText('{}'.format(letras[box_y][box_x]), letter_location, font='Courier 25') # aca tambien se modifica la font
            colores[box_y][box_x]="grey"
        else:
            g.DrawRectangle(top_left=arriba_izq,bottom_right=abajo_derecha, line_color='black',fill_color="spring green")#aca se cmbia el color segun los 3 colores
            g.DrawText('{}'.format(letras[box_y][box_x]), letter_location, font='Courier 25')  					#la font tambien es una variable y se modifica  
            colores[box_y][box_x]="spring green"

		
window.Close()
