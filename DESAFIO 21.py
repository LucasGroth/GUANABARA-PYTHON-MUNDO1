#um programa que abra e reproduza um arquivo MP3.
import pygame
pygame.init()
pygame.mixer.music.load('Oh The Larceny - Man On A Mission  (Official Audio) - Position Music (youtube).mp3')
pygame.mixer.music.play()
input('Aperte Enter para sair')
pygame.quit()