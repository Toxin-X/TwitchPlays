
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
                
                #if message's last charecter is a number
                if msg[-1].isdigit():
                    htime = int(msg[-1])
                
                if not msg[-1].isdigit():
                    htime = 1 
                #CONTROL STICK
                if msg.startswith("left"): 
                    pyautogui.keyDown('left')
                    time.sleep(0.1 * htime)
                    pyautogui.keyUp('left')
                    print ("LEFT " + str(htime) + " pressed by " + str(message['username']))
                if msg.startswith("right"): 
                    pyautogui.keyDown('right')
                    time.sleep(0.1 * htime)
                    pyautogui.keyUp('right')
                    print ("RIGHT " + str(htime) + " pressed by " + str(message['username'])) 

                if msg.startswith("up"): 
                    pyautogui.keyDown('up')
                    time.sleep(0.1 * htime)
                    pyautogui.keyUp('up')
                    print ("UP " + str(htime) + " pressed by " + str(message['username'])) 

                if msg.startswith("down"): 
                    pyautogui.keyDown('down')
                    time.sleep(0.1 * htime)
                    pyautogui.keyUp('down')
                    print ("DOWN " + str(htime) + " pressed by " + str(message['username'])) 

                #CON JUMP
                if msg.startswith("jleft"): 
                    pyautogui.keyDown('a')
                    pyautogui.keyDown('left')
                    time.sleep(0.1 * htime)
                    pyautogui.keyUp('left')
                    pyautogui.keyUp('a')
                    print ("JLEFT " + str(htime) + " pressed by " + str(message['username']))
                
                if msg.startswith("jright"): 
                    pyautogui.keyDown('a')
                    pyautogui.keyDown('right')
                    time.sleep(0.1 * htime)
                    pyautogui.keyUp('right')
                    pyautogui.keyUp('a')
                    print ("JRIGHT " + str(htime) + " pressed by " + str(message['username'])) 

                if msg.startswith("jup"): 
                    pyautogui.keyDown('a')
                    pyautogui.keyDown('up')
                    time.sleep(0.1 * htime)
                    pyautogui.keyUp('up')
                    pyautogui.keyUp('a')
                    print ("JUP " + str(htime) + " pressed by " + str(message['username'])) 

                if msg.startswith("jdown"): 
                    pyautogui.keyDown('a')
                    pyautogui.keyDown('down')
                    time.sleep(0.1 * htime)
                    pyautogui.keyUp('down')
                    pyautogui.keyUp('a')
                    print ("JDOWN " + str(htime) + " pressed by " + str(message['username'])) 
                
                
                #C STICK
                if msg.startswith("cup"): 
                    pyautogui.keyDown('1')
                    time.sleep(0.1 * htime)
                    pyautogui.keyUp('1')
                    print ("C UP " + str(htime) + " pressed by " + str(message['username'])) 
                
                if msg.startswith("cdown"): 
                    pyautogui.keyDown('2')
                    time.sleep(0.1 * htime)
                    pyautogui.keyUp('2')
                    print ("C DOWN " + str(htime) + " pressed by " + str(message['username'])) 

                if msg.startswith("cleft"): 
                    pyautogui.keyDown('3')
                    time.sleep(0.1 * htime)
                    pyautogui.keyUp('3')
                    print ("C LEFT " + str(htime) + " pressed by " + str(message['username'])) 

                if msg.startswith("cright"): 
                    pyautogui.keyDown('4')
                    time.sleep(0.1 * htime)
                    pyautogui.keyUp('4')
                    print ("C RIGHT " + str(htime) + " pressed by " + str(message['username'])) 


                #D PAD
                if msg.startswith("dup"): 
                    pyautogui.keyDown('5')
                    time.sleep(0.1 * htime)
                    pyautogui.keyUp('5')
                    print ("D UP " + str(htime) + " pressed by " + str(message['username'])) 
                
                if msg.startswith("ddown"): 
                    pyautogui.keyDown('6')
                    time.sleep(0.1 * htime)
                    pyautogui.keyUp('6')
                    print ("D DOWN " + str(htime) + " pressed by " + str(message['username'])) 

                if msg.startswith("dright"): 
                    pyautogui.keyDown('8')
                    time.sleep(0.1 * htime)
                    pyautogui.keyUp('8')
                    print ("D RIGHT " + str(htime) + " pressed by " + str(message['username'])) 
                
                if msg.startswith("dleft"): 
                    pyautogui.keyDown('7')
                    time.sleep(0.1 * htime)
                    pyautogui.keyUp('7')
                    print ("D RIGHT " + str(htime) + " pressed by " + str(message['username'])) 


                #BUTTONS

                if msg.startswith("a"):
                    pyautogui.keyDown('a')
                    time.sleep(0.1 * htime)
                    pyautogui.keyUp('a')
                    print ("A " + str(htime) + " pressed by " + str(message['username'])) 

                if msg.startswith("b"): 
                    pyautogui.keyDown('b')
                    time.sleep(0.1 * htime)
                    pyautogui.keyUp('b')
                    print ("B " + str(htime) + " pressed by " + str(message['username'])) 

                if msg.startswith("x"): 
                    pyautogui.keyDown('x')
                    time.sleep(0.1 * htime)
                    pyautogui.keyUp('x')
                    print ("X " + str(htime) + " pressed by " + str(message['username'])) 

                if msg.startswith("y"): 
                    pyautogui.keyDown('y')
                    time.sleep(0.1 * htime)
                    pyautogui.keyUp('y')
                    print ("Y " + str(htime) + " pressed by " + str(message['username'])) 

                if msg.startswith("z"): 
                    pyautogui.keyDown('z')
                    time.sleep(0.1 * htime)
                    pyautogui.keyUp('z')
                    print ("Z " + str(htime) + " pressed by " + str(message['username'])) 

                if msg.startswith("l") and not msg.startswith("left"): 
                    pyautogui.keyDown('l')
                    time.sleep(0.1 * htime)
                    pyautogui.keyUp('l')
                    print ("L " + str(htime) + " pressed by " + str(message['username'])) 

                if msg.startswith("r") and not msg.startswith ("right"): 
                    pyautogui.keyDown('r')
                    time.sleep(0.1 * htime)
                    pyautogui.keyUp('r')
                    print ("R " + str(htime) + " pressed by " + str(message['username'])) 


        except:
            # There was some error trying to process this chat message. Simply move on to the next message.
            print('Encountered an exception while reading chat.')
