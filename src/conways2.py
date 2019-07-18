import pygame, random
 
# Define some colors and other constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (25, 25, 25)
BTN_COLOUR = (175, 203, 255)
MARGIN = 3
SQ_LENGTH = 20
SQ_NUM = 25
WIN_SIZE = (SQ_NUM + 1) * MARGIN + SQ_NUM * SQ_LENGTH
BTN_SIZE = 30


pygame.init()
 
# Set the width and height of the screen [width, height]
size = (WIN_SIZE, WIN_SIZE + BTN_SIZE + 20)
screen = pygame.display.set_mode(size)

automata = [0] * (SQ_NUM * SQ_NUM)
# TODO: add some variables to track generations and speed of game start and stop etc
generations = 0
time_step = 5
running = True

# Assign Random Values to our Automata
# rowx:
#     col:
#         automata[row * SQ_NUM + col] = set to a random number

# for i in range(SQ_NUM * SQ_NUM):
#     automata[i] = random.randint(0, 1)

for row in range(SQ_NUM):
    for col in range(SQ_NUM):
        automata[row * SQ_NUM + col] = random.randint(0, 1)

# TODO: add some special figures on to the screen

# Block
automata[3] = 1
automata[4] = 1
automata[SQ_NUM + 3] = 1
automata[SQ_NUM + 4] = 1

# Bee-Hive
automata[SQ_NUM - 6] = 1
automata[SQ_NUM - 5] = 1
automata[SQ_NUM + SQ_NUM - 4] = 1
automata[SQ_NUM + SQ_NUM - 7] = 1
automata[2 * SQ_NUM + SQ_NUM - 5] = 1
automata[2 * SQ_NUM + SQ_NUM - 6] = 1


# Blinker

# Beacon

# glider

# Add a title
pygame.display.set_caption("Conway's Game of Life")

# add font
font = pygame.font.Font('freesansbold.ttf', 16)

# Add button
# inc_timestep_button = pygame.draw.rect(screen, BTN_COLOUR, pygame.Rect(10, WIN_SIZE + 10, 3 * BTN_SIZE, BTN_SIZE))
# dec_timestep_button = pygame.draw.rect(screen, BTN_COLOUR, pygame.Rect(25, WIN_SIZE + 10, 3 * BTN_SIZE, BTN_SIZE))

# TODO: add more buttons
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # click event
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()

            # use the pos of mouse to decide which button was pressed
            if inc_timestep_button.collidepoint(click_pos) and time_step < 20:
                print("faster")
                time_step += 1
            # TODO: click pos for other buttons
            if dec_timestep_button.collidepoint(click_pos) and time_step > 1:
                print("slower")
                time_step -= 1

            if restart_button.collidepoint(click_pos):
                print("reset")
                generations = 0
                for row in range(SQ_NUM):
                    for col in range(SQ_NUM):
                        automata[row * SQ_NUM + col] = random.randint(0, 1)

            if pr_button.collidepoint(click_pos):
                running = not running
                
                

    # --- Game logic should go here
    # Update State ( Add Rules to update each cell based on it's previous state )

    # Create a new automata for the next state
    new_automata = [0] * (SQ_NUM * SQ_NUM)

    for i in range(len(automata)):
        live = 0
        dead = 8

        # look at neighbors
        # (8 if conditions)
        if i - 1 >= 0 and automata[i - 1]:
            live += 1
        if i + 1 < (SQ_NUM * SQ_NUM) and automata[i + 1]:
            live += 1
        # TODO: the other neighbours
        if i - SQ_NUM >= 0 and automata[i - SQ_NUM]:
            live += 1
        if i + SQ_NUM < (SQ_NUM * SQ_NUM) and automata[i + SQ_NUM]:
            live += 1
        if i - SQ_NUM - 1 >= 0 and automata[i - SQ_NUM - 1]:
            live += 1
        if i + SQ_NUM + 1 < (SQ_NUM * SQ_NUM) and automata[i + SQ_NUM + 1]:
            live += 1
        if i - SQ_NUM - 1 >= 0 and automata[i - SQ_NUM + 1]:
            live += 1
        if i + SQ_NUM + 1 < (SQ_NUM * SQ_NUM) and automata[i + SQ_NUM - 1]:
            live += 1
        
        dead -= live
        
        

        # Update State
        # if there are less than 2 living neighbors the cell dies
        if automata[i] and live < 2:
            new_automata[i] = 0
        # if alive and has less than 4 neighbors then cell carrys on living
        elif automata[i] and live < 4:
            new_automata[i] = 1
        # TODO: 3 more conditions
        elif automata[i] and live >= 4:
            new_automata[i] = 0
        elif not automata[i] and live == 3:
            new_automata[i] = 1
        else:
            new_automata[i] = 0


    # swap the data for the next generations data
    if running:
        automata = new_automata
        generations += 1



    # --- Screen-clearing code goes here

    # Here, we clear the screen to gray. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(GRAY)
    # --- Drawing code should go here
    # pygame.draw.rect(screen, RED, pygame.Rect(20, 20, 20, 20))
    y = MARGIN
    i = 0
    while y < WIN_SIZE:
        x = MARGIN
        while x < WIN_SIZE:
            if automata[i] == 0:
                pygame.draw.rect(screen, BLACK, pygame.Rect(x, y, SQ_LENGTH, SQ_LENGTH))
            else:
                pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, SQ_LENGTH, SQ_LENGTH))
            i += 1
            x += SQ_LENGTH + MARGIN
        y += SQ_LENGTH + MARGIN

    # Update inc Timestep button
    inc_timestep_button = pygame.draw.rect(screen, BTN_COLOUR, pygame.Rect(10, WIN_SIZE + 10, 3 * BTN_SIZE, BTN_SIZE))
    text = font.render("Speed up", True, (14, 28, 54)) # TODO: change text in button and refactor colour
    textRect = text.get_rect()
    textRect.center = (inc_timestep_button.center[0], inc_timestep_button.center[1])
    screen.blit(text, textRect)

    # TODO: add other button updates

    # Update dec Timestep button
    dec_timestep_button = pygame.draw.rect(screen, BTN_COLOUR, pygame.Rect(115, WIN_SIZE + 10, 3 * BTN_SIZE, BTN_SIZE))
    dec_text = font.render("Slow down", True, (14, 28, 54)) # TODO: change text in button and refactor colour
    dec_textRect = dec_text.get_rect()
    dec_textRect.center = (dec_timestep_button.center[0], dec_timestep_button.center[1])
    screen.blit(dec_text, dec_textRect)

    # generation counter
    generation_counter = pygame.draw.rect(screen, BTN_COLOUR, pygame.Rect(220, WIN_SIZE + 10, 3 * BTN_SIZE, BTN_SIZE))
    gen_text = font.render(f"Gen: {generations}", True, (14, 28, 54)) # TODO: change text in button and refactor colour
    gen_textRect = gen_text.get_rect()
    gen_textRect.center = (generation_counter.center[0], generation_counter.center[1])
    screen.blit(gen_text, gen_textRect)

    # restart
    restart_button = pygame.draw.rect(screen, BTN_COLOUR, pygame.Rect(325, WIN_SIZE + 10, 3 * BTN_SIZE, BTN_SIZE))
    restart_text = font.render("Restart", True, (14, 28, 54)) # TODO: change text in button and refactor colour
    restart_textRect = restart_text.get_rect()
    restart_textRect.center = (restart_button.center[0], restart_button.center[1])
    screen.blit(restart_text, restart_textRect)

    # Pause/Resume
    pr_button = pygame.draw.rect(screen, BTN_COLOUR, pygame.Rect(430, WIN_SIZE + 10, 4.5 * BTN_SIZE, BTN_SIZE))
    pr_text = font.render("Pause/Resume", True, (14, 28, 54)) # TODO: change text in button and refactor colour
    pr_textRect = pr_text.get_rect()
    pr_textRect.center = (pr_button.center[0], pr_button.center[1])
    screen.blit(pr_text, pr_textRect)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 5 frames per second
    clock.tick(time_step)
 
# Close the window and quit.
pygame.quit()