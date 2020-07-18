
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
                
                holdtime = msg('message'[-1:0]) 
                
                #CONTROL STICK
                if msg == "left": 
                    pyautogui.keyDown('left')
                    time.sleep(0.1 * holdtime)
                    pyautogui.keyUp('left')
                    print "LEFT pressed by " + str(message['username'])
                if msg == "hammer": 
                    pyautogui.keyDown('left')
                    time.sleep(1)
                    pyautogui.keyUp('left')
                    print "HAMMER pressed by " + str(message['username'])
                if msg == "right": 
                    pyautogui.keyDown('right')
                    time.sleep(0.1 * holdtime)
                    pyautogui.keyUp('right')
                    print "RIGHT pressed by " + str(message['username']) 

                if msg == "up": 
                    pyautogui.keyDown('up')
                    time.sleep(0.1 * holdtime)
                    pyautogui.keyUp('up')
                    print "UP pressed by " + str(message['username']) 

                if msg == "down": 
                    pyautogui.keyDown('down')
                    time.sleep(0.1 * holdtime)
                    pyautogui.keyUp('down')
                    print "DOWN pressed by " + str(message['username']) 

                #CON JUMP
                if msg == "jleft": 
                    pyautogui.keyDown('a')
                    pyautogui.keyDown('left')
                    time.sleep(0.1 * holdtime)
                    pyautogui.keyUp('left')
                    pyautogui.keyUp('a')
                    print "JLEFT pressed by " + str(message['username'])
                
                if msg == "jright": 
                    pyautogui.keyDown('a')
                    pyautogui.keyDown('right')
                    time.sleep(0.1 * holdtime)
                    pyautogui.keyUp('right')
                    pyautogui.keyUp('a')
                    print "JRIGHT pressed by " + str(message['username']) 

                if msg == "jup": 
                    pyautogui.keyDown('a')
                    pyautogui.keyDown('up')
                    time.sleep(0.1 * holdtime)
                    pyautogui.keyUp('up')
                    pyautogui.keyUp('a')
                    print "JUP pressed by " + str(message['username']) 

                if msg == "jdown": 
                    pyautogui.keyDown('a')
                    pyautogui.keyDown('down')
                    time.sleep(0.1 * holdtime)
                    pyautogui.keyUp('down')
                    pyautogui.keyUp('a')
                    print "JDOWN pressed by " + str(message['username']) 
                
                
                #C STICK
                if msg == "cup": 
                    pyautogui.keyDown('1')
                    time.sleep(0.1 * holdtime)
                    pyautogui.keyUp('1')
                    print "C UP pressed by " + str(message['username']) 
                
                if msg == "cdown": 
                    pyautogui.keyDown('2')
                    time.sleep(0.1 * holdtime)
                    pyautogui.keyUp('2')
                    print "C DOWN pressed by " + str(message['username']) 

                if msg == "cleft": 
                    pyautogui.keyDown('3')
                    time.sleep(0.1 * holdtime)
                    pyautogui.keyUp('3')
                    print "C LEFT pressed by " + str(message['username']) 

                if msg == "cright": 
                    pyautogui.keyDown('4')
                    time.sleep(0.1 * holdtime)
                    pyautogui.keyUp('4')
                    print "C RIGHT pressed by " + str(message['username']) 


                #D PAD
                if msg == "dup": 
                    pyautogui.keyDown('5')
                    time.sleep(0.1 * holdtime)
                    pyautogui.keyUp('5')
                    print "D UP pressed by " + str(message['username']) 
                
                if msg == "ddown": 
                    pyautogui.keyDown('6')
                    time.sleep(0.1 * holdtime)
                    pyautogui.keyUp('6')
                    print "D DOWN pressed by " + str(message['username']) 

                if msg == "dright": 
                    pyautogui.keyDown('8')
                    time.sleep(0.1 * holdtime)
                    pyautogui.keyUp('8')
                    print "D RIGHT pressed by " + str(message['username']) 
                
                if msg == "dleft": 
                    pyautogui.keyDown('7')
                    time.sleep(0.1 * holdtime)
                    pyautogui.keyUp('7')
                    print "D RIGHT pressed by " + str(message['username']) 


                #BUTTONS

                if msg == "a":
                    pyautogui.keyDown('a')
                    time.sleep(0.1 * holdtime)
                    pyautogui.keyUp('a')
                    print "A pressed by " + str(message['username']) 

                if msg == "b": 
                    pyautogui.keyDown('b')
                    time.sleep(0.1 * holdtime)
                    pyautogui.keyUp('b')
                    print "B pressed by " + str(message['username']) 

                if msg == "x": 
                    pyautogui.keyDown('x')
                    time.sleep(0.1 * holdtime)
                    pyautogui.keyUp('x')
                    print "X pressed by " + str(message['username']) 

                if msg == "y": 
                    pyautogui.keyDown('y')
                    time.sleep(0.1 * holdtime)
                    pyautogui.keyUp('y')
                    print "Y pressed by " + str(message['username']) 

                if msg == "z": 
                    pyautogui.keyDown('z')
                    time.sleep(0.1 * holdtime)
                    pyautogui.keyUp('z')
                    print "Z pressed by " + str(message['username']) 

                if msg == "l": 
                    pyautogui.keyDown('l')
                    time.sleep(0.1 * holdtime)
                    pyautogui.keyUp('l')
                    print "L pressed by " + str(message['username']) 

                if msg == "r": 
                    pyautogui.keyDown('r')
                    time.sleep(0.1 * holdtime)
                    pyautogui.keyUp('r')
                    print "R pressed by " + str(message['username']) 


        except:
            # There was some error trying to process this chat message. Simply move on to the next message.
            print('Encountered an exception while reading chat.')
