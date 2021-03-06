from subprocess import call
import RPi.GPIO as GPIO
import time
import datetime
import threading
import notify

#GPIO pin set
lightsensor = 21
callsw = 16
pinponled = 26
callled = 20


#Setmode set
GPIO.setmode(GPIO.BCM)

#GPIO setup
GPIO.setup(lightsensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(callsw, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pinponled, GPIO.OUT)
GPIO.setup(callled, GPIO.OUT)



#sensor history, flag init
swinfo = GPIO.input(lightsensor)

lighthis = ['his0', 'his1', 'his2', 'his3', 'his4', 'his5', 'his6', 'his7', ]

his0 = 0
his1 = 0
his2 = 0
his3 = 0
his4 = 0
his5 = 0
his6 = 0
his7 = 0

pinponflag = False
tenmetu = False

#Setting func
class ledflash:
  def blink(led):
    global tenmetu
    tenmetu = True
    while tenmetu == True:
      GPIO.output(led, True)
      time.sleep(0.125)
      GPIO.output(led, False)
      time.sleep(0.125)
    else:
      GPIO.output(led, False)

  def lit(led):
    GPIO.output(led, True)

  def stop(led):
    global tenmetu
    tenmetu = False
    GPIO.output(led, False)


def PinPonNotify():
  global pinponflag
  pinponflag = True
  print('PinPonDetected!', datetime.datetime.now())
  threading.Thread(target=ledflash.blink, args=(pinponled,)).start()
  notify.linenotify('お客様がお見えです')
  notify.alexanotify('お客様がお見えです')
  notify.homebridgenotify()
  notify.misskeynotify()
  ledflash.stop(pinponled)
  time.sleep(0.3)
  ledflash.lit(pinponled)
  time.sleep(10)
  ledflash.stop(pinponled)
  pinponflag = False
  print('PinPonReset!')

def PinPonDetect():
  global pinponflag
  if pinponflag == False:
    notfy = threading.Thread(target=PinPonNotify)
    notfy.start()
  else:
    pass

def CallNotify(pin):
  threading.Thread(target=ledflash.blink, args=(callled,)).start()
  notify.linenotify('ボタンが押されました')
  notify.alexanotify('お呼び出しされています')
  ledflash.stop(pinponled)
  time.sleep(0.3)
  ledflash.lit(callled)
  time.sleep(2)
  ledflash.stop(callled)

#GPIO interrupt setting
GPIO.add_event_detect(callsw, GPIO.RISING, callback=CallNotify, bouncetime=5000)

#Main roop
while True:
  try:
    #print('LoopStart!')
    for i in range(8):
      execcom = 'his' + str(i) + ' = GPIO.input(lightsensor)'
      exec(execcom)
      #print(GPIO.input(sw))

      if his0 == his1 == his4 == his5 == 0 and his2 == his3 == his6 == his7 == 1:
        PinPonDetect()
        #print('PinPon!')
      if his0 == his1 == his4 == his5 == 1 and his2 == his3 == his6 == his7 == 0:
        PinPonDetect()
        #print('PinPon!')
      if his1 == his2 == his5 == his6 == 1 and his0 == his3 == his4 == his7 == 0:
        PinPonDetect()
        #print('PinPon!')
      if his1 == his2 == his5 == his6 == 0 and his0 == his3 == his4 == his7 == 1:
        PinPonDetect()
        #print('PinPon!')
      #if i == 7:
        #print('LoopReset!(Scanned 8 times so reset the loop.)')

      
      time.sleep(0.0625)
  except KeyboardInterrupt:
    GPIO.cleanup()
    break

    
#Trash code

#while True:
#  try:
#    print(GPIO.input(sw))
#    GPIO.output(led, GPIO.input(sw))
#    time.sleep(0.0625)
#  except KeyboardInterrupt:
#    GPIO.cleanup()
#    break