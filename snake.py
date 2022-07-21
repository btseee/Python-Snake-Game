import pygame
import sys
import random
import time
import os
import emoji

pygame.init()

#MOGOIN BAIRSHIL HUDULGUUN
class Snake():
    #Ehleh Tseh
    def __init__(self):
        self.position = [100,50]
        self.body = [[50,50],[90,50],[80,50]]   
        self.direction = "RIGHT"
        
    #Chiglelee uurchluh
    def changeDirTo(self,dir):
        if dir=="RIGHT" and not self.direction=="LEFT":
            self.direction = "RIGHT"
        elif dir=="LEFT" and not self.direction=="RIGHT":
            self.direction = "LEFT"
        elif dir=="UP" and not self.direction=="DOWN":
            self.direction = "UP"
        elif dir=="DOWN" and not self.direction=="UP":
            self.direction = "DOWN"    
            
    #Hudluh       
    def move(self,foodPos):
        if self.direction == "RIGHT":
            self.position[0] = self.position[0] + 10
        elif self.direction == "LEFT":
            self.position[0] = self.position[0] - 10
        elif self.direction == "UP":
            self.position[1] = self.position[1] - 10
        elif self.direction == "DOWN":
            self.position[1] = self.position[1] + 10
        self.body.insert(0,list(self.position))
         
        if self.position == foodPos:
            return 1
        else:
            self.body.pop()
            return 0
        
    #Hudluh alham
    def move_Right(self):
        self.position[0] = self.position[0] + 10
    def move_Left(self):
        self.position[0] = self.position[0] - 10
    def move_Up(self):
        self.position[0] = self.position[1] - 10
    def move_Down(self):
        self.position[0] = self.position[1] + 10
        
    #Hana bolon biyee murgusung shalgah
    def checkCollision(self):
        if self.position[0] > 490 or self.position[0] < 10:
            return 1 
        elif self.position[1] > 500 or self.position[1] < 10:
            return 1
        for bodyPart in self.body[1:]:
            if self.position == bodyPart:
                return 1
        return 0
    
    #Tolgoin bairshil avah
    def getHeadPosition(self):
        return self.position
    
    #Biyiin bairshil avah
    def getBody(self):
        return self.body
 
    
#Hoolnii butets
class FoodSpawn():
    #Window dotor bairshuulah
    def __init__(self):
        self.position = [random.randint(4,46)*10,random.randint(4,46)*10]
        self.isFoodOnScreen = True
 
    #Randomoor hool garch ireh
    def spawnFood(self):
        if self.isFoodOnScreen == False:
            self.position = [random.randrange(4,46)*10,random.randrange(4,46)*10]
            self.isFoodOnScreen = True
        return self.position
    
    #Random uusseniig delgetsend bairshuulah
    def setFoodOnScreen(self,b):
        self.isFoodOnScreen = b
 
#Delgetsiin hemjee
window = pygame.display.set_mode((500+20,500+20))

#Zurag duudah 
background = pygame.image.load("./assets/grass.png")
head=pygame.image.load("./assets/head.png")
food=pygame.image.load("./assets/food.png")

#Caption
pygame.display.set_caption("Могой "+emoji.emojize(":snake: :snake: :snake:"))
fps = pygame.time.Clock()

#ONoonii anhnii utga
score=0;

#Funktsiig duudh 
snake = Snake()
foodSpawner = FoodSpawn()

#Togloomiig duusgah
def gameOver():
    #Font tohiruulga
    font = pygame.font.SysFont('Times New Roman',50,bold=True)
    score_text = font.render("Та " + str(score) + " оноо авлаа!!!",4,(255,255,255))
    window.blit(score_text,(60,220))
    pygame.display.flip()
    
    time.sleep(3)
    pygame.quit()
    sys.exit()
    
#Hamgiin undur onoog duudah
def get_high_score():
    #Anhnii utga
    high_score = 0
 
    #File aas unshih
    try:
        high_score_file = open("./stats/high_score.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
    except IOError:
        # File hooson bna
        return "IO ERROR"
    except ValueError:
        # File iig unshij baigaa ch utga oilgohgui bna
        return "VALUE ERROR"
    #UTGA butsaah
    return high_score
 
#Shine undur onoog hadgal 
def save_high_score(new_high_score):
    try:
        #File daa bichih
        high_score_file = open("./stats/high_score.txt", "w")
        high_score_file.write(str(new_high_score))
        high_score_file.close()
    except IOError:
        # Medegdehgui error
        print("IO ERROR1")
 

#=========================================
#           GOL DAVTALT
#=========================================
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver()
        pressed = pygame.key.get_pressed()
        score
        #KEY sonsoh heseg
        if pressed[pygame.K_RIGHT]:
            snake.changeDirTo('RIGHT')
        elif pressed[pygame.K_LEFT]:
            snake.changeDirTo('LEFT')
        elif pressed[pygame.K_UP]:
            snake.changeDirTo('UP')
        elif pressed[pygame.K_DOWN]:
            snake.changeDirTo('DOWN')
            
        #garah
        elif pressed[pygame.K_q]:
            gameOver() 
            
        #shine togloom
        if pressed[pygame.K_n]:
            os.execl(sys.executable, sys.executable, *sys.argv)
            
        #Zavsarlasan uyed urgejluuleh geh met
        if pressed[pygame.K_p]:
            font = pygame.font.SysFont('Times New Roman',50,bold=True)
            text_surface = font.render("Завсарлага авлаа",20, (255, 255, 255))
            window.blit(text_surface,(50,200))
            text_surface1 = font.render("R = Resume",20, (255, 255, 255))
            window.blit(text_surface1,(100,250))
            text_surface1 = font.render("Q= Quit",20, (255, 255, 255))
            window.blit(text_surface1,(100,300))
            text_surface1 = font.render("N= New Game",20, (255, 255, 255))
            window.blit(text_surface1,(100,350))
            pygame.display.flip()
            pygame.time.delay(3000)
            
        if pressed[pygame.K_c]:
            pygame.time.delay(0)
            continue
    #Hool spawndah
    foodPos = foodSpawner.spawnFood()
    if(snake.move(foodPos)==1):
        score+=1
        foodSpawner.setFoodOnScreen(False)
        
    #Background oruulah
    window.fill(pygame.Color(225,225,225))
    window.blit(background,(10,10))
    
    for x in range(0, 510, 10):
        pygame.draw.rect(window, (0,0,225), [x, 0, 10, 10])
        pygame.draw.rect(window, (0,0,225), [x, 510, 10, 10])
 
    for x in range(0, 510, 10):
        pygame.draw.rect(window, (0,0,225), [0, x, 10, 10])
        pygame.draw.rect(window, (0,0,225), [510, x, 10, 10])
        
    #Biyiin bairshil
    for pos in snake.getBody():
        window.blit(head,(pos[0],pos[1],10,10))
    #hoolnii bairshil
    window.blit(food,(foodPos[0],foodPos[1],10,10))
    
    #murguldsun eseh
    if(snake.checkCollision()==1):
        gameOver()
    
    #Undur onoogoos iluu onoo avsan tohioldold hadgalah 
    high_score = get_high_score()
    if score > high_score:
        save_high_score(score)
    
    #Window zsavar    
    pygame.display.set_caption("МОГОЙ(Python3 by B160910083)"+emoji.emojize(":snake:")+"ОНОО:"+str(score)+" ӨНДӨР ОНОО:"+ str(high_score))
    pygame.display.flip()
    fps.tick(20)
    

pygame.quit()