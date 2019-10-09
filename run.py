#!/usr/bin/python3
"""
Send WOL (Wake On LAN) packet to a computer in the network.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

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
