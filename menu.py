import pygame
from constantes import *
import sys
from texto import Texto #importo clase banner

class Menu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image=pygame.Surface([ancho_ventana,alto_ventana]) #creo superficie
        self.image.fill(color_fondo) #color de fondo
        self.rect=self.image.get_rect()
        self.rect.y=0
        self.rect.x=0
        self.texto=Texto()

    def dibujar(self,superficie,puntaje):
        superficie.blit(self.image,self.rect)
        self.texto.mostrar_texto('Ayuda a Cody a limpiar su casa de las arañas!',33,color_banner,ancho_ventana//2,10,superficie,None)
        self.texto.mostrar_texto('Con la flecha arriba inicia el juego',33,color_banner,ancho_ventana//2,60,superficie,None)
        self.texto.mostrar_texto('Con las flechas laterales mueves a Cody',33,color_banner,ancho_ventana//2,110,superficie,None)
        self.texto.mostrar_texto('El puntaje a superar es: {}'.format(puntaje),33,color_banner,ancho_ventana//2,160,superficie,None)
        self.texto.mostrar_texto('Presiona cualquier tecla para continuar',33,color_banner,ancho_ventana//2,210,superficie,None)
        pygame.display.flip()
        self.esperar()

    def esperar(self):
        esperar=True
        reloj=pygame.time.Clock() #creo reloj
        while esperar:
            reloj.tick(60)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    esperar=False
                    self.ejecutando=False
                    pygame.quit()
                    sys.exit()
                if evento.type==pygame.KEYUP:
                    esperar=False