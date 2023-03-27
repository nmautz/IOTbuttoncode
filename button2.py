from gpiozero import Button
import time
import json


button = Button(2)
button2 = Button(3)

while True:
  if button.is_pressed or button2.is_pressed:
    if button.is_pressed :
      print("Pressed button 1")
      f = open("../../SmartAlarmClockWeb/alarm.json")
      file_string = f.read()
      file_json = json.loads(file_string)
      print(file_json["enabled"])
      file_json["enabled"] = true
      file_string = json.dumps(file_json)
      f.close()
      f = open("../../SmartAlarmClockWeb/alarm.json", 'w')
      f.write(file_string)
      f.close()

      time.sleep(0.5)
      
    else:
      print("Pressed button 2")
      f = open("../../SmartAlarmClockWeb/alarm.json")
      file_string = f.read()
      file_json = json.loads(file_string)
      print(file_json["enabled"])
      file_json["enabled"] = false
      file_string = json.dumps(file_json)
      f.close()
      f = open("../../SmartAlarmClockWeb/alarm.json", 'w')
      f.write(file_string)
      f.close()
      time.sleep(0.5)
