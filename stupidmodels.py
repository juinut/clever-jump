import arcade.key

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.stupid = Stupid(self, 65, 100)


    def update(self, delta):
        self.stupid.update(delta)

    def on_key_press(self, key, key_modifiers):
        if self.stupid.x ==65 or self.stupid.x == self.width-65:
            if key == arcade.key.SPACE:
                self.stupid.switch_direction()

class Stupid:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.vx = -20


    def update(self, delta):
        if self.x >= self.world.width-65:
            pass
        elif self.x > 65:
            self.x+=self.vx


        '''
        if self.y > self.world.height:
            self.y = 0
        self.y += 5
        '''
    def switch_direction(self):
        self.vx *= -1
        self.x += self.vx
