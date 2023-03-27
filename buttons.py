import asyncio

from gpiozero import Button



async def wait_for_button(i, callback, str):
  button = Button(i)
  button.wait_for_press()
  callback(str)




async def main():

  

  loop = asyncio.get_event_loop()
  loop.create_task(wait_for_button(2, print, "button 1"))
  loop.create_task(wait_for_button(3,print,"button 2"))
  print("hi")


  


asyncio.get_event_loop().run_until_complete(main())


