import pyautogui as gui


def prim(num):
    i = 2
    pri = True
    while i < num or num == 1:
        if num % i == 0 or num == 1:
            gui.alert(text=f"A {inp1} nem prímszám",
                      title="Prímszám ellenőrző", button="OK")
            pri = False
            break
        else:
            i = i + 1
            continue
        break
    if pri != False and num != 1:
        gui.alert(text=f"A {inp1} prímszám",
                  title="Prímszám ellenőrző", button="OK")


while True:
    inp1 = gui.prompt(text="Melyik számot szeretnéd ellenőrizni?",
                      title="Prímszám ellenőrző")
    if str(inp1) != "q" and inp1:
        prim(int(inp1))
    else:
        break
