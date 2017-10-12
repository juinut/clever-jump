import arcade.key
from random import *


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.score = 0
        self.lastscore = 0
        self.endd = ""
        self.time = 0
        self.time2 = 0
        self.shield = 0
        self.gameover = 0


        self.stupid = Stupid(self, 65, 100)
        self.coin = Coin(self,randint(80,width-80),height)

        self.obstacleLeft = Obstacle(self,65,height,randint(6,11))
        self.obstacleRight = Obstacle(self,width-65,height,randint(6,11))
        self.bonus_list = []
        self.shield_list = []


    def update(self, delta):
        self.stupid.update(delta)
        self.coin.update(delta)
        self.obstacleRight.update(delta)
        self.obstacleLeft.update(delta)

        self.time+=delta
        self.time2+=delta
        if self.time>randint(10,20):
            self.bonus_list.append(Bonus(self,randint(100,self.width-100),self.height,randint(5,15)))
            self.time = 0
        if self.time2>randint(7,15):
            self.shield_list.append(Shield(self,randint(100,self.width-100),self.height,randint(5,15)))
            self.time2 = 0

        for index,b in enumerate(self.bonus_list):
            b.update(delta)
            if self.stupid.hit(b,35):
                self.score+=5
                del self.bonus_list[index]

            if b.is_out_of_screen():
                del self.bonus_list[index]

        print(self.bonus_list)
        for index,s in enumerate(self.shield_list):
            s.update(delta)
            if self.stupid.hit(s,35):
                if self.shield <=2:
                    self.shield+=1
                else:
                    pass

                del self.shield_list[index]

            if s.is_out_of_screen():
                del self.shield_list[index]

        if self.stupid.hit(self.coin, 45):
            self.coin.random_location()
            self.score+=1
        if self.stupid.hit(self.obstacleLeft, 35) and self.shield > 0:
            self.shield -= 1
            self.obstacleLeft.y = -1
        if self.stupid.hit(self.obstacleRight, 35) and self.shield > 0:
            self.shield -= 1
            self.obstacleRight.y = -1
        if (self.stupid.hit(self.obstacleLeft, 35) or self.stupid.hit(self.obstacleRight, 35)) and self.shield == 0:
            if self.gameover ==0:
                self.endd = "GAME OVER"
                self.gameover = 1
                self.lastscore = self.score



    def on_key_press(self, key, key_modifiers):
        if self.stupid.x ==65 or self.stupid.x == self.width-65:
            if key == arcade.key.SPACE:
                self.stupid.switch_direction()

    def hit(self, other, hit_size):
        return (abs(self.x - other.x) <= hit_size) and (abs(self.y - other.y) <= hit_size)

class Stupid(World):
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.vx = -20


    def update(self, delta):
        if self.x >= self.world.width-65:
            pass
        elif self.x > 65 and self.x <= self.world.width/2 and self.vx > 0:
            self.x+=self.vx
            self.y+=2
        elif self.x > self.world.width/2 and self.x < self.world.width-65 and self.vx > 0:
            self.x+=self.vx
            self.y-=2
        elif self.x > self.world.width/2 and self.x< self.world.width-65 and self.vx <0:
            self.x+=self.vx
            self.y+=2
        elif self.x > 65 and self.x <= self.world.width/2 and self.vx < 0:
            self.x+=self.vx
            self.y-=2


    def switch_direction(self):
        self.vx *= -1
        self.x += self.vx

class Coin:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

    def update(self, delta):
        if self.y < 0:
            self.y = self.world.height
            self.x = randint(80, self.world.width-80)
        self.y-=5

    def random_location(self):
        self.x = randint(80, self.world.width-80)
        self.y = self.world.height

class Obstacle:
    def __init__(self, world , x, y, vy):
        self.world = world
        self.x = x
        self.y = y
        self.vy = vy

    def update(self, delta):
        if self.y <0:
            self.y = self.world.height
            if self.world.score <30:
                self.vy = randint(6,11)
            if self.world.score >= 30:
                self.vy = randint(9,14)
            elif self.world.score >= 70:
                self.vy = randint(12,17)
            elif self.world.score >=120:
                self.vy = randint(15,20)
            elif self.world.score >=180:
                self.vy = randint(18,23)

        self.y-=self.vy

class Bonus:
    def __init__(self, world, x, y, vy):
        self.world = world
        self.x = x
        self.y = y
        self.vy = vy

    def __repr__(self):
        return "Bonus[{},{}]->{}".format(self.x,self.y,self.vy)


    def is_out_of_screen(self):
        if self.y < 0:
            return True
        return False

    def movement(self):
        self.y-=self.vy

    def update(self, delta):
        self.movement()

class Shield(Bonus):
    def __init__(self, world, x, y, vy):
        super().__init__(world, x, y, vy)
