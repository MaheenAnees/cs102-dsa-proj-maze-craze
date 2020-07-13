import pygame, time, random

x = 0           # x axis
y = 0           # y axis
width = int(input('Enter your width'))          # width of the block
grid = []
visited = []
stack = []
solution = {}



width_of_the_window = 1000
height_of_the_window = 1000


red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)

#initialize pygame
pygame.init()                              
screen = pygame.display.set_mode((width_of_the_window, height_of_the_window))
pygame.display.set_caption('MAZE CRAZE')                                          #Set the current window caption


#stack function
def push(stack, item):
    stack.append(item)



    
#making nxn grid
def empty_maze(x, y, width):
    for i in range(1, width + 1):
        x = width                                                                 # set x coordinate to start position
        y = y + width                                                             # move to the next row
        for j in range(1, width + 1):
            pygame.draw.line(screen, yellow, [x, y], [x + width, y])                       # draw towards the right of block
            pygame.draw.line(screen, yellow, [x + width, y], [x + width, y + width])       # draw towards the top of block
            pygame.draw.line(screen, yellow, [x + width, y + width], [x, y + width])       # draw towards the left of block
            pygame.draw.line(screen, yellow, [x, y + width], [x, y])                       # draw towards down of block
            push(grid,(x, y))                                                              # append the coordinate of block to grid list
            x = x + width                                                                  # move block to new position
            




def down(x, y):
    pygame.draw.rect(screen, red, (x +  1, y + 1, width - 1, (2*width) - 1), 0)
    pygame.display.update()

def up(x, y):
    pygame.draw.rect(screen, red, (x + 1, y - width + 1, width - 1, (2*width) - 1), 0)         # draw a rectangle twice the width of the block
    pygame.display.update()                                                                    # Update portions of the screen for software displays and animate the wall being removed


def right(x, y):
    pygame.draw.rect(screen, red, (x + 1, y + 1, (2*width) - 1, width - 1), 0)
    pygame.display.update()

def left(x, y):
    pygame.draw.rect(screen, red, (x - width + 1, y + 1, (2*width) - 1, width - 1), 0)
    pygame.display.update()

def backtracking(x, y):
    pygame.draw.rect(screen, red, (x + 1, y + 1, width - 2, width - 2), 0)             # used to re-colour the path_traversal after single_block
    pygame.display.update()                                                            # has visited block

def single_block(x, y):
    pygame.draw.rect(screen, yellow, (x + 1, y + 1, width - 2, width - 2), 0)          # draw a single width block
    pygame.display.update()

def solution_block(x, y):
    pygame.draw.rect(screen, green, (x + 8, y + 8, width // 4, width // 4), 0)             # used to show the solution
    pygame.display.update()                                                                # has visited block

def make_maze(x,y):
    single_block(x, y)                                              # starting positing of maze
    push(stack,(x, y))                                              # place starting block into stack
    push(visited,(x, y))                                            # add starting block to visited list
    while len(stack) > 0:                                           # loop until stack is empty
        time.sleep(.07)                                             # slow program now a bit
        block = []                                                  # define block list
        if (x + width, y) not in visited and (x + width, y) in grid:       # right block available?
            push(block, "right")                                           # if yes add to block list

        if (x - width, y) not in visited and (x - width, y) in grid:       # left block available?
            push(block, "left")

        if (x , y + width) not in visited and (x , y + width) in grid:     # down block available?
            push(block, "down")

        if (x, y - width) not in visited and (x , y - width) in grid:      # up block available?
            push(block, "up")

        if len(block) > 0:                                           # check to see if block list is empty
            choose_block = (random.choice(block))                    # select one of the block randomly

            if choose_block == "right":                             # if this block has been chosen
                right(x, y)                                         # call right function
                solution[(x + width, y)] = x, y                     # solution = dictionary key = new block, other = current block
                x = x + width                                       # make this block the current block
                push(visited,(x, y))                                # add to visited list
                push(stack,(x, y))                                  # place current block on to stack

            elif choose_block == "down":
                down(x, y)
                solution[(x , y + width)] = x, y
                y = y + width
                push(visited,(x, y))
                push(stack,(x, y))

            elif choose_block == "up":
                up(x, y)
                solution[(x , y - width)] = x, y
                y = y - width
                push(visited,(x, y))
                push(stack,(x, y))
                
            elif choose_block == "left":
                left(x, y)
                solution[(x - width, y)] = x, y
                x = x - width
                push(visited,(x, y))
                push(stack,(x, y))

            
        else:
            x, y = stack.pop()                                     # if no blocks are available pop one from the stack
            single_block(x, y)                                     # use single_block function to show backtracking image
            time.sleep(.05)                                        # slow program down a bit
            backtracking(x, y)                                     # change colour to yellow to identify backtracking path_traversal


def path_traversal(x,y):
    solution_block(x, y)                                          # solution list contains all the coordinates to route back to start
    while (x, y) != (width, width):                               # loop until block position == start position
        x, y = solution[x, y]                                     # "key value" now becomes the new key
        solution_block(x, y)                                      # animate route back
        time.sleep(.1)



x, y = width, width                         # starting position of grid
empty_maze(40, 0, width)                    # 1st argument = x value, 2nd argument = y value, 3rd argument = width of block
make_maze(x, y)                             # call build the maze  function
path_traversal(width**2, width**2)          # call the solution function


## pygame loop ####
done = False
while done == False:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
           done = True 
pygame.quit()
