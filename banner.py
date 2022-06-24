import pygame #importo librería
from constantes import * #importo constantes
from pygame import font
from pygame.font import Font

class Banner(pygame.sprite.Sprite): #defino la clase banner
    def __init__(self): #constructor de la clase
        pygame.sprite.Sprite.__init__(self) #llamo al constructor de la clase padre

        self.image=pygame.Surface([ancho_ventana,alto_banner]) #creo superficie
        self.image.fill(color_banner) #color de banner
        self.rect=self.image.get_rect() #obtengo rectángulo de la superficie
        self.rect.y=0 #posición en y
        self.rect.x=0 #posición en x
        self.fuente=pygame.font.match_font(fuente)

    def dibujar(self,superficie): #dibujo el banner
        superficie.blit(self.image,self.rect) #dibujo la superficie

    def formato_puntaje(self,puntaje):
        return "Puntaje: {}".format(puntaje)

    def formato_nivel(self,nivel):
        return "Nivel: {}".format(nivel)

    def mostrar_texto(self,texto,tamaño,color,x,y,superficie):
        fuente=Font(self.fuente,tamaño)
        texto=fuente.render(texto,True,color)
        rectángulo=texto.get_rect()
        rectángulo.midtop=(x,y)
        superficie.blit(texto,rectángulo)

    def dibujar_texto(self,superficie,puntaje,nivel):
        self.mostrar_texto(self.formato_puntaje(puntaje),24,color_techo,ancho_ventana//2,0,superficie)
        self.mostrar_texto(self.formato_nivel(nivel),24,color_techo,60,0,superficie)
        if not juego:
            self.mostrar_texto('PERDISTE!',50,color_techo,ancho_ventana//2,alto_ventana//2)
            self.mostrar_texto('Presiona r para reiniciar el juego',25,color_techo,ancho_ventana//2,alto_ventana//2+50)