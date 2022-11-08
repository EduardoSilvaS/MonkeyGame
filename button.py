import pygame

class button():
    def __init__(self, color, x,y,width,height,font_size=15,font_family="timesnewroman",font_color=(0,0,0), text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font_color = font_color
        self.font_size = font_size
        self.font_family = font_family

    def draw(self,win,outline=None,size=1):
        # call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-size,self.y-size,self.width+(size*2),self.height+(size*2)),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont(self.font_family, self.font_size)
            text = font.render(self.text, 1, self.font_color)
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def is_over(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False