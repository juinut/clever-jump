import arcade
from stupidmodels import World,Stupid

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

        arcade.set_background_color(arcade.color.BLACK)

        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.stupid_sprite = ModelSprite('images/block.png',model=self.world.stupid)

    def on_draw(self):
        arcade.start_render()

        self.stupid_sprite.draw()

    def update(self, delta):
        self.world.update(delta)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)


def main():
    window = StupidWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()

if __name__ == '__main__':
    main()
