
# General imports
import time
import subprocess
import random
import string
from datetime import datetime
# Twitch imports
import TwitchPlays_Connection
from TwitchPlays_AccountInfo import TWITCH_USERNAME, TWITCH_OAUTH_TOKEN

import pyautogui
# An optional countdown before the code actually starts running, so you have time to load up the game before messages are processed.
# TODO: Set the "countdown" variable to whatever countdown length you want.
countdown = 5 #The number of seconds before the code starts running
while countdown > 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)

t = TwitchPlays_Connection.Twitch();
t.twitch_connect(TWITCH_USERNAME, TWITCH_OAUTH_TOKEN);

while True:
    new_messages = t.twitch_recieve_messages();
    if not new_messages:

        continue
    else:
        try:  
            for message in new_messages:
                msg = message['message'].lower()
                username = message['username'].lower()
                             
                #CONTROL STICK
                if msg == "left": 
                    pyautogui.keyDown('left')
                    time.sleep(0.1)
                    pyautogui.keyUp('left')
                    print "LEFT pressed by " + str(message['username'])
                if msg == "right": 
                    pyautogui.keyDown('right')
                    time.sleep(0.1)
                    pyautogui.keyUp('right')
                    print "RIGHT pressed by " + str(message['username']) 

                if msg == "up": 
                    pyautogui.keyDown('up')
                    time.sleep(0.1)
                    pyautogui.keyUp('up')
                    print "UP pressed by " + str(message['username']) 

                if msg == "down": 
                    pyautogui.keyDown('down')
                    time.sleep(0.1)
                    pyautogui.keyUp('down')
                    print "DOWN pressed by " + str(message['username']) 
                
                #CONTROL STICK 0.1s
                if msg == "left1": 
                    pyautogui.keyDown('left')
                    time.sleep(0.1)
                    pyautogui.keyUp('left')
                    print "LEFT1 pressed by " + str(message['username'])
                if msg == "right1": 
                    pyautogui.keyDown('right')
                    time.sleep(0.1)
                    pyautogui.keyUp('right')
                    print "RIGHT1 pressed by " + str(message['username']) 

                if msg == "up1": 
                    pyautogui.keyDown('up')
                    time.sleep(0.1)
                    pyautogui.keyUp('up')
                    print "UP1 pressed by " + str(message['username']) 

                if msg == "down1": 
                    pyautogui.keyDown('down')
                    time.sleep(0.1)
                    pyautogui.keyUp('down')
                    print "DOWN1 pressed by " + str(message['username']) 

                #CONTROL STICK 0.2s
                if msg == "left2": 
                    pyautogui.keyDown('left')
                    time.sleep(0.2)
                    pyautogui.keyUp('left')
                    print "LEFT2 pressed by " + str(message['username'])
                if msg == "right2": 
                    pyautogui.keyDown('right')
                    time.sleep(0.2)
                    pyautogui.keyUp('right')
                    print "RIGHT2 pressed by " + str(message['username']) 

                if msg == "up2": 
                    pyautogui.keyDown('up')
                    time.sleep(0.2)
                    pyautogui.keyUp('up')
                    print "UP2 pressed by " + str(message['username']) 

                if msg == "down2": 
                    pyautogui.keyDown('down')
                    time.sleep(0.2)
                    pyautogui.keyUp('down')
                    print "DOWN2 pressed by " + str(message['username']) 
                
                #CONTROL STICK 0.3s
                if msg == "left3": 
                    pyautogui.keyDown('left')
                    time.sleep(0.3)
                    pyautogui.keyUp('left')
                    print "LEFT3 pressed by " + str(message['username'])
                if msg == "right3": 
                    pyautogui.keyDown('right')
                    time.sleep(0.3)
                    pyautogui.keyUp('right')
                    print "RIGHT3 pressed by " + str(message['username']) 

                if msg == "up3": 
                    pyautogui.keyDown('up')
                    time.sleep(0.3)
                    pyautogui.keyUp('up')
                    print "UP3 pressed by " + str(message['username']) 

                if msg == "down3": 
                    pyautogui.keyDown('down')
                    time.sleep(0.3)
                    pyautogui.keyUp('down')
                    print "DOWN3 pressed by " + str(message['username']) 
                
                #CONTROL STICK 0.4s
                if msg == "left4": 
                    pyautogui.keyDown('left')
                    time.sleep(0.4)
                    pyautogui.keyUp('left')
                    print "LEFT4 pressed by " + str(message['username'])
                if msg == "right4": 
                    pyautogui.keyDown('right')
                    time.sleep(0.4)
                    pyautogui.keyUp('right')
                    print "RIGHT4 pressed by " + str(message['username']) 

                if msg == "up4": 
                    pyautogui.keyDown('up')
                    time.sleep(0.4)
                    pyautogui.keyUp('up')
                    print "UP4 pressed by " + str(message['username']) 

                if msg == "down4": 
                    pyautogui.keyDown('down')
                    time.sleep(0.4)
                    pyautogui.keyUp('down')
                    print "DOWN4 pressed by " + str(message['username']) 
                
                #CONTROL STICK 0.5s
                if msg == "left5": 
                    pyautogui.keyDown('left')
                    time.sleep(0.5)
                    pyautogui.keyUp('left')
                    print "LEFT5 pressed by " + str(message['username'])
                if msg == "right5": 
                    pyautogui.keyDown('right')
                    time.sleep(0.5)
                    pyautogui.keyUp('right')
                    print "RIGHT5 pressed by " + str(message['username']) 

                if msg == "up5": 
                    pyautogui.keyDown('up')
                    time.sleep(0.5)
                    pyautogui.keyUp('up')
                    print "UP5 pressed by " + str(message['username']) 

                if msg == "down5": 
                    pyautogui.keyDown('down')
                    time.sleep(0.5)
                    pyautogui.keyUp('down')
                    print "DOWN5 pressed by " + str(message['username']) 
                
                #CONTROL STICK 0.6s
                if msg == "left6": 
                    pyautogui.keyDown('left')
                    time.sleep(0.6)
                    pyautogui.keyUp('left')
                    print "LEFT6 pressed by " + str(message['username'])
                if msg == "right6": 
                    pyautogui.keyDown('right')
                    time.sleep(0.6)
                    pyautogui.keyUp('right')
                    print "RIGHT6 pressed by " + str(message['username']) 

                if msg == "up6": 
                    pyautogui.keyDown('up')
                    time.sleep(0.6)
                    pyautogui.keyUp('up')
                    print "UP6 pressed by " + str(message['username']) 

                if msg == "down6": 
                    pyautogui.keyDown('down')
                    time.sleep(0.6)
                    pyautogui.keyUp('down')
                    print "DOWN6 pressed by " + str(message['username']) 

                #CONTROL STICK 0.7s
                if msg == "left7": 
                    pyautogui.keyDown('left')
                    time.sleep(0.7)
                    pyautogui.keyUp('left')
                    print "LEFT7 pressed by " + str(message['username'])
                if msg == "right7": 
                    pyautogui.keyDown('right')
                    time.sleep(0.7)
                    pyautogui.keyUp('right')
                    print "RIGHT7 pressed by " + str(message['username']) 

                if msg == "up7": 
                    pyautogui.keyDown('up')
                    time.sleep(0.7)
                    pyautogui.keyUp('up')
                    print "UP7 pressed by " + str(message['username']) 

                if msg == "down7": 
                    pyautogui.keyDown('down')
                    time.sleep(0.7)
                    pyautogui.keyUp('down')
                    print "DOWN7 pressed by " + str(message['username']) 

                #CONTROL STICK 0.8s
                if msg == "left8": 
                    pyautogui.keyDown('left')
                    time.sleep(0.8)
                    pyautogui.keyUp('left')
                    print "LEFT8 pressed by " + str(message['username'])
                if msg == "right8": 
                    pyautogui.keyDown('right')
                    time.sleep(0.8)
                    pyautogui.keyUp('right')
                    print "RIGHT8 pressed by " + str(message['username']) 

                if msg == "up8": 
                    pyautogui.keyDown('up')
                    time.sleep(0.8)
                    pyautogui.keyUp('up')
                    print "UP8 pressed by " + str(message['username']) 

                if msg == "down8": 
                    pyautogui.keyDown('down')
                    time.sleep(0.8)
                    pyautogui.keyUp('down')
                    print "DOWN8 pressed by " + str(message['username']) 
                
                #CONTROL STICK 0.9s
                if msg == "left9": 
                    pyautogui.keyDown('left')
                    time.sleep(0.9)
                    pyautogui.keyUp('left')
                    print "LEFT9 pressed by " + str(message['username'])
                if msg == "right9": 
                    pyautogui.keyDown('right')
                    time.sleep(0.9)
                    pyautogui.keyUp('right')
                    print "RIGHT9 pressed by " + str(message['username']) 

                if msg == "up9": 
                    pyautogui.keyDown('up')
                    time.sleep(0.9)
                    pyautogui.keyUp('up')
                    print "UP9 pressed by " + str(message['username']) 

                if msg == "down9": 
                    pyautogui.keyDown('down')
                    time.sleep(0.9)
                    pyautogui.keyUp('down')
                    print "DOWN9 pressed by " + str(message['username']) 
                
                
                #JUMP DIRECTIONS
                if msg == "jleft": 
                    pyautogui.keyDown('a')
                    pyautogui.keyDown('left')
                    time.sleep(0.1)
                    pyautogui.keyUp('left')
                    pyautogui.keyUp('a')
                    print "JLEFT pressed by " + str(message['username'])
                
                if msg == "jright": 
                    pyautogui.keyDown('a')
                    pyautogui.keyDown('right')
                    time.sleep(0.1)
                    pyautogui.keyUp('right')
                    pyautogui.keyUp('a')
                    print "JRIGHT pressed by " + str(message['username']) 

                if msg == "jup": 
                    pyautogui.keyDown('a')
                    pyautogui.keyDown('up')
                    time.sleep(0.1)
                    pyautogui.keyUp('up')
                    pyautogui.keyUp('a')
                    print "JUP pressed by " + str(message['username']) 

                if msg == "jdown": 
                    pyautogui.keyDown('a')
                    pyautogui.keyDown('down')
                    time.sleep(0.1)
                    pyautogui.keyUp('down')
                    pyautogui.keyUp('a')
                    print "JDOWN pressed by " + str(message['username']) 
                
                
                #C STICK
                if msg == "cup": 
                    pyautogui.keyDown('1')
                    time.sleep(0.1)
                    pyautogui.keyUp('1')
                    print "C UP pressed by " + str(message['username']) 
                
                if msg == "cdown": 
                    pyautogui.keyDown('2')
                    time.sleep(0.1)
                    pyautogui.keyUp('2')
                    print "C DOWN pressed by " + str(message['username']) 

                if msg == "cleft": 
                    pyautogui.keyDown('3')
                    time.sleep(0.1)
                    pyautogui.keyUp('3')
                    print "C LEFT pressed by " + str(message['username']) 

                if msg == "cright": 
                    pyautogui.keyDown('4')
                    time.sleep(0.1)
                    pyautogui.keyUp('4')
                    print "C RIGHT pressed by " + str(message['username']) 


                #D PAD
                if msg == "dup": 
                    pyautogui.keyDown('5')
                    time.sleep(0.1)
                    pyautogui.keyUp('5')
                    print "D UP pressed by " + str(message['username']) 
                
                if msg == "ddown": 
                    pyautogui.keyDown('6')
                    time.sleep(0.1)
                    pyautogui.keyUp('6')
                    print "D DOWN pressed by " + str(message['username']) 

                if msg == "dright": 
                    pyautogui.keyDown('8')
                    time.sleep(0.1)
                    pyautogui.keyUp('8')
                    print "D RIGHT pressed by " + str(message['username']) 
                
                if msg == "dleft": 
                    pyautogui.keyDown('7')
                    time.sleep(0.1)
                    pyautogui.keyUp('7')
                    print "D RIGHT pressed by " + str(message['username']) 


                #BUTTONS

                if msg == "a":
                    pyautogui.keyDown('a')
                    time.sleep(0.1)
                    pyautogui.keyUp('a')
                    print "A pressed by " + str(message['username']) 

                if msg == "b": 
                    pyautogui.keyDown('b')
                    time.sleep(0.1)
                    pyautogui.keyUp('b')
                    print "B pressed by " + str(message['username']) 

                if msg == "x": 
                    pyautogui.keyDown('x')
                    time.sleep(0.1)
                    pyautogui.keyUp('x')
                    print "X pressed by " + str(message['username']) 

                if msg == "y": 
                    pyautogui.keyDown('y')
                    time.sleep(0.1)
                    pyautogui.keyUp('y')
                    print "Y pressed by " + str(message['username']) 

                if msg == "z": 
                    pyautogui.keyDown('z')
                    time.sleep(0.1)
                    pyautogui.keyUp('z')
                    print "Z pressed by " + str(message['username']) 

                if msg == "l": 
                    pyautogui.keyDown('l')
                    time.sleep(0.1)
                    pyautogui.keyUp('l')
                    print "L pressed by " + str(message['username']) 

                if msg == "r": 
                    pyautogui.keyDown('r')
                    time.sleep(0.1)
                    pyautogui.keyUp('r')
                    print "R pressed by " + str(message['username']) 


        except:
            # There was some error trying to process this chat message. Simply move on to the next message.
            print('Encountered an exception while reading chat.')
