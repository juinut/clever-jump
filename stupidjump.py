import arcade
from stupidmodels import *


SCREEN_WIDTH = 530
SCREEN_HEIGHT = 725


class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)

        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)

    def draw(self):
        self.sync_with_model()
        super().draw()

class StupidWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.AERO_BLUE)

        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)
        #self.stupid_sprite = ModelSprite('images/stupidchar.png',model=self.world.stupid)

        self.coin_sprite = ModelSprite('images/brand.png',model=self.world.coin)
        self.obstacleL_sprite = ModelSprite('images/weed.png',model=self.world.obstacleLeft)
        self.obstacleR_sprite = ModelSprite('images/weed.png',model=self.world.obstacleRight)
        self.endd = arcade.create_text("GAME OVER", arcade.color.BLACK, 20)

    def on_draw(self):
        arcade.start_render()
        draw_background()
        if(self.world.endd != "GAME OVER"):
            if self.world.shield == 0:
                ModelSprite('images/stupidchar.png',model = self.world.stupid).draw()
            elif self.world.shield == 1:
                ModelSprite('images/readbookchar.png',model = self.world.stupid).draw()
            elif self.world.shield ==2:
                ModelSprite('images/smartchar.png',model = self.world.stupid).draw()
            #self.stupid_sprite.draw()
            self.coin_sprite.draw()
            self.obstacleL_sprite.draw()
            self.obstacleR_sprite.draw()
            for bs in self.world.bonus_list:
                ModelSprite('images/peptein.png',model=bs).draw()
            for ss in self.world.shield_list:
                ModelSprite('images/redbook.png',model=ss).draw()

            arcade.draw_text(str(self.world.score),
                         self.width - 30, self.height - 30,
                         arcade.color.BLACK, 20)
        else:
            arcade.render_text(self.endd,self.width/3, self.height/2)
            arcade.draw_text("score = {}".format(str(self.world.score)),
                         self.width/2.6, self.height/3.1,
                         arcade.color.BLACK, 20)


    def update(self, delta):
        self.world.update(delta)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

def draw_background():
    arcade.draw_lrtb_rectangle_filled(0,38,SCREEN_HEIGHT,0,arcade.color.BROWN_NOSE)

    arcade.draw_lrtb_rectangle_filled(SCREEN_WIDTH-38,SCREEN_WIDTH,SCREEN_HEIGHT,0,arcade.color.BROWN_NOSE)

def main():
    window = StupidWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()

if __name__ == '__main__':
    main()
