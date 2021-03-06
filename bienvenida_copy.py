import pygame
from pygame import time
from constantes import *
import sys
from texto import Texto #importo clase banner
from jugador import Jugador

class Bienvenida_2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image=pygame.image.load(os.path.join(dirImágenes,'fondo_menu.jpg')) #creo superficie
        self.imagen_piso=pygame.image.load(os.path.join(dirImágenes,'piso_menu.jpg'))
        self.imágenes_flechas=(
            pygame.image.load(os.path.join(dirImágenes,'tecla_arr.png')),
            pygame.image.load(os.path.join(dirImágenes,'tecla_izq.png')),)
        self.imagen_flecha=self.imágenes_flechas[0]
        self.rect=self.image.get_rect()
        self.rect_piso=self.imagen_piso.get_rect()
        self.rect_flecha=self.imagen_flecha.get_rect()
        self.rect.y=0
        self.rect.x=0
        self.rect_piso.y=alto_ventana-147
        self.rect_piso.x=0
        self.rect_flecha.y=alto_ventana-147
        self.rect_flecha.x=ancho_ventana//2+ancho_ventana//4
        self.texto=Texto()
        self.jugador=Jugador()

    def dibujar(self,superficie,puntaje):
        superficie.blit(self.image,self.rect)
        superficie.blit(self.imagen_piso,self.rect_piso)
        self.texto.mostrar_texto('Ayuda a Cody a limpiar su casa de las arañas!',33,color_techo,ancho_ventana//2,10,superficie,None)
        self.texto.mostrar_texto('Con la flecha arriba inicia el juego',33,color_techo,ancho_ventana//2,60,superficie,None)
        self.texto.mostrar_texto('Con las flechas laterales mueves a Cody',33,color_techo,ancho_ventana//2,110,superficie,None)
        self.texto.mostrar_texto('El puntaje a superar es: {}'.format(puntaje),33,color_techo,ancho_ventana//2,160,superficie,None)
        self.texto.mostrar_texto('Presiona cualquier tecla para continuar',33,color_techo,ancho_ventana//2,210,superficie,None)
        pygame.display.flip()
        self.animación(self.imágenes_jugador,self.imágenes_araña,self.rect_jugador,self.rect_araña,superficie)

    def esperar(self):
        esperar=True
        reloj=pygame.time.Clock() #creo reloj
        reloj.tick(60)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                esperar=False
                self.ejecutando=False
                pygame.quit()
                sys.exit()
            if evento.type==pygame.KEYUP:
                esperar=False
        return esperar

    def animación(self,imágenes_1,imágenes_2,rectángulo_1,rectángulo_2,superficie):
        esperar=True
        while esperar:
            superficie.blit(self.imagen_piso,self.rect_piso)
            superficie.blit(imágenes_1[0],rectángulo_1)        #dibujo la imagen
            superficie.blit(imágenes_2[0],rectángulo_2)        #dibujo la imagen
            time.wait(300)
            pygame.display.flip()
            superficie.blit(self.imagen_piso,self.rect_piso)
            superficie.blit(imágenes_1[1],rectángulo_1)        #dibujo la imagen
            superficie.blit(imágenes_2[1],rectángulo_2)        #dibujo la imagen
            time.wait(300)
            pygame.display.flip()
            esperar=self.esperar()