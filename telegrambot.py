import time,datetime 
import RPi.GPIO as GPIO 
import telepot 
import sys 
def on(pin):        
  GPIO.output(pin,GPIO.HIGH)        
  return 
def off(pin):        
  GPIO.output(pin,GPIO.LOW)        
  return 
GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False) 
GPIO.setup(11,GPIO.OUT) 
def handle(msg):    
  chat_id=msg['chat']['id']    
  command=msg['text']    
  print('Got command:%s' % command)    
  if command=='on':        
    bot.sendMessage(chat_id,on (11))    
  elif command=='off':       
    bot.sendMessage(chat_id,off (11))                                           
bot=telepot.Bot('5329577491:AAHhKMS0XTk-H2DMAVMwI69hoN9vWXVGKfk') 
bot.message_loop(handle) 
print("I am Listening....") 
while 1:   
   try:        
    time.sleep(10)    
   except keyboardInterrupt:       
     print('/ program interrupt')        
     GPIO.cleanup()        
     exit()    
   except:        
     print('other error or exception occured')        
     GPIO.cleanup()