import os

ancho_ventana = 800
alto_ventana = 600
alto_piso=25
alto_techo=5
alto_banner=30
ancho_jugador=120
alto_jugador=120
ancho_pelota=20
alto_pelota=20
ancho_bloque=30
alto_bloque=30

color_fondo = (100, 140, 120)
color_piso = (200, 210, 220)
color_techo = (250, 250, 250)
color_banner = (20, 20, 20)
color_jugador = (255, 0, 0)
color_pelota = (0, 0, 255)
color_bloque = (0, 255, 0)

velocidad_jugador = 5
velocidad_pelota = 2

fuente="Arial"

puntaje=0
puntaje_máximo=0
nivel=1
nivel_máximo=1
juego=False
jugando=True
vidas=3
pausa=False
ganador=False

dir=os.path.dirname(__file__)
dirSonidos=os.path.join(dir,'Sonidos')
dirImágenes=os.path.join(dir,'Imágenes')