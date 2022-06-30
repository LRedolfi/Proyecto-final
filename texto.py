import pygame #importo librería
from constantes import * #importo constantes
from pygame import font
from pygame.font import Font

class Texto(pygame.sprite.Sprite): #defino la clase texto
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

    def formato_vidas(self,vidas):
        return "Vidas: {}".format(vidas)

    def formato_record(self,puntaje_máximo):
        return "Récord: {}".format(puntaje_máximo)

    def mostrar_texto(self,texto,tamaño,color,x,y,superficie,f):
        fuente=Font(self.fuente,tamaño)
        texto=fuente.render(texto,True,color,f)
        rectángulo=texto.get_rect()
        rectángulo.midtop=(x,y)
        superficie.blit(texto,rectángulo)

    def dibujar_texto(self,superficie,puntaje,nivel,jugando,vidas,pausa,ganador,puntaje_máximo):
        self.mostrar_texto(self.formato_puntaje(puntaje),24,color_techo,ancho_ventana//2+100,0,superficie,None)
        self.mostrar_texto(self.formato_nivel(nivel),24,color_techo,60,0,superficie,None)
        self.mostrar_texto(self.formato_vidas(vidas),24,color_techo,750,0,superficie,None)
        self.mostrar_texto(self.formato_record(puntaje_máximo),24,color_techo,ancho_ventana//2-100,0,superficie,None)
        self.mostrar_texto('Para pausar el juego presiona P',24,color_banner,ancho_ventana//2,alto_ventana-30,superficie,None)
        if not jugando and vidas>0:
            self.mostrar_texto('Perdiste una vida!',50,color_techo,ancho_ventana//2,alto_ventana//2,superficie,color_fondo)
            self.mostrar_texto('Presiona r para continuar el juego',25,color_techo,ancho_ventana//2,alto_ventana//2+50,superficie,color_fondo)
        if not jugando and vidas==0:
            self.mostrar_texto('PERDISTE!',50,color_techo,ancho_ventana//2,alto_ventana//2,superficie,color_fondo)
            self.mostrar_texto('Presiona r para reiniciar el juego',25,color_techo,ancho_ventana//2,alto_ventana//2+50,superficie,color_fondo)
        if pausa:
            self.mostrar_texto('Juego pausado',50,color_techo,ancho_ventana//2,alto_ventana//2,superficie,color_fondo)
            self.mostrar_texto('Presiona r para continuar el juego',25,color_techo,ancho_ventana//2,alto_ventana//2+60,superficie,color_fondo)
        if ganador and vidas==0:
            self.mostrar_texto('Felicidades! Tu puntaje {} fue el mas alto!'.format(puntaje),25,color_techo,ancho_ventana//2,alto_ventana//2+85,superficie,color_fondo)
        if not ganador and vidas==0:
            self.mostrar_texto('Tu puntaje no supero el puntaje máximo de {}'.format(puntaje_máximo),25,color_techo,ancho_ventana//2,alto_ventana//2+85,superficie,color_fondo)