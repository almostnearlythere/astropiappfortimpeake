#!/usr/bin/python
import pygame

from pygame.locals import *
from sense_hat import AstroPi

pygame.init()
pygame.display.set_mode((640,480))
ap = AstroPi()

import sys

ap.show_message ("Game 1",text_colour=[255,0,50])
from random import *

y = [randint(1, 6), randint(1, 6), randint(1, 6)]
print(y)

import time

ap.show_letter (str(y[0]),text_colour=[255,0,0])
time.sleep(1)
ap.clear()
ap.show_letter (str(y[1]),text_colour=[255,0,0])
time.sleep(1)
ap.clear()
ap.show_letter (str(y[2]),text_colour=[255,0,0])
time.sleep(1)

ap.clear()
time.sleep(3)
import time
from pygame.locals import *
x = 0
score = 0
running = True


while (x < 6):
            x = sum = x + 1
            ap.show_letter (str(x),text_colour=[255,0,50])
            time.sleep(3)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        print(event)
                        if y[0] == ((x)):   
                            score = sum = score + 1
                            time.sleep(1)
                        elif y[1] == ((x)):   
                            score = sum = score + 1
                            time.sleep(1)
                        elif y[2] == ((x)):   
                           score = sum = score + 1
                           time.sleep(1)
                        else:
                            score = sum = score - 1



time.sleep(1)
ap.show_message((str(score),text_colour==[255,0,50])

    time.sleep(0.5)
ap.show_message ("Game 2",text_colour=[255,0,50])

from random import *
import time

xy = [randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9)]

ap.show_letter (str(xy[0]),text_colour=[255,0,0])
time.sleep(1)
ap.clear() 
ap.show_letter (str(xy[1]),text_colour=[255,0,0])
time.sleep(1)
ap.clear()
ap.show_letter (str(xy[2]),text_colour=[255,0,0])
time.sleep(1)
ap.clear()
ap.show_letter (str(xy[3]),text_colour=[255,0,0])
time.sleep(1)
ap.clear()
ap.show_letter (str(xy[4])),text_colour=[255,0,0]
time.sleep(1)
ap.clear()
ap.show_letter (str(xy[5])),text_colour=[255,0,0]
time.sleep(1)
ap.clear()

time.sleep(0.5)
import time
x = 0
score2 = 0
while (x < 9):
        time.sleep(3)
        x = sum = x + 1
        ap.show_letter (str(x)),text_colour=[255,0,50]
        time.sleep(1)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    print(event)           
                    if xy[0] == (x):   
                        score2 = sum = score2 + 1
                        time.sleep(1)
                    elif xy[1] == (x):   
                        score2 = sum = score2 + 1
                        time.sleep(1)
                    elif xy[2] == x:   
                       score2 = sum = score2 + 1
                       time.sleep(1)
                    elif xy[3] == x:   
                        score2 = sum = score2 + 1
                        time.sleep(1)
                    elif xy[4] == x:   
                        score2 = sum = score2 + 1
                        time.sleep(1)
                    elif xy[5] == x:   
                       score2 = sum = score2 + 1
                       time.sleep(1)
                    else:
                        score2 = sum = score2 - 1

time.sleep(2)
ap.show_message(str(score2),text_colour=[255,0,50])

from random import *

ap.show_message("Game 3"),text_colour=[255,0,50]
z = [randint(1, 6), randint(1, 6), randint(1, 6)]
print(z)

import time
ap.show_letter (str(z[0])),text_colour=[255,0,0]
time.sleep(0.5)
ap.clear()
ap.show_letter (str(z[1])),text_colour=[255,0,0]
time.sleep(0.5)
ap.clear()
ap.show_letter (str(z[2])),text_colour=[255,0,0]
time.sleep(0.5)

ap.clear()
time.sleep(3)
import time
from pygame.locals import *
x = 0
score3 = 0
running = True


while (x < 6):
            x = sum = x + 1
            ap.show_letter (str(x)),text_colour=[255,0,50]
            time.sleep(3)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        print(event)
                        if z[0] == ((x)):   
                            score3 = sum = score3 + 1
                            time.sleep(1)
                        elif z[1] == ((x)):   
                            score3 = sum = score3 + 1
                            time.sleep(1)
                        elif z[2] == ((x)):   
                           score3 = sum = score3 + 1
                           time.sleep(1)
                        else:
                            score3 = sum = score3 - 1



time.sleep(1)
ap.show_message((str(score)),text_colour=[255,0,50])

time.sleep(0.5)
ap.show_message ("Game 4",text_colour=[255,0,50])

from random import *
import time

a = [randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9)]
ap.show_letter (str(a[0]))
time.sleep(1)

ap.clear()
ap.show_letter (str(a[1])),text_colour=[255,0,0]
time.sleep(0.5)
ap.clear()
ap.show_letter (str(a[2])),text_colour=[255,0,0]
time.sleep(0.5)
ap.clear()
ap.show_letter (str(a[3])),text_colour=[255,0,0]
time.sleep(0.5)
ap.clear()
ap.show_letter (str(a[4])),text_colour=[255,0,0]
time.sleep(0.5)
ap.clear()
ap.show_letter (str(a[5])),text_colour=[255,0,0]
time.sleep(0.5)
ap.clear()

time.sleep(0.5)
import time
x = 0
score4 = 0
while (x < 9):
        time.sleep(3)
        x = sum = x + 1
        ap.show_letter (str(x)),text_colour=[255,0,50]
        time.sleep(1)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    print(event)           
                    if a[0] == (x):   
                        score4 = sum = score4 + 1
                        time.sleep(1)
                    elif a[1] == (x):   
                        score4 = sum = score4 + 1
                        time.sleep(1)
                    elif a[2] == x:   
                       score4 = sum = score4 + 1
                       time.sleep(1)
                    elif a[3] == x:   
                        score4 = sum = score4 + 1
                        time.sleep(1)
                    elif a[4] == x:   
                        score4 = sum = score4 + 1
                        time.sleep(1)
                    elif a[5] == x:   
                       score4 = sum = score4 + 1
                       time.sleep(1)
                    else:
                        score4 = sum = score4 - 1

time.sleep(2)
ap.show_message(str(score2),text_colour=[255,0,50])
ap.show_message("Thank you for playing."),text_colour=[255,0,50]

quit

