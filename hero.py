
class Hero():
    def __init__(self, image, x_coordinate, y_coordinate):
        self.is_alive = True
        self.img = image
        self.xcor = x_coordinate
        self.ycor = y_coordinate
    def show(self, game_display):
        game_display.blit(self.img, (self.xcor, self.ycor))    
