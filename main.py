from random import randint
from banana import banana as bn
from button import button as btn
from upgrades import upgrades as up

import pygame as pg
import os
import time

def main():
    # definir constantes importantes
    WIDTH, HEIGHT = 800, 500
    WIN = pg.display.set_mode((WIDTH, HEIGHT))
        # carregar e redimensionar a imagem de backgorund
    BG = pg.transform.scale(pg.image.load(os.path.join("assets", "backgroundmonke.jpg")), (WIDTH, HEIGHT))


    # funcionamento do loop principal
    running = True
    LPS = 60 # loops per second
    clock = pg.time.Clock()

    main_font = pg.font.SysFont("comicsansms", 30) # fonte principal


    # variaveis para objetos do jogo
    mine_area = 200
    bn_mine = bn(WIDTH / 2 - mine_area / 2, HEIGHT / 2 - mine_area / 2)
    dinheiro = 1000

    # funcionamento dos upgrades
    click = up(1, 250)

    auto_click = 0

    # botoes
    off = (255,255,0)
    on = (204,204,0)

    TAMANHO = (80, 25)


    upgrades = {
        "click" : btn(off, WIDTH - TAMANHO[0] - 50, HEIGHT/2, TAMANHO[0], TAMANHO[1], font_family="comicsansms", text=str("lvl " + str(click.lvl)))
    }


    
    def update_window(): # função para atualizar a tela sempre que acontecer alguma coisa
        WIN.blit(BG, (0,0))
        bn_mine.draw(WIN)

        # labels
        money_label = main_font.render(f"$ {dinheiro}", 1, (0,153,0))
        WIN.blit(money_label, (WIDTH - money_label.get_width() - 5,0))

        # botoes
        upgrades["click"].draw(WIN)

        pg.display.update()

    
    while running:
        clock.tick(LPS)
        update_window()

        if auto_click == 120:
            auto_click = 0
            dinheiro += 1
        
        for event in pg.event.get():
            mouse_pos = pg.mouse.get_pos()

            if event.type == pg.QUIT: # clicar no 'X' para fechar
                running = False

            if event.type == pg.MOUSEBUTTONDOWN:
                if pg.mouse.get_pressed()[0]:
                    if bn_mine.is_over(mouse_pos): # BANANA
                        bn_mine.img_size = (180,220)
                        dinheiro += click.hab
                    
                    if upgrades["click"].is_over(mouse_pos):
                        dinheiro = click.up_lvl(dinheiro)
                        upgrades["click"].text = str("lvl " + str(click.lvl))
                        print(click.hab)

                                    
            if event.type == pg.MOUSEBUTTONUP:
                bn_mine.img_size = (200,200)
            
            if event.type == pg.MOUSEMOTION:
                if upgrades["click"].is_over(mouse_pos):
                    upgrades["click"].color = on
                else:
                    upgrades["click"].color = off

        auto_click += 1


if __name__ == '__main__':
    pg.init() # iniciar pygame
    pg.font.init()  # iniciar fonte

    main()
    
    pg.quit() # finalizar