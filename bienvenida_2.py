import pygame
from pygame import time
from constantes import *
import sys
from texto import Texto #importo clase banner
from jugador import Jugador
from pelota import Pelota
from piso import Piso

class Bienvenida_2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image=pygame.image.load(os.path.join(dirImágenes,'fondo_menu.jpg')) #creo superficie
        self.imagen_piso=pygame.image.load(os.path.join(dirImágenes,'piso_menu.jpg'))
        self.imágenes_flechas=(
            pygame.image.load(os.path.join(dirImágenes,'teclas.png')),
            pygame.image.load(os.path.join(dirImágenes,'tecla_arr.png')),)
        self.imagen_flecha=self.imágenes_flechas[0]
        self.rect=self.image.get_rect()
        self.rect_piso=self.imagen_piso.get_rect()
        self.rect_flecha=self.imagen_flecha.get_rect()
        self.rect.y=0
        self.rect.x=0
        self.rect_piso.y=alto_ventana-221
        self.rect_piso.x=0
        self.rect_flecha.y=alto_ventana-121
        self.rect_flecha.x=ancho_ventana//2+ancho_ventana//4
        self.texto=Texto()
        self.jugador=Jugador()
        self.pelota=Pelota()
        self.piso=Piso()

    def dibujar(self,superficie):
        superficie.blit(self.image,self.rect)
        superficie.blit(self.imagen_piso,self.rect_piso)
        self.texto.mostrar_texto('Ayuda a Cody a limpiar su casa de las arañas!',33,color_banner,ancho_ventana//2+2,10,superficie,None)
        self.texto.mostrar_texto('Ayuda a Cody a limpiar su casa de las arañas!',33,color_techo,ancho_ventana//2,10,superficie,None)
        self.texto.mostrar_texto('Con la flecha arriba inicia el juego',33,color_banner,ancho_ventana//2+2,60,superficie,None)
        self.texto.mostrar_texto('Con la flecha arriba inicia el juego',33,color_techo,ancho_ventana//2,60,superficie,None)
        self.texto.mostrar_texto('Presiona cualquier tecla para continuar',33,color_banner,ancho_ventana//2+2,110,superficie,None)
        self.texto.mostrar_texto('Presiona cualquier tecla para continuar',33,color_techo,ancho_ventana//2,110,superficie,None)
        self.jugador.dibujar_nuevamente(superficie)
        self.pelota.dibujar(superficie)
        self.piso.dibujar(superficie)
        pygame.display.flip()        
        self.animación(self.imágenes_flechas,self.rect_flecha,superficie)

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

    def animación(self,imágenes,rectángulo,superficie):
        esperar=True
        while esperar:
            superficie.blit(self.imagen_piso,self.rect_piso)
            self.piso.dibujar(superficie)
            self.jugador.dibujar_nuevamente(superficie)
            self.pelota.dibujar_nuevamente(superficie)
            superficie.blit(imágenes[0],rectángulo)        #dibujo la imagen
            pygame.display.flip()
            time.wait(1000)            
            superficie.blit(self.imagen_piso,self.rect_piso)
            for i in range(35):
                pygame.display.flip()
                superficie.blit(self.imagen_piso,self.rect_piso)
                self.piso.dibujar(superficie)
                self.pelota.subir(velocidad_pelota)
                self.pelota.derecha(velocidad_pelota)
                superficie.blit(self.pelota.image,self.pelota.rect)
                self.jugador.dibujar_nuevamente(superficie)
                time.wait(10)
                if i <20:
                    superficie.blit(imágenes[1],rectángulo)        #dibujo la imagen
                else:
                    superficie.blit(imágenes[0],rectángulo)
            pygame.display.flip()
            time.wait(100)            
            esperar=self.esperar()