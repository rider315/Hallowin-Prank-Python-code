import pygame
from time import sleep

from pygame import image
pygame.init()
window=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.mixer.init()
pygame.mixer.music.load('ratsasan.mp3')
pygame.mixer.music.play()

sleep(2)
pygame.mixer.init()
pygame.mixer.music.load('scary.mp3')

pygame.mixer.music.play()
sleep(1)
image=pygame.image.load('scary.jpg')
window.blit(image,(500,200))
pygame.display.update()
sleep(3)
