import time, pyautogui, os

path = r"path to folder with text file"
os.chdir(path)
f = open("text.txt", "r")
f = f.read()
f = f.split()
time.sleep(5)
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press('enter')
    time.sleep(1)