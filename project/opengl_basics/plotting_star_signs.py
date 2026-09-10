# import pygame is used to access the pygame module
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init() # Initialize the pygame module

screen_width = 1000
screen_height = 800


screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL) # Set the display mode to OpenGL and double buffering enabled, this is the default mode

pygame.display.set_caption("Hello OpenGL") # Set the title of the window

# orthographic for 2D
def init_orthographic():
    glMatrixMode(GL_PROJECTION) # Set the matri
    glLoadIdentity() # Cleans the matrix
    gluOrtho2D(0, 640, 0, 480) # Set the orthographic projection

done = False

init_orthographic()
while not done:
    for event in pygame.event.get(): # Get all the events that have happened
        if event.type == pygame.QUIT:
            done = True


    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Clear anything to do with depth and color

    glMatrixMode(GL_MODELVIEW) # Sets OpenGL to start drawing in the model coordinate system

    glLoadIdentity() # Cleans whatever is in the model view

    glPointSize(10) # Set the point size to 5 pixels



    glBegin(GL_POINTS) # Start drawing points
    # {
    # } 
    glEnd() # End drawing points


    pygame.display.flip() # Update the display
    pygame.time.wait(100) # Wait for 10 milliseconds
    
    




pygame.quit() # Quit the program
