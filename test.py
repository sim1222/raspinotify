import RPi.GPIO as GPIO
import time

sw = 20
led = 21

GPIO.setmode(GPIO.BCM)

#GPIO.setup(sw, GPIO.IN)
GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT)

swinfo = GPIO.input(sw)

while True:
  try:
    print(GPIO.input(sw))
    GPIO.output(led, GPIO.input(sw))
    time.sleep(0.0625)
  except KeyboardInterrupt:
    GPIO.cleanup()
    break