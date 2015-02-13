import pygame, serial, time

numpins = 12
previnputs = [False for a in range(0, numpins)]

if True:
    ser = serial.Serial('/dev/ttyACM0', 9600)
    ser1= serial.Serial('/dev/ttyACM2', 9600)

pygame.mixer.pre_init(channels=6, buffer=1024)
pygame.mixer.init()

guit_let = ["a", "b", "b1", "c", "c1", "d","e", "e1", "f", "f1", "g","g1"]
guitar_notes = [pygame.mixer.Sound("newsounds/"+letter+".wav") for letter in guit_let]


def guitar(i):
    guitar_notes[i].play()

count = 0

while True:
    
    line = ""
    if True:
        line = ser.readline()
        print line
    else:
        line = raw_input()
    line += ser1.readline() 
    print line

    for i in range(0, numpins):
        curr = line[i] != '0'
        prev = previnputs[i]
        if curr and not prev:
            guitar(i)
        previnputs[i] = curr

