import pygame
pygame.init()
fenetreLargeur =1280# 1720 #1280 
fenetreHauteur = 720  #  1000 #720
screen = pygame.display.set_mode((fenetreLargeur, fenetreHauteur))
clock = pygame.time.Clock()
running = True
font = pygame.font.Font("assets/NotoSans-Bold.ttf",  screen.get_width()//40)
pygame.display.set_caption("Morpion")
running = True

class Morpion:
    def __init__(self):
        self.board = [["" for j in range(3)]for i in range(3)]
        self.running = True
        self.joueur1 = "X"
        self.joueur2 = "O"
        self.touractuelle = "X"
    def draw(self):
        print(" |", self.board[0][0] , "|", self.board[0][1] , "|", self.board[0][2] , "|","\n"
       " ----------","\n",
       "|", self.board[1][0] , "|", self.board[1][1] , "|", self.board[1][2] , "|","\n",
        "----------","\n",
        "|", self.board[2][0] , "|", self.board[2][1], "|" , self.board[2][2] , "|","\n")
    def play(self,coup):
        coup -= 1
        coup1 = coup//3
        coup2 = coup%3
        print(str(self.board[coup1][coup2]))
        if self.board[coup1][coup2] == "":
            self.board[coup1][coup2] = self.touractuelle
            
            self.touractuelle = self.joueur2 if self.touractuelle == self.joueur1 else self.joueur1
        
            winner = self.get_winner()
            if winner != None:
                return winner
        
    def game(self):
        while self.running:
            self.draw()
            if self.touractuelle == self.joueur1:
                coup = int(input("Joueur {} ".format(self.touractuelle)))
            elif self.touractuelle == self.joueur2:
                coup = self.get_best_move()
                if coup is None:
                    print("Match nul !")
                    self.running = False
                    return
            winner = self.play(coup)
            if winner != None:
                print("The winner is {}".format(winner))
                self.running = False
    
    def get_winner(self):
        if self.board[0][0] == self.board[0][1] == self.board[0][2]!= "":
            return self.board[0][0]
        elif self.board[1][0] == self.board[1][1] == self.board[1][2]!= "":
            return self.board[1][0]
        elif self.board[2][0] == self.board[2][1] == self.board[2][2]!= "":
            return self.board[0][0]
            
        elif self.board[0][0] == self.board[1][0] == self.board[2][0]!= "":
            return self.board[1][0]
        elif self.board[0][1] == self.board[1][1] == self.board[2][1]!= "":
            return self.board[0][1]
        elif self.board[0][2] == self.board[1][2] == self.board[2][2]!= "":
            return self.board[0][2]
            
        elif self.board[0][0] == self.board[1][1] == self.board[2][2]!= "":
            return self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0]!= "":
            return self.board[0][2]
    def isfull(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    return False
        return True
    def minimax(self,is_maximizing):
        winner = self.get_winner()
        if winner == self.joueur2:
            return 1
        elif winner == self.joueur1:
            return -1
        elif self.isfull():
            return 0
        if is_maximizing:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == "":
                        self.board[i][j] = self.joueur2
                        score = self.minimax(False)
                        self.board[i][j] = ""
                        best_score = max(score,best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == "":
                        self.board[i][j] = self.joueur1
                        score = self.minimax(True)
                        self.board[i][j] = ""
                        best_score = min(score,best_score)
            return best_score
    def get_best_move(self):
        best_score = -float('inf')
        move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    self.board[i][j] = self.joueur2
                    score = self.minimax(False)
                    self.board[i][j] = ""
                    if score > best_score:
                        best_score = score
                        print(i,j)
                        move = i*3 + j + 1
        return move
class Button:
    def __init__(self,x,y,width,height,color = "white",text = "",text_color = (255,255,255),taille = 25):
        self.rect = pygame.Rect(x,y,width,height)
        self.color = color
        self.taille_text = pygame.font.Font("assets/NotoSans-Bold.ttf", taille)
        self.text = self.taille_text.render(text, 1,text_color)
    def draw(self):
        pygame.draw.rect(screen,self.color,self.rect)
        screen.blit(self.text,(self.rect.x+self.rect.width/2-self.text.get_width()/2,self.rect.y+self.rect.height/2-self.text.get_height()/2))
class Menu_principal:
    def __init__(self):
        self.titre = font.render("PONG",True,"black")
        self.human = Button(fenetreLargeur/2-fenetreLargeur/20,fenetreLargeur*0.1,fenetreLargeur/10,fenetreLargeur/20,"Black","JcJ","White")
        self.bot = Button(fenetreLargeur/2-fenetreLargeur/20,fenetreLargeur*0.2,fenetreLargeur/10,fenetreLargeur/20,"Black","JcB")
        self.ouvert = True
    def load(self):
        screen.blit(self.titre,(fenetreLargeur/2-self.titre.get_width()/2,0))
        self.human.draw()
        self.bot.draw()
class Menu_game:
    def __init__(self):
        self.tkt = 0
        self.ouvert = False
        self.button = [Button(i * fenetreLargeur/3,j*fenetreHauteur/3,fenetreLargeur/3,fenetreHauteur/3) for j in range(3) for i in range(3)]
        self.button_restart = Button(fenetreLargeur/2-fenetreLargeur/20,fenetreHauteur/2-fenetreHauteur/20,fenetreLargeur/10,fenetreHauteur/10,"blue","Restart")
        self.board = [["" for j in range(3)]for i in range(3)]
        self.running = True
        self.bot = False
        self.joueur1 = "X"
        self.joueur2 = "O"
        self.winner = None
        self.touractuelle = "X"
    def load(self):
        for i in range(1, 3):  # 2 lignes horizontales et 2 verticales
            # Ligne verticale
            pygame.draw.line(screen, (0,0,0), (i * (fenetreLargeur/3), 0), (i * (fenetreLargeur/3), fenetreHauteur), 5)
            # Ligne horizontale
            pygame.draw.line(screen, (0,0,0), (0, i * fenetreHauteur/3), (fenetreLargeur, i * (fenetreHauteur/3)), 5)
            self.draw()
            if self.winner != None:
                winner = font.render(f"the winner is {self.winner}",True,"black")
                screen.blit(winner,(fenetreLargeur/2-winner.get_width()/2,fenetreHauteur/2-winner.get_height()*2))
                self.button_restart.draw()
    def draw(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == self.joueur1:
                    self.draw_cross(j,i)
                elif self.board[i][j] == self.joueur2:
                    self.draw_circle(j,i)
    def draw_cross(self,x,y):
        pygame.draw.line(screen,(0,0,0),(x*fenetreLargeur/3+fenetreLargeur/12,y*fenetreHauteur/3 + fenetreHauteur/12),(x*fenetreLargeur/3 + fenetreLargeur/4,y*fenetreHauteur/3 + fenetreHauteur/4),5)
        pygame.draw.line(screen,(0,0,0),(x*fenetreLargeur/3+fenetreLargeur/4,y*fenetreHauteur/3 + fenetreHauteur/12),(x*fenetreLargeur/3 + fenetreLargeur/12,y*fenetreHauteur/3 + fenetreHauteur/4),5)

    def draw_circle(self,x,y):
        pygame.draw.circle(screen,"black",(x*fenetreLargeur/3 + fenetreLargeur/6,y*fenetreHauteur/3 + fenetreHauteur/6),50)
    def play(self,coup):
        coup1 = coup//3
        coup2 = coup%3
        if self.board[coup1][coup2] == "":
            self.board[coup1][coup2] = self.touractuelle
            
            self.touractuelle = self.joueur2 if self.touractuelle == self.joueur1 else self.joueur1
            self.get_winner()
        if self.bot and self.touractuelle == self.joueur2 and self.isfull() == False:
            self.play(self.get_best_move())
            
        
    def game(self):
        while self.running:
            self.draw()
            if self.touractuelle == self.joueur1:
                coup = int(input("Joueur {} ".format(self.touractuelle)))
            elif self.touractuelle == self.joueur2:
                coup = self.get_best_move()
                if coup is None:
                    print("Match nul !")
                    self.running = False
                    return
            winner = self.play(coup)
            if winner != None:
                print("The winner is {}".format(winner))
                self.running = False
    
    def get_winner(self):
        if self.board[0][0] == self.board[0][1] == self.board[0][2]!= "":
            self.winner = self.board[0][0]
        elif self.board[1][0] == self.board[1][1] == self.board[1][2]!= "":
            self.winner = self.board[1][0]
        elif self.board[2][0] == self.board[2][1] == self.board[2][2]!= "":
            self.winner = self.board[0][0]
            
        elif self.board[0][0] == self.board[1][0] == self.board[2][0]!= "":
            self.winner = self.board[1][0]
        elif self.board[0][1] == self.board[1][1] == self.board[2][1]!= "":
            self.winner = self.board[0][1]
        elif self.board[0][2] == self.board[1][2] == self.board[2][2]!= "":
            self.winner = self.board[0][2]
            
        elif self.board[0][0] == self.board[1][1] == self.board[2][2]!= "":
            self.winner = self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0]!= "":
            self.winner = self.board[0][2]
    def isfull(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    return False
        return True
    def minimax(self,is_maximizing):
        self.winner = None
        self.get_winner()
        if self.winner == self.joueur2:
            return 1
        elif self.winner == self.joueur1:
            return -1
        elif self.isfull():
            return 0
        if is_maximizing:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == "":
                        self.board[i][j] = self.joueur2
                        score = self.minimax(False)
                        self.board[i][j] = ""
                        best_score = max(score,best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == "":
                        self.board[i][j] = self.joueur1
                        score = self.minimax(True)
                        self.board[i][j] = ""
                        best_score = min(score,best_score)
            return best_score
    def get_best_move(self):
        best_score = -float('inf')
        move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    self.board[i][j] = self.joueur2
                    score = self.minimax(False)
                    self.board[i][j] = ""
                    if score > best_score:
                        best_score = score
                        print(i,j)
                        move = i*3 + j
        self.winner = None
        return move
    def restart(self):
        self.__init__()
        self.ouvert = True
    
menu_list = [Menu_principal(),Menu_game()]
for button in menu_list[1].button:
    print(str(button.rect.x) + " " + str(button.rect.y) + " " +  str(button.rect.width) + " " + str(button.rect.height))
while running:
    screen.fill("white")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            if menu_list[0].ouvert:
                if menu_list[0].human.rect.collidepoint(pygame.mouse.get_pos()):
                    screen.fill("white")
                    menu_list[0].ouvert = False
                    menu_list[1].ouvert = True
                if menu_list[0].bot.rect.collidepoint(pygame.mouse.get_pos()):
                    menu_list[0].ouvert = False
                    menu_list[1].ouvert = True
                    menu_list[1].bot = True

            elif menu_list[1].ouvert == True:
                    if menu_list[1].winner == None:
                        for i in range(9):
                            if menu_list[1].button[i].rect.collidepoint(pygame.mouse.get_pos()):
                                menu_list[1].play(i)
                                menu_list[1].draw()
                    else:
                        if menu_list[1].button_restart.rect.collidepoint(pygame.mouse.get_pos()):
                            menu_list[1].restart()
    for menu in menu_list:
        if menu.ouvert == True:
            menu.load()
    pygame.display.flip()
