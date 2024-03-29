from luma.led_matrix.device import max7219			#a pesar de tener instalado el luma, (o eso creo) no lo reconoce
from luma.core.interface.serial import spi, noop    #me debe estar falatando algo, por lo tanto no puedo probarlo
from luma.core.render import canvas					#              preguntar
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT,TINY_FONT, SINCLAIR_FONT, LCD_FONT

class Matriz:
	def __init__(self, numero_matrices=1, orientacion=0,
		rotacion=0, ancho=8, alto=8):
		self.font = [CP437_FONT, TINY_FONT, SINCLAIR_FONT,LCD_FONT]
		self.serial = spi(port=0, device=0, gpio=noop())
		self.device = max7219(self.serial, width=ancho, height=alto, cascaded=numero_matrices, rotate=rotacion)
	def mostrar_mensaje(self, msg, delay=0.1, font=1):
		show_message(self.device, msg, fill="white",font=proportional(self.font[font]),scroll_delay=delay)
matriz = Matriz(numero_matrices=2, ancho=16)
matriz.mostrar_mensaje("Python", delay=0.3)
