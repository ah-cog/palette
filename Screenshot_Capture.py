import os

# Capture a screenshot
# -x prevents the screenshot sound from playing
# Reference:
# - http://stackoverflow.com/questions/4524723/take-screenshot-in-python-on-mac-os-x
os.system("screencapture -x screenshot.png")
