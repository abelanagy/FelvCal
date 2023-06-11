from xml.etree.ElementTree import tostring
import pyautogui as gui


def prim(num):
    i = 2
    pri = True
    while i < num or num == 1:
        if num % i == 0 or num == 1:
            gui.alert(text=f"{inp1} is not a prime number",
                      title="Prime number checker", button="OK")
            pri = False
            break
        else:
            i = i + 1
            continue
        break
    if pri != False and num != 1:
        gui.alert(text=f"{inp1} is a prime number",
                  title="Prime number checker", button="OK")


while True:
    inp1 = gui.prompt(text="Which number do you want to check?",
                      title="Prime number checker")
    if str(inp1) != "q" and inp1:
        prim(int(inp1))
    else:
        break
