import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))

baseLayer = pygame.Surface((640, 480))
color = (255, 255, 255)
depth = 3
mode = "pen"
clock = pygame.time.Clock()

prevX = -1
prevY = -1
currentX = -1
currentY = -1
    
background = (0, 0, 0)
screen.fill(background)

isMouseDown = False

while True:
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_1]: color = (255, 255, 255)
    if pressed[pygame.K_2]: color = (255, 0, 0)
    if pressed[pygame.K_3]: color = (0, 255, 0)
    if pressed[pygame.K_4]: color = (0, 0, 255)
    if pressed[pygame.K_5]: color = (255, 255, 0)
    if pressed[pygame.K_6]: color = (0, 255, 255)
    if pressed[pygame.K_7]: color = (255, 0, 255)
    if pressed[pygame.K_KP_PLUS] and depth < 48: depth += 1
    if pressed[pygame.K_KP_MINUS] and depth > 3: depth -= 1
    if pressed[pygame.K_r]: 
        baseLayer.fill(background)
        screen.fill(background)


    if pressed[pygame.K_KP_1]: mode = "pen"
    if pressed[pygame.K_KP_2]: mode = "rect"
    if pressed[pygame.K_KP_3]: mode = "circle"
    if pressed[pygame.K_KP_4]: mode = "square"
    if pressed[pygame.K_KP_5]: mode = "tr_triangle"
    if pressed[pygame.K_KP_6]: mode = "eq_triangle"
    
    

    if pressed[pygame.K_0]: 
        color = background
        mode = "eraser"
    
    if not(mode == "eraser" or mode == "pen"):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    isMouseDown = True
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]    
                    prevX =  event.pos[0]
                    prevY =  event.pos[1]

            if event.type == pygame.MOUSEBUTTONUP:
                isMouseDown = False
                baseLayer.blit(screen, (0, 0))


            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]
        

        if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
                screen.blit(baseLayer, (0, 0))
                l, u = min(prevX, currentX), min(prevY, currentY)
                w, h = abs(prevX - currentX), abs(prevY - currentY)
                r = pygame.Rect(l, u, w, h)


                if mode == "rect":
                    pygame.draw.rect(screen, color, pygame.Rect(r), depth)
                if mode == "circle":
                    pygame.draw.circle(screen, color, (l+w/2, u+h/2), min(w, h), depth)    

                if mode == "square":
                    pygame.draw.rect(screen, color, pygame.Rect(l, u, min(w, h), min(w, h)), depth)
                if mode == "tr_triangle":
                    pygame.draw.polygon(screen, color, [(l,u), (l,u+h), (l+w,u+h)], depth)
                if mode == "eq_triangle":
                    pygame.draw.polygon(screen, color, [(l,u+h), (l+h//2, u), (l+w,u+h)], depth)
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    isMouseDown = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: 
                    isMouseDown = False

            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                currentX =  event.pos[0]
                currentY =  event.pos[1]
                
        
        if isMouseDown:
            pygame.draw.line(screen, color, (prevX, prevY), (currentX, currentY), depth)

        prevX = currentX
        prevY = currentY
                

    
    pygame.display.flip()
    clock.tick(60)
