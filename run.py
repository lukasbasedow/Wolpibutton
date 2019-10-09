#!/usr/bin/python3

from gpiozero import Button
from signal import pause
from wakeonlan import send_magic_packet


button = Button(2)
button2 = Button(3)


# MAC addresses; replace X by actual address
MAC_GAMING = "XX:XX:XX:XX:XX:XX"
MAC_CLIENT = "XX:XX:XX:XX:XX:XX"


def print_button_press(pc_name):
    print(f"Button pressed! Waking up {pc_name} ...")
    return True


def start_gamingserver():
    print_button_press("Gaming Server")
    send_magic_packet(MAC_GAMING)


def start_clientserver():
    print_button_press("Client Server")
    send_magic_packet(MAC_CLIENT)


button.when_pressed = start_gamingserver
button2.when_pressed = start_clientserver

pause()
