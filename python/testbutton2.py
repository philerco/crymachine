import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
        try:
                GPIO.wait_for_edge(23, GPIO.FALLING)
                print "Appui detecte\n"
        except KeyboardInterupt:
                GPIO.cleanup()

GPIO.cleanup()
