#!/usr/bin/python3

from gpiozero import Button
from signal import pause
from wakeonlan import send_magic_packet


button = Button(2)
button2 = Button(3)


# MAC addresses; replace X by actual address
MAC_GAMING = "XX:XX:XX:XX:XX:XX"
MAC_CLIENT = "XX:XX:XX:XX:XX:XX"


def start_gamingserver():
    print("Button is pressed")
    send_magic_packet(MAC_GAMING)


def start_clientserver():
    print("Button is pressed")
    send_magic_packet(MAC_CLIENT)


button.when_pressed = start_gamingserver
button2.when_pressed = start_clientserver

pause()
