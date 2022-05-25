
import pygame
import tkinter as tk
from tkinter import messagebox


# defining cube object class i.e the snack the snake will consume to grow
class cube(object) :
    rows = 0
    w = 0

    # defining methods for cube class
    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass

# defining snake class and all its methods
class snake(object):

    # defining methods for snake class
    def __init__(self, color, pos):
        pass

    def move(self):
        pass

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        pass


# defining all other function to make the game work
def drawGrid(w, rows, surface):
    pass

def redrawWindow(surface):
    pass

def randomSnack(rows, items):
    pass

def message_box(subject, content):
    pass

    
# defining main function and main loop  
def main():
    width = 800
    height = 600
    rows = 20
    win = pygame.display.set_mode((width, height))
    s = snake((255, 0, 0), (10, 10))