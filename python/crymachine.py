import RPi.GPIO as GPIO
import time
import pygame
from random import randint
import threading

print "init pygame"
pygame.init()

print "starting..."
GPIO.setmode(GPIO.BCM)
#define inputs/outputs
#inputs
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)#deactivate button
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)#cry
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)#laugh
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)#gouzigouzi
#outputs
GPIO.setup(22, GPIO.OUT)#system on - red LED
GPIO.setup(4 , GPIO.OUT)#audio on  - yellow LED

#light system on LED
GPIO.output(22, True)

#--------------------------
#thread definition for button management
#--------------------------
def buttons_management():
	print ("debut thread 1")
	while True:
		#RAZ Button
		input_state = GPIO.input(18)
		if input_state == False:
			print('Button 18 Pressed :  RAZ Button')
			GPIO.output(4, False)#close light
			pygame.mixer.music.stop()
			#pygame.event.wait()
			time.sleep(0.2)
		input_state = GPIO.input(24)
		if input_state == False:
			print('Button 24 Pressed : baby cry')
			GPIO.output(4, True)
			pygame.mixer.music.load("/home/pi/crymachine/python/cry2.wav")#load cry file
			pygame.mixer.music.play(-1)
			time.sleep(0.2)
		input_state = GPIO.input(16)
		if input_state == False:
			print('Button 16 Pressed : baby laugh')
			GPIO.output(4, True)
			pygame.mixer.music.load("/home/pi/crymachine/python/laugh1.wav")#load laugh file
			pygame.mixer.music.play(-1)
			time.sleep(0.2)
		input_state = GPIO.input(12)
		if input_state == False:
			print('Button 12 Pressed : baby laugh2')
			GPIO.output(4, True)
			pygame.mixer.music.load("/home/pi/crymachine/python/laugh2_2.wav")#load cry file
			pygame.mixer.music.play(-1)
			time.sleep(0.2)
	
#--------------------------
#thread definition for button management
#--------------------------
def random_cry():
	while True:
		#wait random number of seconds between 3600*2 seconds and 3600*4 seconds
		wait_time = randint(3600*2,3600*4)
		print ("random cry : wait :")
		print (wait_time)
		time.sleep(wait_time)
		print('Automatic cry on Baby')
		pygame.mixer.music.load("/home/pi/crymachine/python/cry2.wav")
		GPIO.output(4, True)
		pygame.mixer.music.play(-1)
		
		
#------------------------------
# Main Call
#------------------------------
print ("creation thread 1")
btm = threading.Thread(target=buttons_management) 
print ("creation thread 2")
rdm = threading.Thread(target=random_cry)
print ("start thread 1")
btm.start() 
print ("start thread 2")
rdm.start()
		
