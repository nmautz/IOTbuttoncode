from gpiozero import Button


button = Button(2)
button2 = Button(3)

while True:
  if button.is_pressed or button2.is_pressed:
    if button.is_pressed :
      print("Pressed button 1")
    else:
      print("Pressed button 2")