import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BCM)

RPi.GPIO.setwarnings(False)

RPi.GPIO.setup(13, RPi.GPIO.OUT)
RPi.GPIO.setup(6, RPi.GPIO.IN)

RPi.GPIO.output(13, RPi.GPIO.input(6))
