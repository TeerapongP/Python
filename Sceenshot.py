import pyautogui
from PIL import ImageGrab
snapshot = ImageGrab.grab()
snapshot.save("MyScreenShot.jpg")
screenshot = pyautogui.screenshot("MyScreenShot.jpg")