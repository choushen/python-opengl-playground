import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


pygame.init() # Initialize the pygame module

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL) # Set the display mode to OpenGL and double buffering enabled, this is the default mode

pygame.display.set_caption("Zodiac Signs") # Set the title of the window

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

    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex2i(200, 200)  # Vertex 1 - Center point
    glVertex2i(270, 260)  # Vertex 2
    glVertex2i(360, 255)  # Vertex 3
    glVertex2i(425, 290)  # Vertex 4
    glEnd()

    glPointSize(4)
    glBegin(GL_POINTS)
    glVertex2i(260, 210)  # Vertex 6
    glVertex2i(380, 190)  # Vertex 7
    glVertex2i(370, 280)
    glVertex2i(410, 305)
    glEnd()

    glBegin(GL_LINES)
    # {
    glVertex2i(200, 200)
    glVertex2i(270, 260)

    glVertex2i(270, 260)
    glVertex2i(360, 255)

    glVertex2i(360, 255) 
    glVertex2i(370, 280)

    glVertex2i(200, 200)
    glVertex2i(260,210)

    glVertex2i(260,210)
    glVertex2i(380,190)

    glVertex2i(380, 190)
    glVertex2i(360, 255) 

    glVertex2i(370, 280)
    glVertex2i(410, 305)
    
    glVertex2i(410, 305)
    glVertex2i(425, 290)

    # }
    glEnd()



    pygame.display.flip() # Update the display
    pygame.time.wait(100) # Wait for 10 milliseconds
    
pygame.quit() # Quit the program