import pygame
import time
from pygame.locals import *
import os
import sys
import math
import random


os.environ['SDL_VIDEO_CENTERED'] = '1'


pygame.init()
info = pygame.display.Info()
screen_width,screen_height = info.current_w,info.current_h
worldx  = screen_width-20
worldy = screen_height-50
curr = 2
barrCount = [20,20,15]
mouseTrack = 1
starter = 0
escTrack = 1

if starter:
    pygame.init()
    win = pygame.display.set_mode((screen_width-20, screen_height-50),pygame.FULLSCREEN)
else:
    pygame.init()
    win = pygame.display.set_mode((screen_width-screen_width//2,screen_height-screen_height//4))
    win.fill([255,255,255])

pygame.display.set_caption("SHAB AND AYU ")
bgtrack = 0
win_width = win.get_width()
win_height = win.get_height()

bulletSound = pygame.mixer.Sound('weapon.wav')
monster = pygame.mixer.Sound('monster.wav')
hitSound = pygame.mixer.Sound('hit.wav')
deadsong = pygame.mixer.Sound("gameover.wav")
music = pygame.mixer.music.load('back.wav')
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(-1)

bg = [pygame.transform.scale((pygame.image.load('bg1.png').convert_alpha()),(screen_width-20,screen_height-50)),
      pygame.transform.scale((pygame.image.load('bg2.png').convert_alpha()),(screen_width-20,screen_height-50)),
      pygame.transform.scale((pygame.image.load('bg3.png').convert_alpha()),(screen_width-20,screen_height-50)),
      pygame.transform.scale((pygame.image.load('bg4.png').convert_alpha()),(screen_width-20,screen_height-50))]

grass = [pygame.transform.scale((pygame.image.load('Grass/G1.png').convert_alpha()),(screen_width-20,screen_height-50)),
        pygame.transform.scale((pygame.image.load('Grass/G2.png').convert_alpha()),(screen_width-20,screen_height-50)),
        pygame.transform.scale((pygame.image.load('Grass/G3.png').convert_alpha()),(screen_width-20,screen_height-50)),
        pygame.transform.scale((pygame.image.load('Grass/G4.png').convert_alpha()),(screen_width-20,screen_height-50))]

bar = [pygame.transform.scale((pygame.image.load('bars/b1.png').convert_alpha()), (200, 80)),
       pygame.transform.scale((pygame.image.load('bars/b2.png').convert_alpha()), (200, 80)),
       pygame.transform.scale((pygame.image.load('bars/b3.png').convert_alpha()), (200, 80)),
       pygame.transform.scale((pygame.image.load('bars/b4.png').convert_alpha()), (200, 80)),
       pygame.transform.scale((pygame.image.load('bars/b5.png').convert_alpha()), (200, 80)),
       pygame.transform.scale((pygame.image.load('bars/b6.png').convert_alpha()), (200, 80))
  ]

Art4Menu = [ pygame.transform.scale((pygame.image.load('CONTROL.jpg').convert_alpha()),(win.get_width(),win.get_height())) ,pygame.transform.scale((pygame.image.load('Aboutus.jpg').convert_alpha()),(win.get_width(),win.get_height()))
             ,pygame.transform.scale((pygame.image.load('back.png').convert_alpha()),(40,30))]


# Enemy .....................................................................................

Emenu =     [pygame.transform.scale((pygame.image.load('ENEM/E2R1.png').convert_alpha()), (200, 230)),
             pygame.transform.scale((pygame.image.load('ENEM/E2R2.png').convert_alpha()), (200, 230)),
             pygame.transform.scale((pygame.image.load('ENEM/E2R3.png').convert_alpha()), (200, 230)),
             pygame.transform.scale((pygame.image.load('ENEM/E2R4.png').convert_alpha()), (200, 230)),
             pygame.transform.scale((pygame.image.load('ENEM/E2R5.png').convert_alpha()), (200, 230)),
             pygame.transform.scale((pygame.image.load('ENEM/E2R6.png').convert_alpha()), (200, 230)),
             pygame.transform.scale((pygame.image.load('ENEM/E2R7.png').convert_alpha()), (200, 230)),
             pygame.transform.scale((pygame.image.load('ENEM/E2R8.png').convert_alpha()), (200, 230)),
             pygame.transform.scale((pygame.image.load('ENEM/E2R9.png').convert_alpha()), (200, 230)),
             pygame.transform.scale((pygame.image.load('ENEM/E2R10.png').convert_alpha()), (200, 230))]

Ewalk =[ [[pygame.transform.scale((pygame.image.load('ENEM/1.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/2.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/3.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/4.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/5.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/6.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/7.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/8.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/9.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/10.png').convert_alpha()), (300, 400))],

            [pygame.transform.scale((pygame.image.load('ENEM/E1R1.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E1R2.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E1R3.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E1R4.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E1R5.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E1R6.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E1R7.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E1R8.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E1R9.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E1R10.png').convert_alpha()), (300, 400))]
          ]

    ,
         [[pygame.transform.scale((pygame.image.load('ENEM/E1.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E2.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E3.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E4.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E5.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E6.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E7.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E8.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E9.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E10.png').convert_alpha()), (300, 400))],

          [pygame.transform.scale((pygame.image.load('ENEM/E2R1.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E2R2.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E2R3.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E2R4.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E2R5.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E2R6.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E2R7.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E2R8.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E2R9.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E2R10.png').convert_alpha()), (300, 400))]]

         ,[[pygame.transform.scale((pygame.image.load('ENEM/E3L1.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E3L2.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E3L3.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E3L4.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E3L5.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E3L6.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E3L7.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E3L8.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E3L9.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E3L10.png').convert_alpha()), (300, 400))],

          [pygame.transform.scale((pygame.image.load('ENEM/E3R1.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E3R2.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E3R3.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E3R4.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E3R5.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E3R6.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E3R7.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E3R8.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E3R9.png').convert_alpha()), (300, 400)),
             pygame.transform.scale((pygame.image.load('ENEM/E3R10.png').convert_alpha()), (300, 400))]]

         ]

EAttack = [
           [[pygame.transform.scale((pygame.image.load('attack/1.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/2.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/3.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/4.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/5.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/6.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/7.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/8.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/9.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/10.png').convert_alpha()), (300, 400))],

            [pygame.transform.scale((pygame.image.load('attack/E1A1.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E1A2.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E1A3.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E1A4.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E1A5.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E1A6.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E1A7.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E1A8.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E1A9.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E1A10.png').convert_alpha()), (300, 400))]
           ],
            [[pygame.transform.scale((pygame.image.load('attack/E2A1.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E2A2.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E2A3.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E2A4.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E2A5.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E2A6.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E2A7.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E2A8.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E2A9.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E2A10.png').convert_alpha()), (300, 400))]
            ,
             [pygame.transform.scale((pygame.image.load('attack/E2AR1.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E2AR2.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E2AR3.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E2AR4.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E2AR5.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E2AR6.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E2AR7.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E2AR8.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E2AR9.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E2AR10.png').convert_alpha()), (300, 400))]
             ],
[[pygame.transform.scale((pygame.image.load('attack/E3LA1.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E3LA2.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E3LA3.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E3LA4.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E3LA5.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E3LA6.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E3LA7.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E3LA8.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E3LA9.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E3LA10.png').convert_alpha()), (300, 400))]
            ,
             [pygame.transform.scale((pygame.image.load('attack/E3AR1.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E3AR2.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E3AR3.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E3AR4.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E3AR5.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E3AR6.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E3AR7.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E3AR8.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E3AR9.png').convert_alpha()), (300, 400)),
           pygame.transform.scale((pygame.image.load('attack/E3AR10.png').convert_alpha()), (300, 400))]
             ]
]

# .......................................................................................

# Player.....................................................................................................
pmenu =         [pygame.transform.scale((pygame.image.load('p1/R1.png').convert_alpha()), (90, 90)),
                pygame.transform.scale((pygame.image.load('p1/R2.png').convert_alpha()), (90, 90)),
                pygame.transform.scale((pygame.image.load('p1/R3.png').convert_alpha()), (90, 90)),
                pygame.transform.scale((pygame.image.load('p1/R4.png').convert_alpha()), (90, 90)),
                pygame.transform.scale((pygame.image.load('p1/R5.png').convert_alpha()), (90, 90)),
                pygame.transform.scale((pygame.image.load('p1/R6.png').convert_alpha()), (90, 90)),
                pygame.transform.scale((pygame.image.load('p1/R7.png').convert_alpha()), (90, 90)),
                pygame.transform.scale((pygame.image.load('p1/R8.png').convert_alpha()), (90, 90)),
                pygame.transform.scale((pygame.image.load('p1/R9.png').convert_alpha()), (90, 90)),
                pygame.transform.scale((pygame.image.load('p1/R10.png').convert_alpha()), (90, 90))]

player1Right = [pygame.transform.scale((pygame.image.load('p1/R1.png').convert_alpha()), (120, 120)),
                pygame.transform.scale((pygame.image.load('p1/R2.png').convert_alpha()), (120, 120)),
                pygame.transform.scale((pygame.image.load('p1/R3.png').convert_alpha()), (120, 120)),
                pygame.transform.scale((pygame.image.load('p1/R4.png').convert_alpha()), (120, 120)),
                pygame.transform.scale((pygame.image.load('p1/R5.png').convert_alpha()), (120, 120)),
                pygame.transform.scale((pygame.image.load('p1/R6.png').convert_alpha()), (120, 120)),
                pygame.transform.scale((pygame.image.load('p1/R7.png').convert_alpha()), (120, 120)),
                pygame.transform.scale((pygame.image.load('p1/R8.png').convert_alpha()), (120, 120)),
                pygame.transform.scale((pygame.image.load('p1/R9.png').convert_alpha()), (120, 120)),
                pygame.transform.scale((pygame.image.load('p1/R10.png').convert_alpha()), (120, 120))]

player1Left = [pygame.transform.scale((pygame.image.load('p1/L1.png').convert_alpha()), (120, 120)),
               pygame.transform.scale((pygame.image.load('p1/L2.png').convert_alpha()), (120, 120)),
               pygame.transform.scale((pygame.image.load('p1/L3.png').convert_alpha()), (120, 120)),
               pygame.transform.scale((pygame.image.load('p1/L4.png').convert_alpha()), (120, 120)),
               pygame.transform.scale((pygame.image.load('p1/L5.png').convert_alpha()), (120, 120)),
               pygame.transform.scale((pygame.image.load('p1/L6.png').convert_alpha()), (120, 120)),
               pygame.transform.scale((pygame.image.load('p1/L7.png').convert_alpha()), (120, 120)),
               pygame.transform.scale((pygame.image.load('p1/L8.png').convert_alpha()), (120, 120)),
               pygame.transform.scale((pygame.image.load('p1/L9.png').convert_alpha()), (120, 120)),
               pygame.transform.scale((pygame.image.load('p1/L10.png').convert_alpha()), (120, 120))]

player1Standing = [pygame.transform.scale((pygame.image.load("p1/SL.png").convert_alpha()), (80, 120)),
                   pygame.transform.scale((pygame.image.load("p1/SR.png").convert_alpha()), (80, 120))]

p1dead = [[ pygame.transform.scale((pygame.image.load('p1/DL1.png').convert_alpha()),(120,120)),pygame.transform.scale((pygame.image.load('p1/DL2.png').convert_alpha()),(120,120)),
            pygame.transform.scale((pygame.image.load('p1/DL3.png').convert_alpha()),(120,120)),pygame.transform.scale((pygame.image.load('p1/DL4.png').convert_alpha()),(120,120)),
            pygame.transform.scale((pygame.image.load('p1/DL5.png').convert_alpha()),(120,120)),pygame.transform.scale((pygame.image.load('p1/DL6.png').convert_alpha()),(120,120))
           ,pygame.transform.scale((pygame.image.load('p1/DL7.png').convert_alpha()),(120,120)),pygame.transform.scale((pygame.image.load('p1/DL8.png').convert_alpha()),(120,120))
           ,pygame.transform.scale((pygame.image.load('p1/DL9.png').convert_alpha()),(120,120)),pygame.transform.scale((pygame.image.load('p1/DL10.png').convert_alpha()),(120,120))],

            [pygame.transform.scale((pygame.image.load('p1/DR1.png').convert_alpha()),(120,120)),pygame.transform.scale((pygame.image.load('p1/DR2.png').convert_alpha()),(120,120)),
            pygame.transform.scale((pygame.image.load('p1/DR3.png').convert_alpha()),(120,120)),pygame.transform.scale((pygame.image.load('p1/DR4.png').convert_alpha()),(120,120)),
            pygame.transform.scale((pygame.image.load('p1/DR5.png').convert_alpha()),(120,120)),pygame.transform.scale((pygame.image.load('p1/DR6.png').convert_alpha()),(120,120))
           ,pygame.transform.scale((pygame.image.load('p1/DR7.png').convert_alpha()),(120,120)),pygame.transform.scale((pygame.image.load('p1/DR8.png').convert_alpha()),(120,120))
           ,pygame.transform.scale((pygame.image.load('p1/DR9.png').convert_alpha()),(120,120)),pygame.transform.scale((pygame.image.load('p1/DR10.png').convert_alpha()),(120,120))]
          ]
p1flying = [[ pygame.transform.scale((pygame.image.load('p1/FL1.png').convert_alpha()),(120,120)),pygame.transform.scale((pygame.image.load('p1/FL2.png').convert_alpha()),(120,120)),
            pygame.transform.scale((pygame.image.load('p1/FL3.png').convert_alpha()),(120,120)),pygame.transform.scale((pygame.image.load('p1/FL4.png').convert_alpha()),(120,120)),
            pygame.transform.scale((pygame.image.load('p1/FL5.png').convert_alpha()),(120,120)),pygame.transform.scale((pygame.image.load('p1/FL6.png').convert_alpha()),(120,120))
           ,pygame.transform.scale((pygame.image.load('p1/FL7.png').convert_alpha()),(120,120)),pygame.transform.scale((pygame.image.load('p1/FL8.png').convert_alpha()),(120,120))
           ,pygame.transform.scale((pygame.image.load('p1/FL9.png').convert_alpha()),(120,120)),pygame.transform.scale((pygame.image.load('p1/FL10.png').convert_alpha()),(120,120))],

            [pygame.transform.scale((pygame.image.load('p1/FR1.png').convert_alpha()),(120,120)),pygame.transform.scale((pygame.image.load('p1/FR2.png').convert_alpha()),(120,120)),
            pygame.transform.scale((pygame.image.load('p1/FR3.png').convert_alpha()),(120,120)),pygame.transform.scale((pygame.image.load('p1/FR4.png').convert_alpha()),(120,120)),
            pygame.transform.scale((pygame.image.load('p1/FR5.png').convert_alpha()),(120,120)),pygame.transform.scale((pygame.image.load('p1/FR6.png').convert_alpha()),(120,120))
           ,pygame.transform.scale((pygame.image.load('p1/FR7.png').convert_alpha()),(120,120)),pygame.transform.scale((pygame.image.load('p1/FR8.png').convert_alpha()),(120,120))
           ,pygame.transform.scale((pygame.image.load('p1/FR9.png').convert_alpha()),(120,120)),pygame.transform.scale((pygame.image.load('p1/FR10.png').convert_alpha()),(120,120))]
          ]

p1attack = [[ pygame.transform.scale((pygame.image.load('p1/AL1.png').convert_alpha()),(180,120)),pygame.transform.scale((pygame.image.load('p1/AL2.png').convert_alpha()),(180,120)),
            pygame.transform.scale((pygame.image.load('p1/AL3.png').convert_alpha()),(180,120)),pygame.transform.scale((pygame.image.load('p1/AL4.png').convert_alpha()),(180,120)),
            pygame.transform.scale((pygame.image.load('p1/AL5.png').convert_alpha()),(180,120)),pygame.transform.scale((pygame.image.load('p1/AL6.png').convert_alpha()),(180,120))
           ,pygame.transform.scale((pygame.image.load('p1/AL7.png').convert_alpha()),(180,120)),pygame.transform.scale((pygame.image.load('p1/AL8.png').convert_alpha()),(180,120))
           ,pygame.transform.scale((pygame.image.load('p1/AL9.png').convert_alpha()),(180,120)),pygame.transform.scale((pygame.image.load('p1/AL10.png').convert_alpha()),(180,120))],

            [pygame.transform.scale((pygame.image.load('p1/AR1.png').convert_alpha()),(180,120)),pygame.transform.scale((pygame.image.load('p1/AR2.png').convert_alpha()),(180,120)),
            pygame.transform.scale((pygame.image.load('p1/AR3.png').convert_alpha()),(180,120)),pygame.transform.scale((pygame.image.load('p1/AR4.png').convert_alpha()),(180,120)),
            pygame.transform.scale((pygame.image.load('p1/AR5.png').convert_alpha()),(180,120)),pygame.transform.scale((pygame.image.load('p1/AR6.png').convert_alpha()),(180,120))
           ,pygame.transform.scale((pygame.image.load('p1/AR7.png').convert_alpha()),(180,120)),pygame.transform.scale((pygame.image.load('p1/AR8.png').convert_alpha()),(180,120))
           ,pygame.transform.scale((pygame.image.load('p1/AR9.png').convert_alpha()),(180,120)),pygame.transform.scale((pygame.image.load('p1/AR10.png').convert_alpha()),(180,120))]
          ]



# ....................................................................................................................


# Weapons .................................................................................................
weapon = [pygame.transform.scale((pygame.image.load("weapon/w0.png").convert_alpha()), (60, 60)), pygame.transform.scale((pygame.image.load("weapon/w1.png").convert_alpha()), (60, 60)),
          pygame.transform.scale((pygame.image.load("weapon/w2.png").convert_alpha()), (60, 60)), pygame.transform.scale((pygame.image.load("weapon/w3.png").convert_alpha()), (60, 60)),
          pygame.transform.scale((pygame.image.load("weapon/w4.png").convert_alpha()), (60, 60)), pygame.transform.scale((pygame.image.load("weapon/w5.png").convert_alpha()), (60, 60))
         ,pygame.transform.scale((pygame.image.load("weapon/w6.png").convert_alpha()), (60, 60)),pygame.transform.scale((pygame.image.load("weapon/w7.png").convert_alpha()), (60, 60))]

# ...................................................................................................


# Barriers ................................................................


barriers = [pygame.transform.scale((pygame.image.load("barrier/b1.png").convert_alpha()), (150, 150)),
            pygame.transform.scale((pygame.image.load("barrier/b2.png").convert_alpha()), (150, 150))
    , pygame.transform.scale((pygame.image.load("barrier/b3.png").convert_alpha()), (150, 150))]

barrierbar = [pygame.transform.scale((pygame.image.load("barrier/b1.png").convert_alpha()), (45, 45)),
            pygame.transform.scale((pygame.image.load("barrier/b2.png").convert_alpha()), (45, 45))
    , pygame.transform.scale((pygame.image.load("barrier/b3.png").convert_alpha()), (45, 45))]
# ............................................................................

# Weapon Bar .....................

weaponBar = [pygame.transform.scale((pygame.image.load("Ubar/weaponBar.png").convert_alpha()), (200, 180)) ,
             pygame.transform.scale((pygame.image.load("Ubar/swordBar.png").convert_alpha()), (250, 100)) ,
             pygame.transform.scale((pygame.image.load("Ubar/healthBar.png").convert_alpha()), (100, 100)),
             pygame.transform.scale((pygame.image.load("Ubar/gemsbar.png").convert_alpha()), (200, 90)),
            pygame.transform.scale((pygame.image.load("Ubar/next0.png").convert_alpha()), (30, 40)),
            pygame.transform.scale((pygame.image.load("Ubar/next1.png").convert_alpha()), (20, 20)),
            pygame.transform.scale((pygame.image.load("Ubar/next2.png").convert_alpha()), (30, 40)),
            pygame.transform.scale((pygame.image.load("Ubar/next3.png").convert_alpha()), (20, 20))
             ]
weapontype = [pygame.transform.scale((pygame.image.load("weapon/w0.png").convert_alpha()), (70, 70)) , pygame.transform.scale((pygame.image.load("weapon/w1.png").convert_alpha()), (70, 70))
              ,pygame.transform.scale((pygame.image.load("weapon/w2.png").convert_alpha()), (70, 70)),pygame.transform.scale((pygame.image.load("weapon/w3.png").convert_alpha()), (70, 70)),
              pygame.transform.scale((pygame.image.load("weapon/w4.png").convert_alpha()), (70, 70)) , pygame.transform.scale((pygame.image.load("weapon/w5.png").convert_alpha()), (70, 70))
              ,pygame.transform.scale((pygame.image.load("weapon/w6.png").convert_alpha()), (70, 70)),pygame.transform.scale((pygame.image.load("weapon/w7.png").convert_alpha()), (70, 70))]
# . . . .. . . . . .. . . . . .

# Bomb Blast . . . . . . . . . .. .. .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .

fireblastlist =[ [pygame.transform.scale((pygame.image.load("Boom/ba1.png").convert_alpha()),(200,200)) ,pygame.transform.scale((pygame.image.load("Boom/ba2.png").convert_alpha()),(200,200))
                  ,pygame.transform.scale((pygame.image.load("Boom/ba3.png").convert_alpha()),(200,200)),pygame.transform.scale((pygame.image.load("Boom/ba4.png").convert_alpha()),(200,200))
                  ,pygame.transform.scale((pygame.image.load("Boom/ba5.png").convert_alpha()),(200,200)),pygame.transform.scale((pygame.image.load("Boom/ba6.png").convert_alpha()),(200,200))
                  ,pygame.transform.scale((pygame.image.load("Boom/ba7.png").convert_alpha()),(200,200)),pygame.transform.scale((pygame.image.load("Boom/ba8.png").convert_alpha()),(200,200))]

                 ,[ pygame.transform.scale((pygame.image.load("stonebreak/s1.png").convert_alpha()),(300,200)),pygame.transform.scale((pygame.image.load("stonebreak/s2.png").convert_alpha()),(300,200)),
                    pygame.transform.scale((pygame.image.load("stonebreak/s3.png").convert_alpha()),(300,200)),pygame.transform.scale((pygame.image.load("stonebreak/s4.png").convert_alpha()),(300,200))
                    ,pygame.transform.scale((pygame.image.load("stonebreak/s5.png").convert_alpha()),(300,200)),pygame.transform.scale((pygame.image.load("stonebreak/s6.png").convert_alpha()),(300,200))
                    ,pygame.transform.scale((pygame.image.load("stonebreak/s8.png").convert_alpha()),(300,200)) ,pygame.transform.scale((pygame.image.load("stonebreak/s9.png").convert_alpha()),(300,200))]

                ,[pygame.transform.scale((pygame.image.load("Boom/bc1.png").convert_alpha()), (200, 200)), pygame.transform.scale((pygame.image.load("Boom/bc2.png").convert_alpha()), (200, 200))
                     , pygame.transform.scale((pygame.image.load("Boom/bc3.png").convert_alpha()), (200, 200)), pygame.transform.scale((pygame.image.load("Boom/bc4.png").convert_alpha()), (200, 200))
                     , pygame.transform.scale((pygame.image.load("Boom/bc5.png").convert_alpha()), (200, 200)), pygame.transform.scale((pygame.image.load("Boom/bc6.png").convert_alpha()), (200, 200))
                     , pygame.transform.scale((pygame.image.load("Boom/bc7.png").convert_alpha()), (200, 200)), pygame.transform.scale((pygame.image.load("Boom/bc8.png").convert_alpha()), (200, 200))]
                 ]

stoneB = [ pygame.transform.scale((pygame.image.load("stonebreak/s1.png").convert_alpha()),(200,200)),pygame.transform.scale((pygame.image.load("stonebreak/s2.png").convert_alpha()),(200,200)),
           pygame.transform.scale((pygame.image.load("stonebreak/s3.png").convert_alpha()),(200,200)),pygame.transform.scale((pygame.image.load("stonebreak/s4.png").convert_alpha()),(200,200))
           ,pygame.transform.scale((pygame.image.load("stonebreak/s5.png").convert_alpha()),(200,200)),pygame.transform.scale((pygame.image.load("stonebreak/s6.png").convert_alpha()),(200,200))
           ,pygame.transform.scale((pygame.image.load("stonebreak/s7.png").convert_alpha()),(200,200)),pygame.transform.scale((pygame.image.load("stonebreak/s8.png").convert_alpha()),(200,200))
           ,pygame.transform.scale((pygame.image.load("stonebreak/s9.png").convert_alpha()),(200,200))
           ]

motivation = [pygame.transform.scale((pygame.image.load("motivation/boom1.png").convert_alpha()),(120,120)),pygame.transform.scale((pygame.image.load("motivation/boom2.png").convert_alpha()),(120,120))
              ,pygame.transform.scale((pygame.image.load("motivation/boom3.png").convert_alpha()),(120,120)),pygame.transform.scale((pygame.image.load("motivation/boom4.png").convert_alpha()),(120,120)),
            pygame.transform.scale((pygame.image.load("motivation/boom5.png").convert_alpha()),(120,120)),pygame.transform.scale((pygame.image.load("motivation/boom6.png").convert_alpha()),(120,120))
             ,pygame.transform.scale((pygame.image.load("motivation/boom7.png").convert_alpha()),(120,120)),pygame.transform.scale((pygame.image.load("motivation/boom8.png").convert_alpha()),(120,120))
              ]

gems = [pygame.transform.scale((pygame.image.load("gems/gem1.png").convert_alpha()),(40,40)), pygame.transform.scale((pygame.image.load("gems/gem2.png").convert_alpha()),(40,40))
        ,pygame.transform.scale((pygame.image.load("gems/gem3.png").convert_alpha()),(40,40)), pygame.transform.scale((pygame.image.load("gems/gem4.png").convert_alpha()),(40,40))
        , pygame.transform.scale((pygame.image.load("gems/gem5.png").convert_alpha()),(40,40))]

gemsrecord = [pygame.transform.scale((pygame.image.load("gems/gem1.png").convert_alpha()),(25,25)), pygame.transform.scale((pygame.image.load("gems/gem2.png").convert_alpha()),(25,25))
        ,pygame.transform.scale((pygame.image.load("gems/gem3.png").convert_alpha()),(25,25)), pygame.transform.scale((pygame.image.load("gems/gem4.png").convert_alpha()),(25,25))
        , pygame.transform.scale((pygame.image.load("gems/gem5.png").convert_alpha()),(25,25))]
#  . . . . . . . . . . . . . . . . . .. ... . .. ...

stonecloudlist = []




#  Menu and Starting . ..  . .. ..  .. . ....  . ..  ..  . . . . . . . . . .. .  . . . . .. . . ..    . . . . . . .

menuimg = [pygame.transform.scale((pygame.image.load("heading.png").convert_alpha()),(screen_width//2-40,100))]

pauseMenu = [pygame.transform.scale((pygame.image.load("mbg.jpg").convert_alpha()),(win_width//2,win_height//2)),
             pygame.transform.scale((pygame.image.load("menu.png").convert_alpha()),(700,700))
            ,pygame.transform.scale((pygame.image.load("pMenu/nl.png").convert_alpha()),(20,50))
            ,pygame.transform.scale((pygame.image.load("pMenu/nr.png").convert_alpha()),(20,50))
             ,pygame.transform.scale((pygame.image.load("pMenu/buy.png").convert_alpha()),(60,20))]

pauseMenuWeapon =[pygame.transform.scale((pygame.image.load("weapon/w0.png").convert_alpha()), (120, 120)), pygame.transform.scale((pygame.image.load("weapon/w1.png").convert_alpha()), (120, 120)),
          pygame.transform.scale((pygame.image.load("weapon/w2.png").convert_alpha()), (120, 120)), pygame.transform.scale((pygame.image.load("weapon/w3.png").convert_alpha()), (120, 120)),
          pygame.transform.scale((pygame.image.load("weapon/w4.png").convert_alpha()), (120, 120)), pygame.transform.scale((pygame.image.load("weapon/w5.png").convert_alpha()), (120, 120))
         ,pygame.transform.scale((pygame.image.load("weapon/w6.png").convert_alpha()), (120, 120)),pygame.transform.scale((pygame.image.load("weapon/w7.png").convert_alpha()), (120, 120))]

pauseMenuWeapon2 = [pygame.transform.scale((pygame.image.load("barrier/b1.png").convert_alpha()), (150, 150)),
            pygame.transform.scale((pygame.image.load("barrier/b2.png").convert_alpha()), (150, 150))
    , pygame.transform.scale((pygame.image.load("barrier/b3.png").convert_alpha()), (150, 150))]

weapomNameList = ["   Cannon" ,"  Fire Ring" , "  Fire Rod" ,"  Bush Fire" , "   Blades" , " Holy Water",  "Corona Virus" , "  Holy Ring"]
weapon2list = ["Mountain Rock" , "Wooden Blocks" , "Muddy Rock"]

gemsSize = (25,25)

gemsWalllet = [[pygame.transform.scale((pygame.image.load("gems/gem1.png").convert_alpha()),gemsSize),
             pygame.transform.scale((pygame.image.load("gems/gem2.png").convert_alpha()),gemsSize)
                , pygame.transform.scale((pygame.image.load("gems/gem4.png").convert_alpha()),gemsSize)
             ] ,
               [pygame.transform.scale((pygame.image.load("gems/gem1.png").convert_alpha()),gemsSize),
                pygame.transform.scale((pygame.image.load("gems/gem2.png").convert_alpha()),gemsSize),
                pygame.transform.scale((pygame.image.load("gems/gem4.png").convert_alpha()),gemsSize)]

               ,[pygame.transform.scale((pygame.image.load("gems/gem1.png").convert_alpha()),gemsSize),
                 pygame.transform.scale((pygame.image.load("gems/gem4.png").convert_alpha()),gemsSize),
                 pygame.transform.scale((pygame.image.load("gems/gem3.png").convert_alpha()),gemsSize)]
            ,[
                pygame.transform.scale((pygame.image.load("gems/gem4.png").convert_alpha()),gemsSize),
                pygame.transform.scale((pygame.image.load("gems/gem5.png").convert_alpha()),gemsSize)
                ,   pygame.transform.scale((pygame.image.load("gems/gem2.png").convert_alpha()),gemsSize)
               ],
               [pygame.transform.scale((pygame.image.load("gems/gem1.png").convert_alpha()),gemsSize),
                pygame.transform.scale((pygame.image.load("gems/gem2.png").convert_alpha()),gemsSize)
                , pygame.transform.scale((pygame.image.load("gems/gem4.png").convert_alpha()),gemsSize)
                ],
               [pygame.transform.scale((pygame.image.load("gems/gem4.png").convert_alpha()),gemsSize),
               pygame.transform.scale((pygame.image.load("gems/gem5.png").convert_alpha()),gemsSize)
               , pygame.transform.scale((pygame.image.load("gems/gem2.png").convert_alpha()),gemsSize)
               ],
               [pygame.transform.scale((pygame.image.load("gems/gem3.png").convert_alpha()),gemsSize),
                pygame.transform.scale((pygame.image.load("gems/gem1.png").convert_alpha()),gemsSize)
                , pygame.transform.scale((pygame.image.load("gems/gem5.png").convert_alpha()),gemsSize)
                ],

                [pygame.transform.scale((pygame.image.load("gems/gem1.png").convert_alpha()),gemsSize),
               pygame.transform.scale((pygame.image.load("gems/gem3.png").convert_alpha()),gemsSize),
               pygame.transform.scale((pygame.image.load("gems/gem4.png").convert_alpha()),gemsSize)]
                ]

gemsQuantity = [[1,2,4] , [1,2,4] , [1,2,1] , [1,2,1],[1,2,3],[2,4,3],[1,3,2],[2,1,4]]
gemsBalanceIndex = [[0,1,3],[0,1,3],[0,3,2],[3,4,1],[0,1,3],[3,4,1],[2,0,4],[0,2,3]]
smallMenuColor = [(255,255,255),(255,255,255),(255,255,255),(255,255,255)]


# ...........................................................................................

clock = pygame.time.Clock()
score = 0


class hero(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 25, self.y + 11, 60, 97)
        self.stage = 0
        self.health = 16
        self.live = True
        self.deadcount = 0
        self.flyingcount = 0
        self.attackcount = 0
        self.attack = False
        self.Tiles = False
        self.morehealth = 6
        self.rect = pygame.Rect(self.hitbox)

    def draw(self,win):
        if self.live:
            if self.walkCount + 1 > 30:
                self.walkCount = 0
            if self.jumpCount>0:
                self.flyingcount = 0

                if self.attack:
                    if self.left:
                        aindexi = 0
                    else:
                        aindexi = 1
                    if self.attackcount < 20:
                        win.blit(p1attack[aindexi][self.attackcount//2],(self.x,self.y))
                        self.attackcount +=1
                    else:
                        self.attack = False

                else:
                    if not self.standing:
                        if self.right:
                            win.blit(player1Right[self.walkCount // 3], (self.x, self.y))
                            self.walkCount += 1
                        else:
                            win.blit(player1Left[self.walkCount // 3], (self.x, self.y))
                            self.walkCount += 1
                    elif self.left:
                        win.blit(player1Standing[0], (self.x, self.y))
                    else:
                        win.blit(player1Standing[1], (self.x, self.y))
                    self.hitbox = (self.x + 25, self.y + 11, 60, 97)

            elif self.flyingcount<20:
                if self.left:
                    indexi =0
                else:
                    indexi = 1
                win.blit(p1flying[indexi][self.flyingcount//2],(self.x,self.y))
                self.flyingcount += 1

            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
            self.heroRect = pygame.Rect(self.hitbox)

    def hit(self):
        if self.live and self.health > 0:
            self.health -= 1//self.morehealth
            self.morehealth -= 1
            if self.morehealth == 0:
                self.morehealth = 6

        if self.health == 0:
            pygame.mixer.music.pause()
            if self.deadcount < 20:
                if self.left:
                    indexi=0
                else:
                    indexi =1
                win.blit(p1dead[indexi][self.deadcount//2],(self.x,self.y))
                self.deadcount += 1

            self.live = False


class bars(object):
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        self.hitbox = (self.x, self.y , 200, 80)
        self.Tiles = False
        self.BarJump = False
        self.jumpCount = -1
        self.LjumpCount = 10
        self.barRect = pygame.Rect(self.hitbox)
        self.BarLongJump = False
    def drawBar(self, win):
        win.blit(bar[self.type], (self.x, self.y))

        self.hitbox = (self.x, self.y , 200, 80)
        self.barRect = pygame.Rect(self.hitbox)


class enemy(object):
    def __init__(self, x, y, width, height, EwalkCount, Emar, Evisible, AttackCount,Type):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x + 120, self.y+180, 150, 180)
        self.visible = Evisible
        self.Ewalkcount = EwalkCount
        self.direction = 1
        self.vel = 3
        self.walk = True
        self.mar = Emar
        self.attCount = AttackCount
        self.health = 20
        self.healthBar = (self.x + self.width, self.y - 10, 90, 20)
        self.LeftandRight = 0
        self.enemyType = Type
    def drawEnemy(self, win):
        if self.visible :
            if pause.esc:
                if self.Ewalkcount < 30:
                    win.blit(Ewalk[self.enemyType][self.LeftandRight][self.Ewalkcount // 3], (self.x, self.y))
                else:
                    win.blit(Ewalk[self.enemyType][self.LeftandRight][(self.Ewalkcount-1) // 3], (self.x, self.y))
            else:
                if self.mar:
                    monster.play()
                    if self.attCount >= 30:
                        self.attCount = 0
                    win.blit(EAttack[self.enemyType][self.LeftandRight][self.attCount // 3], (self.x, self.y))
                    self.attCount += 1

                else:
                    if self.Ewalkcount >= 30:
                        self.Ewalkcount = 0
                    if self.x >= 20  and self.x <=win.get_width()-win.get_width()//10:
                        self.x -= self.vel*self.direction

                    win.blit(Ewalk[self.enemyType][self.LeftandRight][self.Ewalkcount // 3], (self.x, self.y))
                    self.Ewalkcount += 1
            self.hitbox = (self.x + 120, self.y +180, 130, 180)
            pygame.draw.rect(win, (255, 0, 0), (self.healthBar[0] + 100, self.healthBar[1] + 160, 190, 10), 2)
            pygame.draw.rect(win, (0, 220, 0), (self.healthBar[0] + 100, self.healthBar[1] + 160, 190 - 10 *(20 - self.health) , 10))
            self.healthBar = (self.x + self.width, self.y - 10, 90, 20)

    def hit(self, obj):
        global enemyrecord
        if self.visible:
            self.health -= 1
        if self.health == 0:
            Xcor = int(random.choice(list(range(self.x , self.x + self.hitbox[2]+30))))
            Ycor = int(random.choice(list(range(self.y-50 ,self.y+50))))
            Mtype = int(random.choice(list(range(0,len(motivation)-1))))
            motivelist.append(Motivation(Xcor,Ycor,Mtype))
            enemyrecord[LevelRecord] -= 1

            randgem = random.choice([0,0,0,0,0,0,2,1,1, 3, 4])

            gemslist.append(Gems(random.choice(range(self.x, self.x+self.hitbox[2])), random.choice(range(self.y, self.y+self.hitbox[3])), randgem))
            ammuBar.score += 1
            self.visible = False
            enem.pop(enem.index(obj))
            del obj


class Weapons(object):
    def __init__(self, width, height, x, y, quantity, facing):
        self.quantity = quantity
        self.attack = False
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.facing = facing
        self.vel = 5 * self.facing
        self.hitbox = (self.x + 3, self.y + 10, 90, 90)


    def Fire(self, win):
        # print("Fire")
        win.blit(weapon[ammuBar.weaponType], (self.x, self.y))
        self.hitbox = (self.x + 3, self.y + 10, 90, 90)



class Barrier(object):
    def __init__(self, width, height, x, y, type, visible):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.type = type
        self.power = 100 * (self.type + 1)
        self.visible = visible
        self.hitbox = (self.x + 32, self.y + 35, 75, 75)
        self.stoneCount = 0
        self.barrTiles = False
        self.BarrJump = False
        self.BarrjumpCount = -1
    def draw(self, win):
        if self.visible and len(barriers)>0:
            win.blit(barriers[self.type], (self.x, self.y))
            self.hitbox = (self.x + 32, self.y + 35, 75, 75)
            # pygame.draw.rect(win, (0, 233, 0), self.hitbox, 1)

    def BlockBlast(self, block):
        if self.visible:
            self.power -= 1
        if self.power == 0 :
            stonecloudlist.append(Barrier(200, 200, block.x, block.y , ammuBar.barrtype, True))
            self.visible = False
            barrier.pop(barrier.index(block))
            del block
    def stonecloud(self,cloud):
        if self.stoneCount<18:
            win.blit(stoneB[self.stoneCount//2],(self.x, self.y))
            self.stoneCount +=1
        else:
            stonecloudlist.pop(stonecloudlist.index(cloud))
            del cloud


class WeaponBar(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.smallhitbox = (self.x,self.y,100,100)
        self.largehitbox = (self.smallhitbox[0] + self.smallhitbox[2]//2 ,self.smallhitbox[3]//6, 400,50)
        self.mouseOver = False
        self.weaponType = 1
        self.button1Hit = (win.get_width()-162 , 55 , 30 , 40)
        self.button2Hit = (win.get_width() - 66, 55, 30, 40)
        self.button3Hit = (win.get_width() - 140, 130, 20, 20)
        self.button4Hit = (win.get_width() - 80, 130, 20, 20)
        self.weaponList = [100, 50, 40, 100, 50,20,40,30]
        self.score = 0
        self.barrtype = 0
    def draw(self,win):

        pygame.draw.rect(win, (3, 253, 219), (self.largehitbox[0]+55,self.largehitbox[1]+self.largehitbox[3]//2 +10, 160,30), 0)
        pygame.draw.rect(win, (253, 11, 3), (self.largehitbox[0]+55,self.largehitbox[1] + self.largehitbox[3]//2 + 10, 160 - 10 * (16 - char.health), 30),0)

        fontlevelLabel = pygame.font.SysFont('comiscans', 30)
        LevelNo = fontlevelLabel.render(" Level : " + str(LevelRecord + 1), 15, (255, 255, 255))
        win.blit(LevelNo, (10, 130))


        win.blit(weaponBar[1], (self.largehitbox[0], self.largehitbox[1]))
        win.blit(weaponBar[2], (self.x, self.y))
        win.blit(weaponBar[0], (win.get_width()-200,5))
        win.blit(weapontype[self.weaponType] , (win.get_width()-135 ,40))

        win.blit(weaponBar[6], (self.button1Hit[0],self.button1Hit[1]))

        win.blit(weaponBar[4], (self.button2Hit[0], self.button2Hit[1]))

        win.blit(weaponBar[3],(win.get_width()//2-50,10))
        fontgems = pygame.font.SysFont('comicsans',19)

        win.blit(gemsrecord[1],(win.get_width()//2-30,25))
        textG1 = fontgems.render(str(gemscorelist[1]),10,(255,255,255))
        win.blit(textG1,(win.get_width()//2-30+5,50))

        win.blit(gemsrecord[0], (win.get_width() // 2+5 , 25))
        textG2 = fontgems.render(str(gemscorelist[0]), 10, (255, 255, 255))
        win.blit(textG2, (win.get_width() // 2+10 , 50))

        win.blit(gemsrecord[2], (win.get_width() // 2 +40, 25))
        textG3 = fontgems.render(str(gemscorelist[2]), 10, (255, 255, 255))
        win.blit(textG3, (win.get_width() // 2 +45, 50))

        win.blit(gemsrecord[3], (win.get_width() // 2 +75, 25))
        textG4 = fontgems.render(str(gemscorelist[3]), 10, (255, 255, 255))
        win.blit(textG4, (win.get_width() // 2 +80, 50))

        win.blit(gemsrecord[4], (win.get_width() // 2 + 105, 25))
        textG5 = fontgems.render(str(gemscorelist[4]), 10, (255, 255, 255))
        win.blit(textG5, (win.get_width() // 2 + 110, 50))

        font1 = pygame.font.SysFont('comicsans', 20)
        text = font1.render(str(self.weaponList[self.weaponType]), 7, (255, 255, 255))
        win.blit(text, (win.get_width()-110 , 110))

        font3 = pygame.font.SysFont('comicsans', 25)
        text2 = font3.render("Score : " + str(ammuBar.score), 7 , (255,255,255))
        win.blit(text2,(win.get_width()//2+5, 70))


        win.blit(barrierbar[self.barrtype],(win.get_width()-122 , 120))

        win.blit(weaponBar[7], (self.button3Hit[0], self.button3Hit[1]))

        win.blit(weaponBar[5], (self.button4Hit[0], self.button4Hit[1]))


class AfterHit(object):
    def __init__(self,x,y,width,height,visible,type):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.firecount = 0
        self.visible = visible
        self.type = type
    def Booom(self,obj):
        if self.firecount<16 and self.visible:

            win.blit(fireblastlist[self.type][self.firecount//2] , (self.x,self.y))
            self.firecount +=1
        else:
            self.visible = False
            boom.pop(boom.index(obj))
            del obj


class Motivation(object):
    def __init__(self,x,y,type):
        self.x = x
        self.y = y
        self.type = type
        self.count = 0

    def print(self,obj):

        if self.count <20:
            win.blit(motivation[self.type],(self.x,self.y))
            self.count +=1
        else:
            motivelist.pop(motivelist.index(obj))
            del obj

class Gems(object):
    def __init__(self,x,y,type):
        self.x = x
        self.y = y
        self.type = type
        self.hitbox = (self.x+2,self.y+4,30,30)

    def keep(self,obj):
        win.blit(gems[self.type],(self.x,self.y))


class menu(object):
    def __init__(self):
        self.runcount = 0
        self.x = win.get_width()//2-win.get_width()//7
        self.y = win.get_height()//2 - win.get_height()//6
        self.newgameb = (win.get_width()//2-40,win.get_height()//2+80 , 110,30)
        self.controlsb = (win.get_width() // 2 - 40, win.get_height() // 2 + 160, 110, 30)
        self.AboutUs = (win.get_width() // 2 - 40, win.get_height() // 2 + 120, 110, 30)
        self.exitb = (win.get_width() // 2 - 40, win.get_height() // 2 + 200, 110, 30)
        self.buttonlist = [0,0,0,0]
        self.back = (win.get_width()//20,win.get_height()//20,30,20)
        self.trace = 2
    def draw(self):
        win.blit(menuimg[0],(20,50))
        if self.runcount < 20:
            win.blit(pmenu[self.runcount//2],(self.x,self.y + win.get_height()//14))
            win.blit(Emenu[self.runcount//2],(self.x+120,self.y-win.get_height()//7 ))
            self.runcount += 1
        else:
            self.runcount = 0
            win.blit(pmenu[self.runcount // 2], (self.x, self.y + win.get_height()//14))
            win.blit(Emenu[self.runcount // 2], (self.x + 120, self.y-win.get_height()//7))
        fontmenu = pygame.font.SysFont('comicsans', 25)
        NewText = fontmenu.render("  Play", 7, (0,0,0))
        PlayText = fontmenu.render("About Us",3,(0,0,0))
        ControlText = fontmenu.render(" Control",4,(0,0,0))
        ExitText = fontmenu.render("  Exit",3,(0,0,0))
        if self.buttonlist[0]:
            pygame.draw.rect(win,(133, 133, 173),self.newgameb,0)
        win.blit(NewText,(self.newgameb[0]+20,self.newgameb[1]+4))

        if self.buttonlist[2]:
            pygame.draw.rect(win, (133, 133, 173), self.controlsb, 0)
        win.blit(ControlText,(self.controlsb[0]+20,self.controlsb[1]+4))

        if self.buttonlist[1]:
            pygame.draw.rect(win,(133, 133, 173),self.AboutUs,0)
        win.blit(PlayText,(self.AboutUs[0]+20,self.AboutUs[1]+4))

        if self.buttonlist[3]:
            pygame.draw.rect(win, (133, 133, 173), self.exitb, 0)
        win.blit(ExitText,(self.exitb[0]+20,self.exitb[1]+4))

        if self.trace == 1:
            win.blit(Art4Menu[0],(0,0))

        if self.trace == 0:
            win.blit(Art4Menu[1],(0,0))

        if self.trace !=2:
            win.blit(Art4Menu[2],(win.get_width()//20,win.get_height()//20))


class gamepaused(object):
    def __init__(self):
        self.x = win.get_width()//2-win.get_width()//4
        self.y = win.get_height()//2-win.get_height()//4
        self.menubox = (self.x,self.y , win.get_width()//2,win.get_height()//2)

        self.esc = False
        self.buttons = (self.x +20,self.y+20,100,50)
        self.buttonN1 = (self.x + win.get_width()//6 + win.get_width()//60 - win.get_width()//50,self.y + win.get_height()//12+ win.get_height()//14 ,40,50)
        self.buttonN2 = (self.x+ win.get_width()//5 +win.get_width()//14 - win.get_width()//50 ,self.y+ win.get_height()//12 + win.get_height()//14 ,40,50)
        self.buttonN3 = (self.x + win.get_width() // 3 + win.get_width() // 65 - win.get_width()//50, self.y + win.get_height() //12  + win.get_height()//14, 40, 50)
        self.buttonN4 = (self.x + win.get_width() // 3 + win.get_width() // 12 - win.get_width()//50, self.y + win.get_height() //12  + win.get_height()//14, 40, 50)
        self.buyButton = (self.x + win.get_width()//6 +  win.get_width()//20 - win.get_width()//50, self.y + win.get_height()//4 + win.get_height()//50 + win.get_height()//14, 60,20)
        self.buyButton2 = (self.x + win.get_width() // 6 + win.get_width() // 20 +win.get_width()//7 + win.get_width()//90- win.get_width()//50 , self.y + win.get_height() // 4 + win.get_height() // 50+ win.get_height()//14 ,60, 20)
        self.buttonContinue =  (self.x + win.get_width()//100 , self.y + win.get_height()//15+ win.get_height()//14 , 200, 30)
        self.buttonNewi = (self.x + win.get_width()//100 , self.y + win.get_height()//10 + win.get_height()//40 + win.get_height()//14 + win.get_height()//29 , 200, 30)
        self.buttonExit = (self.x + win.get_width() // 100, self.y + win.get_height() // 10 + win.get_height()// 7+ win.get_height()//14 , 200, 30)

    def PausedMenu(self):
        global gemBalance
        if self.esc:

            pygame.draw.rect(win,(230,230,230),self.menubox,0)
            win.blit(smallMenuImagList[0],(self.x,self.y))
            pygame.draw.rect(win, smallMenuColor[0], self.buttonContinue, 0)
            pygame.draw.rect(win, smallMenuColor[1], self.buttonNewi, 0)
            pygame.draw.rect(win, smallMenuColor[3], self.buttonExit, 0)

            smallMenuFont = pygame.font.SysFont('comicsans', 40)
            ContinueText = smallMenuFont.render("Continue", 7, (0, 0, 0))
            NewText = smallMenuFont.render("New Game",7,(0,0,0))
            ExitText = smallMenuFont.render("Exit" , 7 , (0,0,0))

            win.blit(ContinueText , (self.buttonContinue[0] , self.buttonContinue[1]))
            win.blit(NewText, (self.buttonNewi[0], self.buttonNewi[1]))
            win.blit(ExitText, (self.buttonExit[0], self.buttonExit[1]))



            pygame.draw.rect(win,(255,255,255),(self.x + win.get_width()//6 - win.get_width()//50 ,self.y + win.get_height()//40 + win.get_height()//14 ,win.get_width()//3,win.get_height()//2 - win.get_height()//5 ),0)

            win.blit(smallMenuImagList[1], (self.x+ win.get_width()//5 - win.get_width()//50 ,self.y+ win.get_height()//21 + win.get_height()//14 ))


            win.blit(pauseMenu[2], (self.buttonN1[0], self.buttonN1[1] ))
            win.blit(pauseMenu[3], (self.buttonN2[0], self.buttonN2[1]) )

            pygame.draw.rect(win, (0, 0, 0), self.menubox, 8)
            pygame.draw.rect(win,(0,0,0),(self.x + win.get_width()//6 - win.get_width()//50 ,self.y + win.get_height()//40+ win.get_height()//14 ,win.get_width()//3,win.get_height()//2 - win.get_height()//5),5)
            WeaponName =  pygame.font.SysFont('comicsans', 25)
            WeaponText = WeaponName.render(weapomNameList[ammuBar.weaponType], 7, (0,0,0))
            win.blit(WeaponText,(self.x+ win.get_width()//5 - win.get_width()//50 ,self.y+ win.get_height()//21 + win.get_width()//13 + win.get_height()//14))


            QuantityFont = pygame.font.SysFont('Comicsans', 20)
            QuantityText1 = QuantityFont.render(str(gemsQuantity[ammuBar.weaponType][0])+"x",10,(0,0,0))
            QuantityText2 = QuantityFont.render(str(gemsQuantity[ammuBar.weaponType][1]) + "x",10 , (0, 0, 0))
            QuantityText3 = QuantityFont.render(str(gemsQuantity[ammuBar.weaponType][2]) + "x",10, (0, 0, 0))

            QuantityText4 = QuantityFont.render(str(gemsQuantity[ammuBar.barrtype][0]) + "x", 10, (0, 0, 0))
            QuantityText5 = QuantityFont.render(str(gemsQuantity[ammuBar.barrtype][1]) + "x", 10, (0, 0, 0))
            QuantityText6 = QuantityFont.render(str(gemsQuantity[ammuBar.barrtype][2]) + "x", 10, (0, 0, 0))


            win.blit(gemsWalllet[ammuBar.weaponType][0], (self.x + win.get_width()//6 + win.get_width()//40 - win.get_width()//50 , self.y + win.get_height()//5 + win.get_height()//50 + win.get_height()//14))
            win.blit(gemsWalllet[ammuBar.weaponType][1], (self.x + win.get_width()//5 +   win.get_width()//40 - win.get_width()//50, self.y + win.get_height()//5 + win.get_height()//50 + win.get_height()//14))
            win.blit(gemsWalllet[ammuBar.weaponType][2], (self.x + win.get_width()//4  + win.get_width()//72 - win.get_width()//50, self.y + win.get_height()//5 + win.get_height()//50 + win.get_height()//14 ))

            win.blit(QuantityText1, (self.x + win.get_width()//6 + win.get_width()//35- win.get_width()//50 , self.y + win.get_height()//5 + win.get_height()//40 + win.get_height()//14))
            win.blit(QuantityText2, (self.x + win.get_width()//5 + win.get_width()//35 - win.get_width()//50, self.y +  win.get_height()//5 + win.get_height()//40 + win.get_height()//14))
            win.blit(QuantityText3, (self.x + win.get_width()//4 + win.get_width()//67 - win.get_width()//50, self.y + win.get_height()//5 + win.get_height()//40 + win.get_height()//14))
            pygame.draw.rect(win,(23,232,232),self.buyButton,0)
            win.blit(pauseMenu[4],(self.buyButton[0],self.buyButton[1]))
            win.blit(pauseMenu[2], (self.buttonN3[0], self.buttonN3[1]))
            win.blit(pauseMenu[3], (self.buttonN4[0], self.buttonN4[1]))
            weapon2Text = WeaponName.render(weapon2list[ammuBar.barrtype],7,(0,0,0))
            win.blit(smallMenuImagList[2] , (self.x+ win.get_width()//3 + win.get_width()//45 - win.get_width()//50,self.y+ win.get_height()//21 + win.get_height()//14))
            win.blit(weapon2Text,(self.buttonN3[0]+win.get_width()//140 , self.y+ win.get_height()//21 + win.get_width()//13 + win.get_height()//14))
            win.blit(gemsWalllet[ammuBar.barrtype][0], (self.x + win.get_width() // 6 + win.get_width() // 40 +win.get_width()//7 + win.get_width()//90 - win.get_width()//50,
                                                          self.y + win.get_height() // 5 + win.get_height() // 50+ win.get_height()//14))
            win.blit(gemsWalllet[ammuBar.barrtype][1], (self.x + win.get_width() // 5 + win.get_width() // 40 +win.get_width()//7 + win.get_width()//90- win.get_width()//50,
                                                          self.y + win.get_height() // 5 + win.get_height() // 50+ win.get_height()//14))
            win.blit(gemsWalllet[ammuBar.barrtype][2], (self.x + win.get_width() // 4 + win.get_width() // 72 +win.get_width()//7 + win.get_width()//90- win.get_width()//50,
                                                          self.y + win.get_height() // 5 + win.get_height() // 50+ win.get_height()//14))

            win.blit(QuantityText4, (self.x + win.get_width() // 6 + win.get_width() // 35 +win.get_width()//7 + win.get_width()//90- win.get_width()//50,
                                     self.y + win.get_height() // 5 + win.get_height() // 40+ win.get_height()//14))
            win.blit(QuantityText5, (self.x + win.get_width() // 5 + win.get_width() // 35 +win.get_width()//7 + win.get_width()//90- win.get_width()//50,
                                     self.y + win.get_height() // 5 + win.get_height() // 40+ win.get_height()//14))
            win.blit(QuantityText6, (self.x + win.get_width() // 4 + win.get_width() // 67 +win.get_width()//7 + win.get_width()//90- win.get_width()//50,
                                     self.y + win.get_height() // 5 + win.get_height() // 40 + win.get_height()//14))
            win.blit(pauseMenu[4], (self.buyButton2[0], self.buyButton2[1]))


def refreshWin():

    if starter:
        global EnemyTypeList
        if LevelRecord < 3:
            EnemyTypeList = list(range(0, LevelRecord + 1))

        if pygame.time.get_ticks() % 200 == 0 and enemyrecord2[LevelRecord] > 0:
            randomEnemyType = random.choice(EnemyTypeList)
            enem.append(enemy(int(win.get_width() - win.get_width()/9), win_height - 465, 0, 40, 0, False, True, 0,randomEnemyType))
            enemyrecord2[LevelRecord] -= 1

        win.blit(bg[bgtrack], (0, 0))
        win.blit(grass[bgtrack],(0,win.get_height()-80))
        char.draw(win)
        for bari in barList[LevelRecord]:
            bari.drawBar(win)
        for motive in motivelist:
            motive.print(motive)

        for enemies in enem:
            enemies.drawEnemy(win)

        for bullet in bullets:
            bullet.Fire(win)
        for Barr in barrier:
            Barr.draw(win)
        for bombi in boom:
            bombi.Booom(bombi)
        for cloud in stonecloudlist:
            cloud.stonecloud(cloud)
        for gemi in gemslist:
            gemi.keep(gemi)
        if not char.live and char.deadcount<20:
            char.hit()
        ammuBar.draw(win)

        fontLabel = pygame.font.SysFont('comiscans', 150)
        fontLabel2 = pygame.font.SysFont('comiscans', 50)
        if enemyrecord[LevelRecord] <= 0 and LevelRecord<3:
            Leveltrack = fontLabel.render(" Go ", 15, (255, 255, 255))
            win.blit(Leveltrack, (win.get_width() // 2, win.get_height() // 3))

        if char.health == 0:
            win.blit(fontLabel.render("GAME OVER",14,(255,255,255)),(win.get_width()//4,win.get_height()//3))
            win.blit(fontLabel2.render("Press Esc for New Game",13,(255,255,255)),(win.get_width()//3,win.get_height()//3 +win.get_height()//8))

        if LevelRecord == 3 and enemyrecord[LevelRecord] <= 0:
            win.blit(fontLabel.render(" VICTORY ", 14, (255, 255, 255)), (win.get_width() // 3, win.get_height() // 3))

        pause.PausedMenu()
        win.blit(grass[bgtrack], ((0, 0)))
    else:
         win.fill([255,255,255])
         menurun.draw()


    pygame.display.update()


win_width = win.get_width()
win_height = win.get_height()

enemyrecord = [2,2,2,2]
enemyrecord2 = [2,2,2,2]
LevelRecord = 0
char = hero(200, win_height-190, 0, 40)
barList = [[bars(win.get_width()//8, win.get_height()//3, 0),bars(win.get_width()//2, win.get_height()//2, 1),bars(win.get_width()//2 + win.get_width()//10 , win.get_height()//5,1) ]
                               ,[bars(win.get_width()//2, win.get_height()//3, 2),bars(win.get_width()//3, win.get_height()//2, 1),bars(win.get_width()-win.get_width()//5 , win.get_height()//2,2)]
                               ,[bars(win.get_width()//2, win.get_height()//2, 3),bars(win.get_width()-win.get_width()//5, win.get_height()//3, 2),bars(win.get_width()//3 , win.get_height()//3,3)]
                               ,[bars(win.get_width()//8, win.get_height()//3, 5),bars(win.get_width()//2, win.get_height()//2, 5),bars(win.get_width()//2 + win.get_width()//10 , win.get_height()//5,3) ]
                               ]
enem = []
barrier = []
bullets = []
ammuBar = WeaponBar()

smallMenuImagList = [pygame.transform.scale((pygame.image.load("mbg.jpg").convert_alpha()),(win_width//2,win_height//2)) ,
                     pygame.transform.scale((pygame.image.load("weapon/w{0}.png".format(ammuBar.weaponType)).convert_alpha()), (win.get_width()//15, win.get_width()//15))
                     , pygame.transform.scale((pygame.image.load("barrier/b{0}.png".format(ammuBar.barrtype + 1)).convert_alpha()), (win.get_width()//15, win.get_width()//15))]
EnemyTypeList = []
motivelist = []
boom = []
run = True
facing = 1
firelimit = 0
gemscorelist = [0,0,0,0,0]
menurun = menu()
gemslist = [Gems(random.choice(range(win.get_width()//5,win.get_width()-win.get_width()//10)), random.choice(range(win.get_height()//5,win.get_height()-win.get_height()//8)),random.choice([0,1,1,1,1,2,3,4]))
            ,Gems(random.choice(range(win.get_width()//5,win.get_width()-win.get_width()//10)), random.choice(range(win.get_height()//5,win.get_height()-win.get_height()//10)),random.choice([0,1,1,1,1,2,3,4]))
            ,Gems(random.choice(range(win.get_width()//5,win.get_width()-win.get_width()//10)), random.choice(range(win.get_height()//5,win.get_height()-win.get_height()//10)), random.choice([0,1,1,1,1,2,3,4]))
            ,Gems(random.choice(range(win.get_width()//5,win.get_width()-win.get_width()//10)), random.choice(range(win.get_height()//5,win.get_height()-win.get_height()//10)), random.choice([0,1,1,1,1,2,3,4]))
            ,Gems(random.choice(range(win.get_width()//5,win.get_width()-win.get_width()//10)), random.choice(range(win.get_height()//5,win.get_height()-win.get_height()//10)),random.choice([0,1,1,1,1,2,3,4]))
             ,Gems(random.choice(range(win.get_width()//5,win.get_width()-win.get_width()//10)), random.choice(range(win.get_height()//5,win.get_height()-win.get_height()//10)),random.choice([0,1,1,1,1,2,3,4]))
            ,Gems(random.choice(range(win.get_width()//5,win.get_width()-win.get_width()//10)), random.choice(range(win.get_height()//5,win.get_height()-win.get_height()//10)),random.choice([0,1,1,1,1,2,3,4])),\
             Gems(random.choice(range(win.get_width()//5,win.get_width()-win.get_width()//10)), random.choice(range(win.get_height()//5,win.get_height()-win.get_height()//10)),random.choice([0,1,1,1,1,2,3,4]))
            ]

gemBalance = [0,0,0]

pause = gamepaused()
gameover = 1
while run:
    clock.tick(28)
    randInt = 1
    # print(barrCount[ammuBar.barrtype])
    if char.health == 0 and gameover:
        deadsong.play(loops=0)
        gameover = 0

    for eny in enem:
        if eny.x + eny.hitbox[2] < char.x :
            eny.direction = -1
            eny.LeftandRight = 1
        else:
            eny.direction = 1
            eny.LeftandRight = 0

        if char.hitbox[1] + char.hitbox[3] > eny.hitbox[1] and char.hitbox[1] < eny.hitbox[1] + eny.hitbox[3]:
            if char.hitbox[0] + char.hitbox[2] > eny.hitbox[0] and char.hitbox[0] < eny.hitbox[0] + eny.hitbox[2]:
                char.hit()
                eny.mar = True
        else:
            eny.mar = False

    for Enemys  in enem:
        for BlockIndex in barrier:
            if BlockIndex.hitbox[1] + BlockIndex.hitbox[3] > Enemys.hitbox[1] and BlockIndex.hitbox[1] < \
                    Enemys.hitbox[1] + Enemys.hitbox[3]:
                if BlockIndex.hitbox[0] + BlockIndex.hitbox[2] > Enemys.hitbox[0] and BlockIndex.hitbox[0] < \
                        Enemys.hitbox[0] + Enemys.hitbox[2]:
                    Enemys.mar = True
                    BlockIndex.BlockBlast(BlockIndex)
            else:
                Enemys.mar = False


    for gemis in gemslist:
        if char.hitbox[1] + char.hitbox[3] > gemis.hitbox[1] and char.hitbox[1] < gemis.hitbox[1] + gemis.hitbox[3]:
            if char.hitbox[0] + char.hitbox[2] > gemis.hitbox[0] and char.hitbox[0] < gemis.hitbox[0] + gemis.hitbox[2]:
                gemslist.pop(gemslist.index(gemis))
                gemscorelist[gemis.type] += 1
                del gemis
    if firelimit > 0:
        firelimit += 1
    if firelimit > 5:
        firelimit = 0

    for Enemys in enem:
        for bullet in bullets:
            if bullet.hitbox[1] + bullet.hitbox[3] > Enemys.hitbox[1] and bullet.hitbox[1] < Enemys.hitbox[1] + \
                    Enemys.hitbox[3]:
                if bullet.hitbox[0] + bullet.hitbox[2] > Enemys.hitbox[0] and bullet.hitbox[0] < Enemys.hitbox[0] + \
                        Enemys.hitbox[2]:
                    hitSound.play()
                    Enemys.hit(Enemys)
                    if ammuBar.weaponType in [0,1,2,3]:
                        randInt = 0
                    else:
                        randInt = random.choice([1,2])
                    boom.append(AfterHit(Enemys.x+Enemys.hitbox[2]//2, Enemys.y+200,150,150,True,randInt))
                    bullets.pop(bullets.index(bullet))



    for bulletis in bullets:
        if bulletis.x > 0 and bulletis.x < win_width:
            bulletis.x += bulletis.vel
        else:
            bullets.pop(bullets.index(bulletis))

        bulletis.x += bulletis.vel

    keys = pygame.key.get_pressed()



    for event in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        if pause.buttonContinue[0] <= mouse[0] <= pause.buttonContinue[0] + pause.buttonContinue[2] and \
                pause.buttonContinue[1] <= mouse[1] <= pause.buttonContinue[1] + pause.buttonContinue[3]:
            smallMenuColor[0] = (133, 133, 173)
        else:
            smallMenuColor[0] = (255,255,255)
        if pause.buttonNewi[0] <= mouse[0] <= pause.buttonNewi[0] + pause.buttonNewi[2] and \
                pause.buttonNewi[1] <= mouse[1] <= pause.buttonNewi[1] + pause.buttonNewi[3]:
            smallMenuColor[1] = (133, 133, 173)
        else:
            smallMenuColor[1] = (255,255,255)
        if pause.buttonExit[0] <= mouse[0] <= pause.buttonExit[0] + pause.buttonExit[2] and \
                pause.buttonExit[1] <= mouse[1] <= pause.buttonExit[1] + pause.buttonExit[3]:
            smallMenuColor[3] = (133, 133, 173)
        else:
            smallMenuColor[3] = (255,255,255)




        if starter == 0:
            if menurun.newgameb[0] <= mouse[0] <= menurun.newgameb[0] + menurun.newgameb[2] and \
                    menurun.newgameb[1] <= mouse[1] <= menurun.newgameb[1] + menurun.newgameb[3]:
                menurun.buttonlist[0]=1
            else:
                menurun.buttonlist[0]=0

            if menurun.AboutUs[0] <= mouse[0] <= menurun.AboutUs[0] + menurun.AboutUs[2] and \
                    menurun.AboutUs[1] <= mouse[1] <= menurun.AboutUs[1] + menurun.AboutUs[3]:
                menurun.buttonlist[1]=1
            else:
                menurun.buttonlist[1]=0

            if menurun.controlsb[0] <= mouse[0] <= menurun.controlsb[0] + menurun.controlsb[2] and \
                    menurun.controlsb[1] <= mouse[1] <= menurun.controlsb[1] + menurun.controlsb[3]:
                menurun.buttonlist[2]=1
            else:
                menurun.buttonlist[2]=0

            if menurun.exitb[0] <= mouse[0] <= menurun.exitb[0] + menurun.exitb[2] and \
                    menurun.exitb[1] <= mouse[1] <= menurun.exitb[1] + menurun.exitb[3]:
                menurun.buttonlist[3]=1
            else:
                menurun.buttonlist[3]=0

        if event.type == MOUSEBUTTONDOWN:
            if pause.esc:
                if pause.buttonN1[0] <= mouse[0] <= pause.buttonN1[0] + pause.buttonN1[2] and \
                        pause.buttonN1[1] <= mouse[1] <= pause.buttonN1[1] + pause.buttonN1[3]:
                    if ammuBar.weaponType == 0:
                        ammuBar.weaponType = len(weapontype) - 1
                    else:
                        ammuBar.weaponType -= 1
                if pause.buttonN2[0] <= mouse[0] <= pause.buttonN2[0] + pause.buttonN2[2] and \
                        pause.buttonN2[1] <= mouse[1] <= pause.buttonN2[1] + pause.buttonN2[3]:
                    if ammuBar.weaponType == len(weapontype) - 1:
                        ammuBar.weaponType = 0
                    else:
                        ammuBar.weaponType += 1

                if pause.buyButton[0] <= mouse[0] <= pause.buyButton[0] + pause.buyButton[2] and \
                        pause.buyButton[1] <= mouse[1] <= pause.buyButton[1] + pause.buyButton[3]:
                        if gemscorelist[gemsBalanceIndex[ammuBar.weaponType][0]] >= gemsQuantity[ammuBar.weaponType][0] and gemscorelist[gemsBalanceIndex[ammuBar.weaponType][1]] >= gemsQuantity[ammuBar.weaponType][1] and \
                        gemscorelist[gemsBalanceIndex[ammuBar.weaponType][2]] >= gemsQuantity[ammuBar.weaponType][2]:
                            gemscorelist[gemsBalanceIndex[ammuBar.weaponType][0]] -= gemsQuantity[ammuBar.weaponType][0]
                            gemscorelist[gemsBalanceIndex[ammuBar.weaponType][1]] -= gemsQuantity[ammuBar.weaponType][1]
                            gemscorelist[gemsBalanceIndex[ammuBar.weaponType][2]] -= gemsQuantity[ammuBar.weaponType][2]
                            ammuBar.weaponList[ammuBar.weaponType] += 20


                if pause.buttonN3[0] <= mouse[0] <= pause.buttonN3[0] + pause.buttonN3[2] and \
                        pause.buttonN3[1] <= mouse[1] <= pause.buttonN3[1] + pause.buttonN3[3]:
                    if ammuBar.barrtype == 0:
                        ammuBar.barrtype = len(barrierbar) - 1
                    else:
                        ammuBar.barrtype -= 1
                if pause.buttonN4[0] <= mouse[0] <= pause.buttonN4[0] + pause.buttonN4[2] and \
                        pause.buttonN4[1] <= mouse[1] <= pause.buttonN4[1] + pause.buttonN4[3]:
                    if ammuBar.barrtype == len(barrierbar) - 1:
                        ammuBar.barrtype = 0
                    else:
                        ammuBar.barrtype += 1

                smallMenuImagList[0] = pygame.transform.scale((pygame.image.load("mbg.jpg").convert_alpha()),
                                                              (win_width // 2, win_height // 2))

                smallMenuImagList[1] = pygame.transform.scale(
                    (pygame.image.load("weapon/w{0}.png".format(ammuBar.weaponType)).convert_alpha()),
                    (win.get_width() // 15, win.get_width() // 15))
                smallMenuImagList[2] = pygame.transform.scale(
                    (pygame.image.load("barrier/b{0}.png".format(ammuBar.barrtype + 1)).convert_alpha()),
                    (win.get_width() // 15, win.get_width() // 15))

            if pause.buyButton2[0] <= mouse[0] <= pause.buyButton2[0] + pause.buyButton2[2] and \
                        pause.buyButton2[1] <= mouse[1] <= pause.buyButton2[1] + pause.buyButton2[3]:
                    if gemscorelist[gemsBalanceIndex[ammuBar.weaponType][0]] >= gemsQuantity[ammuBar.weaponType][0] and \
                            gemscorelist[gemsBalanceIndex[ammuBar.weaponType][1]] >= gemsQuantity[ammuBar.weaponType][1] and gemscorelist[gemsBalanceIndex[ammuBar.weaponType][2]] >= gemsQuantity[ammuBar.weaponType][2]:
                        gemscorelist[gemsBalanceIndex[ammuBar.weaponType][0]] -= gemsQuantity[ammuBar.weaponType][0]
                        gemscorelist[gemsBalanceIndex[ammuBar.weaponType][1]] -= gemsQuantity[ammuBar.weaponType][1]
                        gemscorelist[gemsBalanceIndex[ammuBar.weaponType][2]] -= gemsQuantity[ammuBar.weaponType][2]
                        barrCount[ammuBar.barrtype] += 20


            if pause.buttonContinue[0] <= mouse[0] <= pause.buttonContinue[0] + pause.buttonContinue[2] and \
                    pause.buttonContinue[1] <= mouse[1] <= pause.buttonContinue[1] + pause.buttonContinue[3]:
                pause.esc = False

            if pause.buttonNewi[0] <= mouse[0] <= pause.buttonNewi[0] + pause.buttonNewi[2] and \
                    pause.buttonNewi[1] <= mouse[1] <= pause.buttonNewi[1] + pause.buttonNewi[3]:
                pause.esc = False

                win = pygame.display.set_mode((screen_width - 20, screen_height - 50),pygame.FULLSCREEN)
                win_width = win.get_width()
                win_height = win.get_height()

                char = hero(200, win_height - 190, 0, 40)
                pygame.mixer.music.unpause()
                enem = []
                barrCount = [10, 10, 5]
                barrier = []
                bullets = []
                EnemyTypeList = [0]
                ammuBar = WeaponBar()
                pause = gamepaused()
                gameover = 1
                barList = [[bars(win.get_width() // 8, win.get_height() // 3, 0),
                            bars(win.get_width() // 2, win.get_height() // 2, 1),
                            bars(win.get_width() // 2 + win.get_width() // 10, win.get_height() // 5, 1)]
                    , [bars(win.get_width() // 2, win.get_height() // 3, 2),
                       bars(win.get_width() // 3, win.get_height() // 2, 1),
                       bars(win.get_width() - win.get_width() // 5, win.get_height() // 2, 2)]
                    , [bars(win.get_width() // 2, win.get_height() // 2, 3),
                       bars(win.get_width() - win.get_width() // 5, win.get_height() // 3, 2),
                       bars(win.get_width() // 3, win.get_height() // 3, 3)]
                    , [bars(win.get_width() // 8, win.get_height() // 3, 5),
                       bars(win.get_width() // 2, win.get_height() // 2, 5),
                       bars(win.get_width() // 2 + win.get_width() // 10, win.get_height() // 5, 3)]
                           ]
                gemslist = [Gems(random.choice(range(win.get_width() // 5, win.get_width() - win.get_width() // 10)),
                                 random.choice(range(win.get_height() // 5, win.get_height() - win.get_height() // 15)),
                                 random.choice([0, 1, 1, 1, 1, 2, 3, 4]))
                    , Gems(random.choice(range(win.get_width() // 5, win.get_width() - win.get_width() // 10)),
                           random.choice(range(win.get_height() // 5, win.get_height() - win.get_height() // 15)),
                           random.choice([0, 1, 1, 1, 1, 2, 3, 4]))
                    , Gems(random.choice(range(win.get_width() // 5, win.get_width() - win.get_width() // 10)),
                           random.choice(range(win.get_height() // 5, win.get_height() - win.get_height() // 15)),
                           random.choice([0, 1, 1, 1, 1, 2, 3, 4])),
                            Gems(random.choice(range(100, 700)), random.choice(range(100, 500)),
                                 random.choice([0, 1, 1, 1, 1, 2, 3, 4]))
                    , Gems(random.choice(range(win.get_width() // 5, win.get_width() - win.get_width() // 10)),
                           random.choice(range(win.get_height() // 5, win.get_height() - win.get_height() // 15)),
                           random.choice([0, 1, 1, 1, 1, 2, 3, 4])),
                            Gems(random.choice(range(100, 700)), random.choice(range(100, 500)),
                                 random.choice([0, 1, 1, 1, 1, 2, 3, 4]))
                    , Gems(random.choice(range(win.get_width() // 5, win.get_width() - win.get_width() // 10)),
                           random.choice(range(win.get_height() // 5, win.get_height() - win.get_height() // 15)),
                           random.choice([0, 1, 1, 1, 1, 2, 3, 4])),
                            Gems(random.choice(range(700, 800)), random.choice(range(100, 500)),
                                 random.choice([0, 1, 1, 1, 1, 2, 3, 4]))
                            ]
                motivelist = []
                boom = []
                run = True
                facing = 1
                firelimit = 0
                gemscorelist = [0, 0, 0, 0, 0]
                enemyrecord = [2,2,2,2]
                enemyrecord2 = [2, 2, 2, 2]
                LevelRecord = 0
                bgtrack = 0
                gameover = 1
                smallMenuImagList[0] = pygame.transform.scale((pygame.image.load("mbg.jpg").convert_alpha()),
                                                              (win_width // 2, win_height // 2))

                smallMenuImagList[1] = pygame.transform.scale(
                    (pygame.image.load("weapon/w{0}.png".format(ammuBar.weaponType)).convert_alpha()),
                    (win.get_width() // 15, win.get_width() // 15))
                smallMenuImagList[2] = pygame.transform.scale(
                    (pygame.image.load("barrier/b{0}.png".format(ammuBar.barrtype + 1)).convert_alpha()),
                    (win.get_width() // 15, win.get_width() // 15))

            if pause.buttonExit[0] <= mouse[0] <= pause.buttonExit[0] + pause.buttonExit[2] and \
                    pause.buttonExit[1] <= mouse[1] <= pause.buttonExit[1] + pause.buttonExit[3]:
                win = pygame.display.set_mode((screen_width - screen_width // 2, screen_height - screen_height // 4),
                                              RESIZABLE)
                starter = 0


            if starter == 0 :
                if menurun.newgameb[0] <= mouse[0] <= menurun.newgameb[0] + menurun.newgameb[2] and \
                        menurun.newgameb[1] <= mouse[1] <= menurun.newgameb[1] + menurun.newgameb[3]:
                    starter = 1
                    win = pygame.display.set_mode((screen_width - 20, screen_height - 50),pygame.FULLSCREEN)
                    win_width = win.get_width()
                    win_height = win.get_height()
                    pygame.mixer.music.unpause()
                    enemyrecord = [2,2,2,2]
                    enemyrecord2 = [2, 2, 2, 2]
                    gameover = 1
                    gemslist = [
                        Gems(random.choice(range(win.get_width() // 5, win.get_width() - win.get_width() // 10)),
                             random.choice(range(win.get_height() // 5, win.get_height() - win.get_height() // 15)),
                             random.choice([0, 1, 1, 1, 1, 2, 3, 4]))
                        , Gems(random.choice(range(win.get_width() // 5, win.get_width() - win.get_width() // 10)),
                               random.choice(range(win.get_height() // 5, win.get_height() - win.get_height() // 15)),
                               random.choice([0, 1, 1, 1, 1, 2, 3, 4]))
                        , Gems(random.choice(range(win.get_width() // 5, win.get_width() - win.get_width() // 10)),
                               random.choice(range(win.get_height() // 5, win.get_height() - win.get_height() // 15)),
                               random.choice([0, 1, 1, 1, 1, 2, 3, 4])),
                        Gems(random.choice(range(100, 700)), random.choice(range(100, 500)),
                             random.choice([0, 1, 1, 1, 1, 2, 3, 4]))
                        , Gems(random.choice(range(win.get_width() // 5, win.get_width() - win.get_width() // 10)),
                               random.choice(range(win.get_height() // 5, win.get_height() - win.get_height() // 15)),
                               random.choice([0, 1, 1, 1, 1, 2, 3, 4])),
                        Gems(random.choice(range(100, 700)), random.choice(range(100, 500)),
                             random.choice([0, 1, 1, 1, 1, 2, 3, 4]))
                        , Gems(random.choice(range(win.get_width() // 5, win.get_width() - win.get_width() // 10)),
                               random.choice(range(win.get_height() // 5, win.get_height() - win.get_height() // 15)),
                               random.choice([0, 1, 1, 1, 1, 2, 3, 4])),
                        Gems(random.choice(range(700, 800)), random.choice(range(100, 500)),
                             random.choice([0, 1, 1, 1, 1, 2, 3, 4]))
                        ]
                    char = hero(200, win_height - 190, 0, 40)
                    barList = [[bars(win.get_width()//8, win.get_height()//3, 0),bars(win.get_width()//2, win.get_height()//2, 1),bars(win.get_width()//2 + win.get_width()//10 , win.get_height()//5,1) ]
                               ,[bars(win.get_width()//2, win.get_height()//3, 2),bars(win.get_width()//3, win.get_height()//2, 1),bars(win.get_width()-win.get_width()//5 , win.get_height()//2,2)]
                               ,[bars(win.get_width()//2, win.get_height()//2, 3),bars(win.get_width()-win.get_width()//5, win.get_height()//3, 2),bars(win.get_width()//3 , win.get_height()//3,3)]
                               ,[bars(win.get_width()//8, win.get_height()//3, 5),bars(win.get_width()//2, win.get_height()//2, 5),bars(win.get_width()//2 + win.get_width()//10 , win.get_height()//5,3) ]
                               ]
                    barrCount = [10, 10, 5]
                    enem = []
                    barrier = []
                    bullets = []
                    bgtrack = 0
                    ammuBar = WeaponBar()
                    pause = gamepaused()
                    smallMenuImagList[0] = pygame.transform.scale((pygame.image.load("mbg.jpg").convert_alpha()), (win_width // 2, win_height // 2))

                    smallMenuImagList[1] = pygame.transform.scale((pygame.image.load("weapon/w{0}.png".format(ammuBar.weaponType)).convert_alpha()),(win.get_width() // 15, win.get_width() // 15))
                    smallMenuImagList[2] = pygame.transform.scale((pygame.image.load("barrier/b{0}.png".format(ammuBar.barrtype + 1)).convert_alpha()),(win.get_width() // 15, win.get_width() // 15))

                    motivelist = []
                    boom = []
                    run = True
                    facing = 1
                    firelimit = 0
                    gemscorelist = [0, 0, 0, 0, 0]

                    EnemyTypeList = [0]

                if menurun.exitb[0] <= mouse[0] <= menurun.exitb[0] + menurun.exitb[2] and  menurun.exitb[1] <= mouse[1] <= menurun.exitb[1] + menurun.exitb[3]:
                    run = False
                    pygame.quit()


                if menurun.controlsb[0] <= mouse[0] <= menurun.controlsb[0] + menurun.controlsb[2] and \
                        menurun.controlsb[1] <= mouse[1] <= menurun.controlsb[1] + menurun.controlsb[3]:
                        menurun.trace = 1
                if menurun.AboutUs[0] <= mouse[0] <= menurun.AboutUs[0] + menurun.AboutUs[2] and \
                        menurun.AboutUs[1] <= mouse[1] <= menurun.AboutUs[1] + menurun.AboutUs[3]:
                        menurun.trace = 0

                if menurun.trace !=2 and menurun.back[0] <= mouse[0] <= menurun.back[0] + menurun.back[2] and \
                        menurun.back[1] <= mouse[1] <= menurun.back[1] + menurun.back[3]:
                        menurun.trace = 2


            if ammuBar.button1Hit[0] <= mouse[0] <= ammuBar.button1Hit[0] + ammuBar.button1Hit[2] and \
                    ammuBar.button1Hit[1] <= mouse[1] <= ammuBar.button1Hit[1] + ammuBar.button1Hit[3]:
                 if ammuBar.weaponType == 0:
                     ammuBar.weaponType = len(weapontype)-1
                 else:
                     ammuBar.weaponType -=1

            if ammuBar.button2Hit[0] <= mouse[0] <= ammuBar.button2Hit[0] + ammuBar.button2Hit[2] and \
                    ammuBar.button2Hit[1] <= mouse[1] <= ammuBar.button2Hit[1] + ammuBar.button2Hit[3]:
                if ammuBar.weaponType == len(weapontype)-1:
                    ammuBar.weaponType = 0
                else:
                    ammuBar.weaponType += 1

            if ammuBar.button3Hit[0] <= mouse[0] <= ammuBar.button3Hit[0] + ammuBar.button3Hit[2] and \
                    ammuBar.button3Hit[1] <= mouse[1] <= ammuBar.button3Hit[1] + ammuBar.button3Hit[3]:
                if ammuBar.barrtype == 0:
                    ammuBar.barrtype = len(barrierbar) - 1
                else:
                    ammuBar.barrtype -= 1

            if ammuBar.button4Hit[0] <= mouse[0] <= ammuBar.button4Hit[0] + ammuBar.button4Hit[2] and \
                    ammuBar.button4Hit[1] <= mouse[1] <= ammuBar.button4Hit[1] + ammuBar.button4Hit[3]:
                if ammuBar.barrtype == len(barrierbar) - 1:
                    ammuBar.barrtype = 0
                else:
                    ammuBar.barrtype += 1

        if event.type == pygame.KEYDOWN:
            if not pause.esc:
                  if event.key == pygame.K_SPACE and firelimit == 0 and char.live:
                    bulletSound.play()
                    char.attack =True
                    char.attackcount = 0
                    if char.left:
                        facing = -1
                    if char.right:
                        facing = 1
                    if len(bullets) <=7  and ammuBar.weaponList[ammuBar.weaponType] > 0:
                        ammuBar.weaponList[ammuBar.weaponType] -= 1
                        bullets.append(Weapons(80, 80, char.x + char.width // 2, char.y + char.height // 2, 1, facing))

                  if event.key == pygame.K_b and barrCount[ammuBar.barrtype] > 0 and  char.live :
                      ManageBlock = 1
                      for Block in barrier:
                          if char.hitbox[1] + char.hitbox[3] > Block.hitbox[1] and char.hitbox[1] < Block.hitbox[1] + \
                                  Block.hitbox[3]:
                              if char.hitbox[0] + char.hitbox[2] > Block.hitbox[0] and char.hitbox[0] < Block.hitbox[0] + \
                                      Block.hitbox[2]:
                                  barrier.append(Barrier(200, 200, char.x, Block.y - 80, ammuBar.barrtype, True))
                                  ManageBlock = 0
                                  break
                      if ManageBlock:
                          barrier.append(Barrier(300, 300, char.x, char.y + char.height // 10, ammuBar.barrtype, True))
                      barrCount[ammuBar.barrtype] -= 1

            if event.key == pygame.K_ESCAPE:
                if escTrack > 0:
                    pause.esc = True
                else:
                    pause.esc = False
                escTrack *= -1


        if event.type == pygame.QUIT:
            pygame.quit()
            run = False



    if not pause.esc:
        if keys[pygame.K_LEFT] and char.x > 0 and char.live:
            char.x -= char.vel
            char.left = True
            char.right = False
            char.standing = False
        elif keys[pygame.K_RIGHT] and (enemyrecord[LevelRecord] <= 0 or char.x < win_width-100 ) and  char.live:
            char.x += char.vel
            char.right = True
            char.left = False
            char.standing = False
        else:
            char.standing = True

        if not char.isJump:
            if keys[pygame.K_UP] and  char.live:
                char.isJump = True
                char.walkCount = 0
        else:
                if char.jumpCount >= 0:
                    char.y -= (char.jumpCount ** 2)
                    char.jumpCount -= 1
                    char.hitbox = (char.x + 25, char.y + 11, 60, 97)
                else:
                    if char.y < win.get_height() - 190:
                        char.y += (char.jumpCount ** 2)
                        char.jumpCount -= 1
                        char.hitbox = (char.x + 25, char.y + 11, 60, 97)
                    else:
                        char.y = win.get_height()-190
                        char.jumpCount = 10
                        char.isJump = False

                    for bari in barList[LevelRecord]:
                        if char.hitbox[1] + char.hitbox[3] >= bari.hitbox[1] and char.hitbox[1] <= bari.hitbox[1] + \
                                bari.hitbox[3]:
                            if char.hitbox[0] + char.hitbox[2] >= bari.hitbox[0] and char.hitbox[0] <= bari.hitbox[0] + \
                                    bari.hitbox[2]:
                                if char.hitbox[1] >= bari.hitbox[1] + bari.hitbox[3] // 2:
                                    bari.Tiles = False
                                    char.y = bari.hitbox[1] + bari.hitbox[3]
                                    char.isJump = True
                                    char.jumpCount = -1
                                else:
                                    char.y = bari.hitbox[1] - char.hitbox[3]
                                    char.isJump  = False
                                    char.jumpCount = 10

                                for kibar in barList[LevelRecord]:
                                    if kibar != bari:
                                        kibar.Tiles = False
                                        kibar.BarJump = False
                                        kibar.jumpCount = -1
                                for kibarr in barrier:
                                    kibarr.barrTiles = False
                                    kibarr.BarrJump = False
                                    kibarr.BarrjumpCount = -1

                                char.hitbox = (char.x + 25, char.y + 11, 60, 97)

                    for barri in barrier:
                        if char.hitbox[1] + char.hitbox[3] >= barri.hitbox[1] and char.hitbox[1] <= barri.hitbox[1] + \
                                barri.hitbox[3]:
                            if char.hitbox[0] + char.hitbox[2] >= barri.hitbox[0] and char.hitbox[0] <= barri.hitbox[0] + \
                                    barri.hitbox[2]:
                                if char.hitbox[1] > barri.hitbox[1] + barri.hitbox[3] // 2:
                                    barri.barrTiles = False
                                    char.y = barri.hitbox[1] + barri.hitbox[3]
                                    char.isJump = True
                                    char.jumpCount = -1
                                else:
                                    char.y = barri.hitbox[1] - char.hitbox[3]
                                    char.isJump= False
                                    char.jumpCount = 10

                                for kibarr in barrier:
                                    if kibarr != barri:
                                        kibarr.barrTiles = False
                                        kibarr.BarrJump = False
                                        kibarr.BarrjumpCount = -1
                                for kibar in barList[LevelRecord]:
                                    kibar.Tiles = False
                                    kibar.BarJump = False
                                    kibar.jumpCount = -1
                                char.hitbox = (char.x + 25, char.y + 11, 60, 97)




    for bari in barList[LevelRecord]:
        if bari.BarJump:
            if char.y < win.get_height() - 190:
                    char.y += (bari.jumpCount ** 2)
                    bari.jumpCount -= 1
            else:
                char.y = win.get_height() - 190
                char.jumpCount = 10
                bari.BarJump = False
                bari.jumpCount = -1
        char.hitbox = (char.x + 25, char.y + 11, 60, 97)

    for bari in barList[LevelRecord]:
        if char.hitbox[1] + char.hitbox[3] >= bari.hitbox[1] and char.hitbox[1] <= bari.hitbox[1] + bari.hitbox[3]:
            if char.hitbox[0] + char.hitbox[2] >= bari.hitbox[0] and char.hitbox[0] <= bari.hitbox[0] + bari.hitbox[2]:
                if char.hitbox[1] > bari.hitbox[1]+bari.hitbox[3]//2:
                    bari.Tiles = False
                    char.y = bari.hitbox[1]+bari.hitbox[3]
                    char.isJump = True
                    char.jumpCount = -1
                else:
                    if not bari.Tiles:
                        char.y = bari.hitbox[1]-char.hitbox[3]
                        char.isJump = False
                        char.jumpCount = 10
                        bari.Tiles = True
                for kibar in barList[LevelRecord]:
                    if kibar != bari:
                        kibar.Tiles = False
                        kibar.BarJump = False
                        kibar.jumpCount = -1
                for kibarr in barrier:
                    kibarr.barrTiles = False
                    kibarr.BarrJump = False
                    kibarr.BarrjumpCount = -1
            elif bari.Tiles:
                    bari.BarJump = True
                    bari.jumpCount = -1
                    bari.Tiles = False
                    for kibarr in barrier:
                        kibarr.barrTiles = False
                        kibarr.BarrJump = False
                        kibarr.BarrjumpCount = -1

        char.hitbox = (char.x + 25, char.y + 11, 60, 97)




    for barri in barrier:
        if barri.BarrJump:
            if char.y < win.get_height() - 190:
                    char.y += (barri.BarrjumpCount ** 2)
                    barri.BarrjumpCount -= 1
            else:
                barri.BarrjumpCount = -1
                barri.BarrJump = False
                char.y = win.get_height() - 190
                char.jumpCount = 10
        char.hitbox = (char.x + 25, char.y + 11, 60, 97)



    for barri in barrier:

        if char.hitbox[1] + char.hitbox[3] >= barri.hitbox[1] and char.hitbox[1] <= barri.hitbox[1] + barri.hitbox[3]:
            if char.hitbox[0] + char.hitbox[2] >= barri.hitbox[0] and char.hitbox[0] <= barri.hitbox[0] + barri.hitbox[2]:
                if char.hitbox[1] > barri.hitbox[1] + barri.hitbox[3]//2:
                    barri.barrTiles = False
                    char.y = barri.hitbox[1] + barri.hitbox[3]
                    char.isJump = True
                    char.jumpCount = -1
                else:
                    if not barri.barrTiles:
                        char.y = barri.hitbox[1] - char.hitbox[3]
                        char.isJump = False
                        char.jumpCount = 10
                        barri.barrTiles = True

                for kibarr in barrier:
                    if kibarr != barri:
                        kibarr.barrTiles = False
                        kibarr.BarrJump = False
                        kibarr.BarrjumpCount = -1
                for kibar in barList[LevelRecord]:
                    kibar.Tiles = False
                    kibar.BarJump = False
                    kibar.jumpCount = -1

            elif barri.barrTiles:
                barri.BarrJump = True
                barri.BarrjumpCount = -1
                barri.barrTiles = False

        char.hitbox = (char.x + 25, char.y + 11, 60, 97)

    if char.x > win_width and bgtrack < 4:
        barrier.clear()
        LevelRecord += 1
        if LevelRecord == 4:
            starter = 0
            LevelRecord = 0
            win = pygame.display.set_mode((screen_width - screen_width // 2, screen_height - screen_height // 4))
        bgtrack += 1
        char.x = 0
        gemslist.clear()
        gemslist = [Gems(random.choice(range(100, 700)), random.choice(range(100, 500)),
                         random.choice([0, 1, 1, 1, 1, 2, 3, 4])),
                    Gems(random.choice(range(100, 700)), random.choice(range(100, 500)),
                         random.choice([0, 1, 1, 1, 1, 2, 3, 4]))
            , Gems(random.choice(range(100, 700)), random.choice(range(100, 500)),
                   random.choice([0, 1, 1, 1, 1, 2, 3, 4])),
                    Gems(random.choice(range(100, 700)), random.choice(range(100, 500)),
                         random.choice([0, 1, 1, 1, 1, 2, 3, 4]))
            , Gems(random.choice(range(100, 700)), random.choice(range(100, 500)),
                   random.choice([0, 1, 1, 1, 1, 2, 3, 4])),
                    Gems(random.choice(range(100, 700)), random.choice(range(100, 500)),
                         random.choice([0, 1, 1, 1, 1, 2, 3, 4]))
            , Gems(random.choice(range(100, 700)), random.choice(range(400, 500)),
                   random.choice([0, 1, 1, 1, 1, 2, 3, 4])),
                    Gems(random.choice(range(700, 800)), random.choice(range(100, 500)),
                         random.choice([0, 1, 1, 1, 1, 2, 3, 4]))
                    ]

    elif char.x < 0 and bgtrack>0:
        # bgtrack -= 1
        char.x= 0
        # char.x = win.get_width()

    refreshWin()
