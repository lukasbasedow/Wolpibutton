from gpiozero import Button
from signal import pause
from wakeonlan import send_magic_packet

button = Button(2)
button2 = Button(3)

#print("Button is pressed")
#send_magic_packet('xxx')

def start_gamingserver():
    print("Button is pressed")
    send_magic_packet('xxxx')


def start_clientserver():
    print("Button is pressed")
    send_magic_packet('xxxx')

button.when_pressed = start_gamingserver
button2.when_pressed = start_clientserver

pause()
