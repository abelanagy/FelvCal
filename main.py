from tkinter import *
from tkinter import messagebox
import time
root = Tk()
root.title("FelvKal")
root.iconbitmap("C:/Users/abeln/Documents/Python - Sk/FelvCal/calculator.svg")
root.geometry("238x430")
root.configure(bg="#1b263b", highlightcolor="#415a77")
var = IntVar()
var2 = IntVar()
clicked0 = StringVar()
clicked0b = StringVar()
clicked1 = StringVar()
clicked2 = StringVar()
clicked3 = StringVar()


def found():
    talalat = Label(frame, text="1 találat", fg="green", bg="#1b263b")
    talalat.grid(row=4, columnspan=2)


def notfound():
    talalat = Label(frame, text="0 találat", fg="red", bg="#1b263b")
    talalat.grid(row=4, columnspan=2)


def hibak():
    if e1.get() == "":
        messagebox.showwarning("Hiba", "Kérlek írd be a magyar pontszámodat!")
        return True
    elif e2.get() == "":
        messagebox.showwarning(
            "Hiba", "Kérlek írd be a matematika pontszámodat!")
        return True
    elif e3.get() == "":
        messagebox.showwarning("Hiba", "Kérlek írd be a szóbeli pontszámodat!")
        return True
    elif e4.get() == "":
        messagebox.showwarning("Hiba", "Kérlek írd be a hozott pontszámodat!")
        return True
    elif int(e1.get()) > 50:
        messagebox.showwarning(
            "Hiba", "A magyar pontszámod nem lehet nagyobb 50-nél!")
        return True
    elif int(e2.get()) > 50:
        messagebox.showwarning(
            "Hiba", "A matematika pontszámod nem lehet nagyobb 50-nél!")
        return True
    elif int(e1.get()) < 0:
        messagebox.showwarning(
            "Hiba", "A magyar pontszámod nem lehet kisebb 0-nál!")
        return True
    elif int(e2.get()) < 0:
        messagebox.showwarning(
            "Hiba", "A matematika pontszámod nem lehet kisebb 0-nál!")
        return True
    else:
        return False


def cal():
    if hibak():
        pass
    else:
        ans = (int(e1.get()) * float(clicked1.get()) + int(e2.get()) *
               float(clicked2.get())) * float(clicked3.get()) + int(e3.get()) + int(e4.get())
        messagebox.showinfo("Eredmény", f"A pontod: {ans}")


def changedTagozat():
    global talalat
    s = clicked0.get()
    s_e5 = e5.get()
    if s == "Ady":
        clicked1.set("1.0")
        clicked2.set("1.0")
        clicked3.set("1.0")
        talalat = Label(frame, text="1 találat", fg="green", bg="#1b263b")
        talalat.grid(row=4, columnspan=2)
    elif s == "Eötvös":
        if s_e5 == "0001" or s_e5 == "0002":
            clicked1.set("0.8")
            clicked2.set("1.2")
            clicked3.set("1.1")
            found()
        elif s_e5 == "0003":
            clicked1.set("1.2")
            clicked2.set("0.8")
            clicked3.set("1.1")
            found()
        elif s_e5 == "0007" or s_e5 == "0008":
            clicked1.set("1.0")
            clicked2.set("1.0")
            clicked3.set("1.1")
            found()
        else:
            notfound()
    elif s == "Kőrösi":
        if s_e5 == "0001" or s_e5 == "0002" or s_e5 == "0003" or s_e5 == "0011":
            clicked1.set("1.0")
            clicked2.set("1.0")
            clicked3.set("1.0")
            found()
        else:
            notfound()
    else:
        notfound()


def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    clicked0.set("Válassz iskolát!")
    clicked1.set("1.0")
    clicked2.set("1.0")
    clicked3.set("1.0")


# FRAMES
frame = LabelFrame(root, text="Iskolaválasztó",
                   bg="#1b263b", fg="#e0e1dd", padx=3.5, pady=3.5)
frame.grid(row=2, column=0, columnspan=2)

l0c = Label(frame, text="Tagozatkód:", bg="#1b263b", fg="#e0e1dd")
l0c.grid(row=2, column=0, pady=3.5, sticky="w")
e5 = Entry(frame, bg="#415a77",
           borderwidth=0, justify="center", fg="#e0e1dd")
e5.grid(row=2, column=1)
changedTagozatB = Button(frame, text="Keress!", command=changedTagozat, bg="#415a77", fg="#e0e1dd",
                         activebackground="#778da9", activeforeground="#e0e1dd", relief="flat", width="8")
changedTagozatB.grid(row=3, column=1)
# LABELS
l0a = Label(root, text="Felvételi kalkulátor", bg="#1b263b", fg="#e0e1dd")
l0a.grid(row=0, columnspan=3, pady=3.5, padx=3)
l0b = Label(frame, text="Iskola:", bg="#1b263b", fg="#e0e1dd")
l0b.grid(row=1, column=0, pady=3.5, sticky="w")
l1 = Label(root, text="Magyar pontszám:", bg="#1b263b", fg="#e0e1dd")
l1.grid(row=4, column=0, pady=3.5, sticky="w", padx=3)
l2 = Label(root, text="Szorzó:", bg="#1b263b", fg="#e0e1dd")
l2.grid(row=5, column=0, pady=3.5, sticky="w", padx=3)
l3 = Label(root, text="Matek pontszám:", bg="#1b263b", fg="#e0e1dd")
l3.grid(row=7, column=0, pady=3.5, sticky="w", padx=3)
l4 = Label(root, text="Szorzó:", bg="#1b263b", fg="#e0e1dd")
l4.grid(row=8, column=0, pady=3.5, sticky="w", padx=3)
l5 = Label(root, text="Írásbeli szorzó:", bg="#1b263b", fg="#e0e1dd")
l5.grid(row=9, column=0, pady=3.5, sticky="w", padx=3)
l6 = Label(root, text="Szóbeli:", bg="#1b263b", fg="#e0e1dd")
l6.grid(row=13, column=0, pady=3.5, sticky="w", padx=3)
l7 = Label(root, text="Hozott jegyek:", bg="#1b263b",
           fg="#e0e1dd")
l7.grid(row=14, column=0, pady=3.5, sticky="w", padx=3)


# ENTRIES
e1 = Entry(root, bg="#415a77",
           borderwidth=0, justify="center", fg="#e0e1dd")
e1.grid(row=4, column=1, pady=3.5)
e2 = Entry(root, bg="#415a77",
           borderwidth=0, justify="center", fg="#e0e1dd")
e2.grid(row=7, column=1, pady=3.5)
e3 = Entry(root, bg="#415a77",
           borderwidth=0, justify="center", fg="#e0e1dd")
e3.grid(row=13, column=1, pady=3.5)
e4 = Entry(root, bg="#415a77",
           borderwidth=0, justify="center", fg="#e0e1dd")
e4.grid(row=14, column=1, pady=3.5)


# MENUS
drop0 = OptionMenu(frame, clicked0, "Ady", "Kőrösi",
                   "Eötvös", "Madách", "Teleki", "Berzsenyi", "Könyves", "AKG", "Kölcsey")
drop0.config(bg="#415a77", fg="#e0e1dd",
             activebackground="#778da9", activeforeground="#e0e1dd")
drop0.grid(row=1, column=1, pady=3.5)
clicked0.set("Válassz iskolát!")
drop1 = OptionMenu(root, clicked1, "0.5", "0.8",
                   "1.0", "1.1", "1.2", "1.5", "2.0")
drop1.config(bg="#415a77", fg="#e0e1dd",
             activebackground="#778da9", activeforeground="#e0e1dd")
drop1.grid(row=5, column=1, pady=3.5)
clicked1.set("1.0")
drop2 = OptionMenu(root, clicked2, "0.5", "0.8", "0.9",
                   "1.0", "1.1", "1.2", "1.5", "2.0")
drop2.config(bg="#415a77", fg="#e0e1dd",
             activebackground="#778da9", activeforeground="#e0e1dd")
drop2.grid(row=8, column=1, pady=3.5)
clicked2.set("1.0")
drop3 = OptionMenu(root, clicked3, "0.5", "0.8", "0.9",
                   "1.0", "1.1", "1.2", "1.5", "2.0")
drop3.config(bg="#415a77", fg="#e0e1dd",
             activebackground="#778da9", activeforeground="#e0e1dd")
drop3.grid(row=9, column=1, pady=3.5)
clicked3.set("1.0")


# BUTTONS
calB = Button(root, text="Számolj!", command=cal, bg="#415a77", fg="#e0e1dd",
              activebackground="#778da9", activeforeground="#e0e1dd", relief="flat", width="8")
calB.grid(row=15, column=1, pady=3.5)
clearB = Button(root, text="Törlés", command=clear, bg="#415a77", fg="#e0e1dd",
                activebackground="#778da9", activeforeground="#e0e1dd", relief="flat", width="8")
clearB.grid(row=15, column=0, pady=3.5)
root.mainloop()
