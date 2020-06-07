#Corona Scarper



import pygame
import random
from pygame import mixer

# Initialize PyGame
pygame.init()



homepageRunning = True
running = True





# Colours
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
postalRed = (254, 26, 1)
black = (0, 0, 0)
lightYellow = (240, 252, 60)

# Dimensions
width = 650
height = 700
pixel = 64

# Screen
screen = pygame.display.set_mode((width, height))

# Title/Caption
pygame.display.set_caption("CORONA SCARPER")

# Icon
gameIcon = pygame.image.load("virus_1.png")
pygame.display.set_icon(gameIcon)

# Background
backgroundImg = pygame.image.load("wallBackground.jpg")

#Showing Score
score = 0
scoreFont = pygame.font.Font("Woodplank.ttf", 55)
scoreTextXCrd = 10
scoreTextYCrd = 10
def showScore(x, y):
    scoreValue = scoreFont.render("Score: " + str(score), True, lightYellow)
    screen.blit(scoreValue, (x, y))


#Showing Menu Bar:
def topMenu():
    topmenu = pygame.image.load("home.png")
    screen.blit(topmenu, ((650 - 10 - 64), 10))

    homeFont = pygame.font.Font("Woodplank.ttf", 26)
    homeF = homeFont.render("Home", True, (0, 0, 53))
    screen.blit(homeF, (573, 70))


    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 575 < mouse[0] and (575 + 64) > mouse[0]:
        if 10 < mouse[1] and (10 + 64) > mouse[1]:
            if click[0] == 1:
                global score
                score = 0
                homePage()



# Player
playerImage = pygame.image.load("player.png")
playerXPosition = (width/2) - (pixel/2)
playerYPosition = height - pixel - 10     # So that the player will be at height of 20 above the base
playerXPositionChange = 0
def player(x, y):
    screen.blit(playerImage, (x, y))

# Block
blockImage = pygame.image.load("virus.png")
blockXPosition = random.randint(0, (width - pixel))
blockYPosition = 0 - pixel
blockXPositionChange = 0
blockYPositionChange = 5    #SPEED OF THE BLOCK
def block(x, y):
    screen.blit(blockImage, (x, y))





def infoPage():
    global infoPageRunning
    infoPageRunning = True
    while infoPageRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        #InfoPage Background
        infoPageImage = pygame.image.load("background-blue-design.jpg")
        screen.blit(infoPageImage, (0, 0))

        #Back Button
        backButtonImage = pygame.image.load("back.png")
        screen.blit(backButtonImage, ((width - 64 - 15), 10))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 570 < mouse[0] and (570 + 64) > mouse[0]:
            if 10 < mouse[1] and (10 + 64) > mouse[1]:
                if click[0] == 1:
                    infoPageRunning = False

        #How to play
        htpF = pygame.font.Font("Manga Temple.ttf", 50)
        htpFont = htpF.render("=> How To Play", True, black)
        screen.blit(htpFont, (10, 35))

        htpImgLeft = pygame.image.load("left.png")
        screen.blit(htpImgLeft, (135, 117))

        htpImgRight = pygame.image.load("right.png")
        screen.blit(htpImgRight, (230, 117))

        htp1F = pygame.font.Font("Manga Temple.ttf", 24)
        htp1Font = htp1F.render("-> Press     and     arrow key to move", True, (102, 102, 0))
        screen.blit(htp1Font, (10, 120))

        htp2F = pygame.font.Font("Manga Temple.ttf", 24)
        htp2Font = htp2F.render("    the player", True, (102, 102, 0))
        screen.blit(htp2Font, (10, 160))

        htp3_F = pygame.font.Font("Manga Temple.ttf", 24)
        htp3_Font = htp3_F.render("-> dodge the virus by moving the player ", True, (102, 102, 0))
        screen.blit(htp3_Font, (10, 200))

        htp3_F = pygame.font.Font("Manga Temple.ttf", 24)
        htp3_Font = htp3_F.render("-> Score = no. of virus dodged ", True, (102, 102, 0))
        screen.blit(htp3_Font, (10, 240))

        htp3F = pygame.font.Font("Manga Temple.ttf", 24)
        htp3Font = htp3F.render("-> If Virus hits you, You lose!!!", True, (102, 102, 0))
        screen.blit(htp3Font, (10, 280))

        htppause = pygame.font.Font("Manga Temple.ttf", 24)
        htppauseFont = htppause.render("-> Press Spacebar to pause and resume", True, (102, 102, 0))
        screen.blit(htppauseFont, (10, 320))

        htp4F = pygame.font.Font("Manga Temple.ttf", 60)
        htp4Font = htp4F.render("ALL THE BEST !!!", True, postalRed)
        screen.blit(htp4Font, (50, 380))

        htp5F = pygame.font.Font("Manga Temple.ttf", 35)
        htp5Font = htp5F.render("Corona Scarper", True, (51, 0, 25))
        screen.blit(htp5Font, (160, 500))

        htp6F = pygame.font.Font("Manga Temple.ttf", 30)
        htp6Font = htp6F.render("By", True, (102, 0, 51))
        screen.blit(htp6Font, (300, 550))

        htp7F = pygame.font.Font("Manga Temple.ttf", 40)
        htp7Font = htp7F.render("AMEYA JAIN", True, (0, 51, 25))
        screen.blit(htp7Font, (185, 590))

        pygame.display.update()










# Home Page
def homePage():
    mixer.music.load("nfs.mp3")
    mixer.music.play(-1)
    while homepageRunning:
        playButton()
        exitButton()
        infoButton()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


        #HomepageImage
        homepageImg = pygame.image.load("yellow-surface.jpg")
        screen.blit(homepageImg, (0, 0))


        #virus Images
        virusImg1 = pygame.image.load("virus1.png")
        screen.blit(virusImg1, (420, 440))

        virusImg2 = pygame.image.load("virus2.png")
        screen.blit(virusImg2, (580, 500))

        virusImg3 = pygame.image.load("virus3.png")
        screen.blit(virusImg3, (440, 100))

        virusImg4 = pygame.image.load("virus4.png")
        screen.blit(virusImg4, (50, 100))

        virusImg5 = pygame.image.load("virus5.png")
        screen.blit(virusImg5, (520, 240))

        virusImg6 = pygame.image.load("virus3.png")
        screen.blit(virusImg6, (150, 370))

        virusImg7 = pygame.image.load("virus4.png")
        screen.blit(virusImg7, (20, 490))

        virusImg8 = pygame.image.load("virus.png")
        screen.blit(virusImg8, (215, 200))

        virusImg9 = pygame.image.load("Virus_2.png")
        screen.blit(virusImg9, (335, 200))



        #Corona Font
        coronaFont = pygame.font.Font("wood sticks.ttf", 100)
        corona = coronaFont.render("C  r  na", True, (25, 51, 0))
        screen.blit(corona, (160, 160))

        #Scarper Font
        ScarperFont = pygame.font.Font("wood sticks.ttf", 100)
        Scarper = ScarperFont.render("Scarper", True, (25, 51, 0))
        screen.blit(Scarper, (135, 240))

        #CoronaImage
        coronaImg = pygame.image.load("virus_1.png")
        screen.blit(coronaImg, ((width/2 - 64), 30))

        #PlayButtonImage
        playbuttonImg = pygame.image.load("play.png")
        screen.blit(playbuttonImg, (((width/2) - (128/2), 400)))

        playF = pygame.font.Font("Manga Temple.ttf", 40)
        playFont = playF.render("Play", True, blue)
        screen.blit(playFont, (275, 540))

        #ExitButtonImage
        exitbuttonImage = pygame.image.load("close.png")
        screen.blit(exitbuttonImage, (width - 100- 128, 510))

        exitF = pygame.font.Font("Manga Temple.ttf", 40)
        exitFont = exitF.render("Exit", True, blue)
        screen.blit(exitFont, (440, 650))

        #InstructionImage
        instructionImage = pygame.image.load("question.png")
        screen.blit(instructionImage, (100, 510))

        infoF = pygame.font.Font("Manga Temple.ttf", 40)
        infoFont = infoF.render("Info", True, blue)
        screen.blit(infoFont, (105, 650))


        pygame.display.update()




def playButton():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 260 < mouse[0] and (260 + 128) > mouse[0]:
        if 400 < mouse[1] and (400 + 128) > mouse[1]:
            if click[0] == 1:
                gamingLoop()


def exitButton():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 420 < mouse[0] and (420 + 128) > mouse[0]:
        if 510 < mouse[1] and (510 +128) > mouse[1]:
            if click[0] == 1:
                pygame.quit()


def infoButton():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 100 < mouse[0] and (100 + 128) > mouse[0]:
        if 510 < mouse[1] and (510 +128) > mouse[1]:
            if click[0] == 1:
                infoPage()




# Crashing
def crash():
    global blockYPosition, scoreFont
    # Crashing Condition and Game Over
    if playerYPosition < (
            blockYPosition + pixel):  # If the block passes through the player's horizontal line, then check for block passing through its vertical line
        if (playerXPosition > blockXPosition and playerXPosition < (blockXPosition + pixel)) or (
                (playerXPosition + pixel) > blockXPosition and (playerXPosition + pixel) < (
                blockXPosition + pixel)):
            # |-----># If players left corner meets the block's corner ranges AND same for right corner, then you can crash it.
            blockYPosition = height + 1000  # If block crashed, then go down at height after the repeating block condition

            pygame.mixer_music.stop()
            gameOverSound = pygame.mixer.Sound("GameOver.wav")
            gameOverSound.play()
            # Stop the player Movement after game ends
            global playerXPositionChange
            playerXPositionChange = 0
            # Game Over Text Display
            text1 = pygame.font.Font('Weirdo Regular.ttf', 100)
            text_1 = text1.render("GAME", True, postalRed)
            screen.blit(text_1, (200, 190))
            text2 = pygame.font.Font('Weirdo Regular.ttf', 100)
            text_2 = text2.render("OVER!!!", True, postalRed)
            screen.blit(text_2, (175, 270))
            # Show Score Function call for Final Score by enlarging it
            scoreFont = pygame.font.Font("Woodplank.ttf", 100)
            if score < 10:
                showScore(150, 400)
            else:
                showScore(120, 400)
    else:
        # Show Score at LEFT while playing only
        showScore(scoreTextXCrd, scoreTextYCrd)




# Gaming Loop
def gamingLoop():

    global score, playerXPosition, playerXPositionChange, playerYPosition, blockYPosition, blockYPositionChange, blockXPosition

    mixer.music.load("corona_go_ringtone.mp3")
    mixer.music.play(-1)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # Movement Key Control of Player
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if 325 < mouse[0] and click[0] == 1:
                playerXPositionChange = 5
            if 323 > mouse[0] and click[0] == 1:
                playerXPositionChange = -5
            if 325 < mouse[0] and click[0] == 0:
                playerXPositionChange = 0
            if 323 > mouse[0] and click[0] == 0:
                playerXPositionChange = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    playerXPositionChange = 5
                if event.key == pygame.K_LEFT:
                    playerXPositionChange = -5

            # PAUSE SCREEN
                if event.key == pygame.K_SPACE:
                    pause = True
                    while pause:
                        pauseImg = pygame.image.load("pauseBig.png")
                        screen.blit(pauseImg, (75, 90))
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    pause = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or pygame.K_LEFT:
                    playerXPositionChange = 0



        # Boundaries to the Player
        if playerXPosition >= (width - pixel):
            playerXPosition = (width - pixel)  # if it comes at right end, stay at right end and does not exceed
        if playerXPosition <= 0:
            playerXPosition = 0  # if it comes at left end, stay at left end and does not exceed

        # Movement of Player
        playerXPosition += playerXPositionChange

        # Movement of Block
        blockYPosition += blockYPositionChange

        # Multiple Blocks Movement after each other
        if blockYPosition >= height - 0 and blockYPosition <= (
                height + 200):  # and condition used because of game over function
            blockYPosition = 0 - pixel
            blockXPosition = random.randint(0, (width - pixel))
            # If block passes the player, then it dodges that block and increases the score by
            score += 1

        # Background Image
        screen.blit(backgroundImg, (0, 0))

        # Player Function Call
        player(playerXPosition, playerYPosition)

        # Block Function Call
        block(blockXPosition, blockYPosition)

        # Call of Crashing Function
        crash()

        # Speed Increasing according to the score
        if score > 7 and score < 12:
            blockYPositionChange = 7
        if score > 12 and score < 18:
            blockYPositionChange = 8.5
        if score > 18 and score < 20:
            blockYPositionChange = 9.2
        if score > 20 and score < 30:
            blockYPositionChange = 10.2
        if score > 30 and score < 43:
            blockYPositionChange = 11.5
        if score > 43 and score < 55:
            blockYPositionChange = 11.9
        if score > 55 and score < 70:
            blockYPositionChange = 12.7
        if score > 70 and score < 100:
            blockYPositionChange = 14



        #CoronaScarper Font
        coronaScarperFont = pygame.font.Font("wood sticks.ttf", 32)
        coronaScarper = coronaScarperFont.render("Corona Scarper", True, (0, 51, 102))
        screen.blit(coronaScarper, (270, 20))

        #Pause to play
        PauseFont = pygame.font.Font("Weirdo Regular.ttf", 30)
        PauseF = PauseFont.render("Space", True, (25, 51, 0))
        screen.blit(PauseF, (570, 110))

        PauseFont1 = pygame.font.Font("Weirdo Regular.ttf", 30)
        PauseF1 = PauseFont1.render("to", True, (25, 51, 0))
        screen.blit(PauseF1, (595, 130))

        PauseFont2 = pygame.font.Font("Weirdo Regular.ttf", 30)
        PauseF2 = PauseFont2.render("pause", True, (25, 51, 0))
        screen.blit(PauseF2, (570, 150))


        # Showing Top Menu
        topMenu()


        # Updating the screen after each iteration
        pygame.display.update()




homePage()
#Sound, HomePage(instruction), StartPage( spacebar press to StartButton), play again at game over
#Buttons Shading
#score in top menu
#pause game
#pause the game by creating new screen
#play function should always start a new game
#while running is breaked and no code after that is written
#if
