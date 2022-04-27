import pygame

pygame.init()

pygame.display.set_mode((400,400))

screen = pygame.display.set_mode((400,400))

clock = pygame.time.Clock()
  
# it will display on screen
screen = pygame.display.set_mode([600, 500])
  
# basic font for user typed
base_font = pygame.font.Font(None, 32)
user_text = ''
  
# create rectangle
input_rect = pygame.Rect(80, 50, 20, 30)

pygame.display.set_caption("project word")
screen.fill((255,255,255))
xpose = 50
width = 31
for i in range(6):
  pygame.draw.rect(screen, (200,111,111), (xpose+width,50,30,30), border_radius=5)
 #text_surface = base_font.render(user_text, True, (255, 255, 255))
  #screen.blit(text_surface, (xpose+width, 50))
  width = width + 31
ypose = -12
height = 31
for i in range(6):
  pygame.draw.rect(screen, (200,111,111), (112,ypose+height,30,30), border_radius=5)
  height = height + 31 




  # color_active stores color(lightskyblue3) which
# gets active when input box is clicked by user
color_active = pygame.Color('#0000ffff')
  
# color_passive store color(chartreuse4) which is
# color of input box.
color_passive = pygame.Color('#0000ffff')
color = color_passive
  
active = False
  
while True:
    for event in pygame.event.get():
  
      # if user types QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
  
        if event.type == pygame.MOUSEBUTTONDOWN:
 
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
  
        if event.type == pygame.KEYDOWN:
            print(event.key)
            # Check for backspace
            if event.key == pygame.K_BACKSPACE:
  
                # get text input from 0 to -1 i.e. end.
                user_text = user_text[:-1]
            elif event.key == 13 or event.key == 1073741912:
                if user_text == "ciao":
                    user_text = "Ciao anche a te"
  
            # Unicode standard is used for string
            # formation
            else:
                user_text += event.unicode
      
  
    if active:
        color = color_active
    else:
        color = color_passive
          
    # draw rectangle and argument passed which should
    # be on screen
    #pygame.draw.rect(screen, color, input_rect)
  
    text_surface = base_font.render(user_text, True, (255, 255, 255))
      
    # render at position stated in arguments
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
      
    # set width of textfield so that text cannot get
    # outside of user's text input
    #input_rect.w = max(100, text_surface.get_width()+10)
      
    # display.flip() will update only a portion of the
    # screen to updated, not full area
    pygame.display.flip()
      
    # clock.tick(60) means that for every second at most
    # 60 frames should be passed.
    clock.tick(60)


pygame.display.set_caption("My Game")




pygame.display.update()

