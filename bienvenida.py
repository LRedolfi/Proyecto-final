import pygame
from pygame import time
from constantes import *
import sys
from texto import Texto #importo clase banner

class Bienvenida(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image=pygame.image.load(os.path.join(dirImágenes,'fondo_menu.jpg')) #creo superficie
        self.imagen_piso=pygame.image.load(os.path.join(dirImágenes,'piso_menu.jpg'))
        self.imágenes_jugador=(
            pygame.image.load(os.path.join(dirImágenes,'arriba_izq.png')),
            pygame.image.load(os.path.join(dirImágenes,'jugador.png')),)
        self.imágenes_araña=(
            pygame.image.load(os.path.join(dirImágenes,'araña_abajo.png')),
            pygame.image.load(os.path.join(dirImágenes,'araña_arriba.png')),)
        self.imagen_jugador=self.imágenes_jugador[0]
        self.imagen_araña=self.imágenes_araña[0]
        self.rect=self.image.get_rect()
        self.rect_piso=self.imagen_piso.get_rect()
        self.rect_jugador=self.imagen_jugador.get_rect()
        self.rect_araña=self.imagen_araña.get_rect()
        self.rect.y=0
        self.rect.x=0
        self.rect_piso.y=alto_ventana-221
        self.rect_piso.x=0
        self.rect_jugador.y=alto_ventana-alto_jugador
        self.rect_jugador.x=ancho_ventana//2-ancho_jugador//2
        self.rect_araña.y=alto_ventana-221
        self.rect_araña.x=ancho_ventana//2+ancho_ventana//4
        self.texto=Texto()

    def dibujar(self,superficie):
        superficie.blit(self.image,self.rect)
        superficie.blit(self.imagen_piso,self.rect_piso)
        self.texto.mostrar_texto('Oh, no! Las arañas están invadiendo la casa de Cody!',33,color_banner,ancho_ventana//2+2,10+2,superficie)
        self.texto.mostrar_texto('Oh, no! Las arañas están invadiendo la casa de Cody!',33,color_techo,ancho_ventana//2,10,superficie)
        self.texto.mostrar_texto('Quieres ayudar a Cody a limpiar su casa de las arañas?',33,color_banner,ancho_ventana//2+2,50+2,superficie)
        self.texto.mostrar_texto('Quieres ayudar a Cody a limpiar su casa de las arañas?',33,color_techo,ancho_ventana//2,50,superficie)
        self.texto.mostrar_texto('Presiona cualquier tecla para continuar',33,color_banner,ancho_ventana//2+2,100+2,superficie)
        self.texto.mostrar_texto('Presiona cualquier tecla para continuar',33,color_techo,ancho_ventana//2,100,superficie)
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