import pygame as pygame

def drawScore(font):
    global score
    
    text=font.render(str(score), True, white)
    window.blit(text, (200, 30))

def MoveBall():
    global ballSpeedx, ballSpeedy, ballLocation, ball
    
    if ballLocation[0] > screenWidth:
        ballSpeedx = -ballSpeedx
    
    if ballLocation[0] < 0:
        ballSpeedx = -ballSpeedx
    
    if ballLocation[1] < 0:
        ballSpeedy = -ballSpeedy
    
    if ballLocation[1] > screenHeight:
        ballSpeedy = -ballSpeedy
        
    ballLocation[0] = ballLocation[0] + ballSpeedx
    ballLocation[1] = ballLocation[1] + ballSpeedy
    ball = pygame.draw.circle(window, white, ballLocation, radius, 0) 
    
def MovePaddle():
    global PadASpeed, PadA
    """
    Moves the paddle side to side
    """
    
    if PadA.left <= 0:
        print("Left Side of Screen")
        PadA = PadA.move(2,0)
        PadASpeed = 0
    #Add right of Paddle Code here
        
    PadA = PadA.move(PadASpeed, 0)
    pygame.draw.rect(window, white, PadA)

timer = pygame.time.Clock()

screenWidth = 1000
screenHeight = 600

window = pygame.display.set_mode([screenWidth, screenHeight])

ballSpeedx = -1
ballSpeedy = 1
black = (0,0,0)
white = (255, 255, 255)
radius = 20
ballLocation=[500, 300]
ball = pygame.Rect(ballLocation, (radius, radius))

PadA = pygame.Rect((500,570), (100,20))
PadASpeed = 0

score = 0

pygame.font.init()
#print(pygame.font.get_fonts())
font = pygame.font.SysFont(None, 72)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PadASpeed = -2
            if event.key == pygame.K_RIGHT:
                PadASpeed = 2
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                PadASpeed = 0
            if event.key == pygame.K_RIGHT:
                PadASpeed = 0
    if PadA.colliderect(ball):
        ballSpeedy = -ballSpeedy
    timer.tick(60)
    window.fill(black)
    MoveBall()
    MovePaddle()
    drawScore(font)
    pygame.display.flip()