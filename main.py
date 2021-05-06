import pygame
import random
class Apple:
    def __init__(self):
        self.r = 10
        self.x = random.randint(0,width)
        self.y = random.randint(0,height)
        self.color = (255,0,0)
    def show(self):
        pygame.draw.circle(d,self.color,[self.x , self.y] , self.r)

class Pear:
    def __init__(self):
        self.r = 10
        self.x = random.randint(0,width)
        self.y = random.randint(0,height)
        self.color = (255,255,0)
    def show(self):
        pygame.draw.circle(d,self.color,[self.x , self.y] , self.r)

class Mine:
    def __init__(self):
        self.r = 10
        self.x = random.randint(0,width)
        self.y = random.randint(0,height)
        self.color = (0,0,0)
    def show(self):
        pygame.draw.circle(d,self.color,[self.x , self.y] , self.r)


class Snake:
    def __init__(self):
        self.w = 16
        self.h = 16
        self.x = width/2
        self.y = height/2
        self.name = "Python"
        self.color = (0,127,0)
        self.speed = 4
        self.score = 0
        self.x_change = 0
        self.y_change = 0
        self.body = []
    def eat(self):
        if apple.x - apple.r < self.x <= apple.x + apple.r and apple.y - apple.r < self.y <= apple.y + apple.r:
            self.score += 1
            self.body.append('1')
            return True
        elif pear.x - pear.r < self.x <= pear.x + pear.r and pear.y - pear.r < self.y <= pear.y + pear.r:
            self.score += 2
            self.body.append('1')
            self.body.append('1')
            return True
        if mine.x - mine.r < self.x <= mine.x + mine.r and mine.y - mine.r < self.y <= mine.y + mine.r:
            self.score -= 1
            self.body.remove('1')
            return True
        else:
            return False
    def show(self):
        pygame.draw.rect(d,self.color,[self.x,self.y,self.w,self.h])

        for index,item in enumerate(self.body):
            
            pygame.draw.rect(d,self.color,[self.x -item *16 ,self.y,self.w,self.h])

    def move(self):
        if self.x_change == -1 :
            self.x -= self.speed
        elif self.x_change == 1 :
            self.x += self.speed
        elif self.y_change == -1 :
            self.y -= self.speed
        elif self.y_change == 1 :
            self.y += self.speed

    def touch(self):
        if self.x > width or self.x< width:
            return False    

    def highscore(self):
        pygame.font.init()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            myfont = pygame.font.SysFont("monospace", 15)
            BLACK = (0, 0, 0)
            label = myfont.render("score = ", 1, BLACK)
            d.blit(label, (0, 10))
            pygame.display.update()





if __name__ == "__main__" :

    width = 600
    height = 400

    d = pygame.display.set_mode((width,height))
    clock = pygame.time.Clock()
    snake = Snake()
    apple = Apple()
    pear = Pear()
    mine = Mine()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    snake.x_change = -1
                    snake.y_change = 0
                elif event.key == pygame.K_d:
                    snake.x_change = 1
                    snake.y_change = 0
                elif event.key == pygame.K_w:
                    snake.y_change = -1
                    snake.x_change = 0
                elif event.key == pygame.K_s:
                    snake.y_change = 1
                    snake.x_change = 0
        snake.move()
        result = snake.eat()
        if result == True:
            apple = Apple()
            pear = Pear()
            mine = Mine()
        d.fill((0,255,0))
        snake.show()
        apple.show()
        pear.show()
        mine.show()
        snake.highscore()
        pygame.display.update()       
        if snake.touch() == False:
            print('Game Over')
            exit()
        clock.tick(30)