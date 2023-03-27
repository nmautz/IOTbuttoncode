from gpiozero import Button
import time


button = Button(2)
button2 = Button(3)

while True:
  if button.is_pressed or button2.is_pressed:
    if button.is_pressed :
      print("Pressed button 1")
      f = open("../../SmartAlarmClockWeb/alarm.json")
      print(f.read())
      time.sleep(0.5)
      
    else:
      print("Pressed button 2")
      time.sleep(0.5)