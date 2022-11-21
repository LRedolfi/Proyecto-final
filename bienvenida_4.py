from pickle import TRUE
import pygame
from pygame import time
from constantes import *
import sys
from texto import Texto #importo clase banner
from piso import Piso
from mariposa import Mariposa
from telaraña import Telaraña

class Bienvenida_4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image=pygame.image.load(os.path.join(dirImágenes,'fondo_menu.jpg')) #creo superficie
        self.imagen_piso=pygame.image.load(os.path.join(dirImágenes,'piso_menu.jpg'))
        self.imagen_telaraña=pygame.image.load(os.path.join(dirImágenes,'telaraña.png'))
        self.rect=self.image.get_rect()
        self.rect_piso=self.imagen_piso.get_rect()
        self.rect_telaraña=self.imagen_telaraña.get_rect()
        self.rect.y=0
        self.rect.x=0
        self.rect_piso.y=alto_ventana-221
        self.rect_piso.x=0
        self.rect_telaraña.y=alto_ventana-147
        self.rect_telaraña.x=ancho_ventana//2+ancho_ventana//4
        self.texto=Texto()
        self.piso=Piso()
        self.mariposa=Mariposa(630,70,ancho_bloque,alto_bloque)
        self.telaraña=Telaraña(740,160,ancho_bloque,alto_bloque)

    def dibujar(self,superficie):
        superficie.blit(self.image,self.rect)
        superficie.blit(self.imagen_piso,self.rect_piso)
        self.texto.mostrar_texto('Ayuda a Cody a limpiar su casa de las arañas!',33,color_banner,ancho_ventana//2+2,10+2,superficie)
        self.texto.mostrar_texto('Ayuda a Cody a limpiar su casa de las arañas!',33,color_techo,ancho_ventana//2,10,superficie)
        self.texto.mostrar_texto('Las mariposas son amigas de Cody!',33,color_banner,ancho_ventana//2+2,60+2,superficie)
        self.texto.mostrar_texto('Las mariposas son amigas de Cody!',33,color_techo,ancho_ventana//2,60,superficie)
        self.texto.mostrar_texto('Si las liberas obtienes una pelota extra!',33,color_banner,ancho_ventana//2+2,110+2,superficie)
        self.texto.mostrar_texto('Si las liberas obtienes una pelota extra!',33,color_techo,ancho_ventana//2,110,superficie)
        self.texto.mostrar_texto('Las arañas usarán telas para bloquearte. Ten cuidado!',33,color_banner,ancho_ventana//2+2,160+2,superficie)
        self.texto.mostrar_texto('Las arañas usarán telas para bloquearte. Ten cuidado!',33,color_techo,ancho_ventana//2,160,superficie)
        self.texto.mostrar_texto('Presiona cualquier tecla para continuar',33,color_banner,ancho_ventana//2+2,210+2,superficie)
        self.texto.mostrar_texto('Presiona cualquier tecla para continuar',33,color_techo,ancho_ventana//2,210,superficie)
        self.texto.mostrar_texto('Ah! y cada 10000 puntos obtienes una vida extra!',33,color_banner,ancho_ventana//2+2,510+2,superficie)
        self.texto.mostrar_texto('Ah! y cada 10000 puntos obtienes una vida extra!',33,color_techo,ancho_ventana//2,510,superficie)
        self.piso.dibujar(superficie)
        self.mariposa.dibujar(superficie)
        self.telaraña.dibujar(superficie)
        pygame.display.flip()
        esperar=True
        while esperar:
            pygame.display.flip()
            esperar=self.esperar()
        
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