import RPi.GPIO as GPIO
import time
import pygame

print "init pygame"
pygame.init()
print "load cry"
pygame.mixer.music.load("/home/pi/crymachine/python/cry2.wav")


print "starting..."
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4, GPIO.OUT)

GPIO.output(4, True)

while True:
  input_state = GPIO.input(18)
  if input_state == False:
    print('Button 18 Pressed')
    GPIO.output(4, True)
    pygame.mixer.music.play()
    #pygame.event.wait()
    time.sleep(0.2)
  input_state = GPIO.input(24)
  if input_state == False:
    print('Button 24 Pressed')
    pygame.mixer.music.stop()
    time.sleep(0.2)
    GPIO.output(4, False)
