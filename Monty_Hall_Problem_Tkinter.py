import random, winsound
import tkinter as tk
import os
from tkinter import *
from tkinter import messagebox

MeineTuer = 0
Zahlen_Liste = ["1", "2", "3"]
a, b, c, d = 0, 0, 0, 0
u, v, w = 0, 0, 0
x, y, z = 0, 0, 0

def Moderator():
    global MeineTuer, Preise, Moderator_Wahl
    Preise = ["ziege", "ziege", "auto"]
    random.shuffle(Preise)
    if MeineTuer == 1 or MeineTuer == 2 or MeineTuer == 3:
        MeineTuer = MeineTuer - 1
        while True:
            Moderator_Wahl = random.randrange(3)
            if Preise[Moderator_Wahl] != "auto" and Moderator_Wahl != MeineTuer:
                Spiel_Text.config(text="Behalten oder Wechseln")
                print(Preise)
                Button_Eins.config(command=Zweite_Wahl_Eins)
                Button_Zwei.config(command=Zweite_Wahl_Zwei)
                Button_Drei.config(command=Zweite_Wahl_Drei)

                if Moderator_Wahl == 0:
                    Button_Eins.config(command=nichts, text="ZIEGE", disabledforeground='#a3a3a3', image=Ziege,width="105",height="105")
                    Button_Zwei.config(command=Zweite_Wahl_Zwei)
                    Button_Drei.config(command=Zweite_Wahl_Drei)
                elif Moderator_Wahl == 1:
                    Button_Eins.config(command=Zweite_Wahl_Eins)
                    Button_Zwei.config(command=nichts, text="ZIEGE", disabledforeground='#a3a3a3', image=Ziege,width="105",height="105")
                    Button_Drei.config(command=Zweite_Wahl_Drei)
                elif Moderator_Wahl == 2:
                    Button_Eins.config(command=Zweite_Wahl_Eins)
                    Button_Zwei.config(command=Zweite_Wahl_Zwei)
                    Button_Drei.config(command=nichts, text="ZIEGE", disabledforeground='#a3a3a3', image=Ziege,width="105",height="105")
                break

def nichts():
    pass
            
def Letzte_Runde():
    global Zweite_Wahl, Preise, Moderator_Wahl, Zahlen_Liste, Original_Button_Farbe,a ,b ,u , v ,x ,y
    if Preise[Zweite_Wahl] == "auto":
        Spiel_Text.config(text="Du hast Gewonnen")
        a = a + 1
        winsound.PlaySound("C:/Windows/Media/tada.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)
        if Zweite_Wahl != Moderator_Wahl and Preise[Zweite_Wahl] != "ziege" and Zahlen_Liste[Zweite_Wahl] != "1" and Zahlen_Liste[Moderator_Wahl] != "1":
            Button_Eins.config(command=Neuer_Versuch, image=Ziege, width = "105", height = "105", bg=Original_Button_Farbe)
        elif Zweite_Wahl != Moderator_Wahl and Preise[Zweite_Wahl] != "ziege" and Zahlen_Liste[Zweite_Wahl] != "2" and Zahlen_Liste[Moderator_Wahl] != "2":
            Button_Zwei.config(command=Neuer_Versuch, image=Ziege, width = "105", height = "105", bg=Original_Button_Farbe)
        elif Zweite_Wahl != Moderator_Wahl and Preise[Zweite_Wahl] != "ziege" and Zahlen_Liste[Zweite_Wahl] != "3" and Zahlen_Liste[Moderator_Wahl] != "3":
            Button_Drei.config(command=Neuer_Versuch, image=Ziege, width = "105", height = "105", bg=Original_Button_Farbe)
        if Zweite_Wahl == 0:
            Button_Eins.config(command=Neuer_Versuch, image=Auto, width = "105", height = "105", bg=Original_Button_Farbe)
            Button_Zwei.config(command=Neuer_Versuch)
            Button_Drei.config(command=Neuer_Versuch)
        elif Zweite_Wahl == 1:
            Button_Eins.config(command=Neuer_Versuch)
            Button_Zwei.config(command=Neuer_Versuch, image=Auto, width = "105", height = "105", bg=Original_Button_Farbe)
            Button_Drei.config(command=Neuer_Versuch)
        elif Zweite_Wahl == 2:
            Button_Eins.config(command=Neuer_Versuch)
            Button_Zwei.config(command=Neuer_Versuch)
            Button_Drei.config(command=Neuer_Versuch, image=Auto, width = "105", height = "105", bg=Original_Button_Farbe)
        if Zweite_Wahl == MeineTuer:
            u = u + 1
        elif Zweite_Wahl != MeineTuer:
            v = v + 1
        Statistik()
    elif Preise[Zweite_Wahl] == "ziege":
        Spiel_Text.config(text="Du hast Verloren")
        b = b + 1
        winsound.PlaySound("C:/Windows/Media/Windows Foreground.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)
        if Zweite_Wahl != Moderator_Wahl and Preise[Zweite_Wahl] != "auto" and Zahlen_Liste[Zweite_Wahl] != "1" and Zahlen_Liste[Moderator_Wahl] != "1":
            Button_Eins.config(command=Neuer_Versuch, image=Auto, width = "105", height = "105", bg=Original_Button_Farbe)
        elif Zweite_Wahl != Moderator_Wahl and Preise[Zweite_Wahl] != "auto" and Zahlen_Liste[Zweite_Wahl] != "2" and Zahlen_Liste[Moderator_Wahl] != "2":
            Button_Zwei.config(command=Neuer_Versuch, image=Auto, width = "105", height = "105", bg=Original_Button_Farbe)
        elif Zweite_Wahl != Moderator_Wahl and Preise[Zweite_Wahl] != "auto" and Zahlen_Liste[Zweite_Wahl] != "3" and Zahlen_Liste[Moderator_Wahl] != "3":
            Button_Drei.config(command=Neuer_Versuch, image=Auto, width = "105", height = "105", bg=Original_Button_Farbe)
        if Zweite_Wahl == 0:
            Button_Eins.config(command=Neuer_Versuch, image=Ziege, width = "105", height = "105", bg=Original_Button_Farbe)
            Button_Zwei.config(command=Neuer_Versuch)
            Button_Drei.config(command=Neuer_Versuch)
        elif Zweite_Wahl == 1:
            Button_Eins.config(command=Neuer_Versuch)
            Button_Zwei.config(command=Neuer_Versuch, image=Ziege, width = "105", height = "105", bg=Original_Button_Farbe)
            Button_Drei.config(command=Neuer_Versuch)
        elif Zweite_Wahl == 2:
            Button_Eins.config(command=Neuer_Versuch)
            Button_Zwei.config(command=Neuer_Versuch)
            Button_Drei.config(command=Neuer_Versuch, image=Ziege, width = "105", height = "105", bg=Original_Button_Farbe)
        if Zweite_Wahl == MeineTuer:
            x = x + 1
        elif Zweite_Wahl != MeineTuer:
            y = y + 1
        Statistik()

def Neuer_Versuch():
    global MeineTuer, Zweite_Wahl
    MeineTuer = 0
    Zweite_Wahl = 0
    Button_Eins.config(text='1', height=105, width=105, command=Wahl_Eins, state=NORMAL, fg='black', bg=Original_Button_Farbe, image=Tuer_1)
    Button_Zwei.config(text='2', height=105, width=105, command=Wahl_Zwei, state=NORMAL, fg='black', bg=Original_Button_Farbe, image=Tuer_2)
    Button_Drei.config(text='3', height=105, width=105, command=Wahl_Drei, state=NORMAL, fg='black', bg=Original_Button_Farbe, image=Tuer_3)
    Spiel_Text.config(text='Wähle eine Türe')
    
def Wahl_Eins():
    global MeineTuer, Preise
    Spiel_Text.config(text="Der Moderator Wählt Jetzt")
    MeineTuer = 0
    MeineTuer = MeineTuer + 1
    Button_Eins.config(fg='white', bg='gray')
    Moderator()

def Wahl_Zwei():
    global MeineTuer, Preise
    Spiel_Text.config(text="Der Moderator Wählt Jetzt")
    MeineTuer = 0
    MeineTuer = MeineTuer + 2
    Button_Zwei.config(fg='white', bg='gray')
    Moderator()

def Wahl_Drei():
    global MeineTuer, Preise
    Spiel_Text.config(text="Der Moderator Wählt Jetzt")
    MeineTuer = 0
    MeineTuer = MeineTuer + 3
    Button_Drei.config(fg='white', bg='gray')
    Moderator()

def Zweite_Wahl_Eins():
    global Zweite_Wahl
    Zweite_Wahl = 0
    Letzte_Runde()
    
def Zweite_Wahl_Zwei():
    global Zweite_Wahl
    Zweite_Wahl = 1
    Letzte_Runde()

def Zweite_Wahl_Drei():
    global Zweite_Wahl
    Zweite_Wahl = 2
    Letzte_Runde()

#Menüleiste Info
def Info_Dialog_Nachricht():
        m_text = """
************************
Autor: Christof
Datum: 05.05.2017
Version: 7.0
************************"""
        messagebox.showinfo(message=m_text, title = "Infos")

def Statistik():
    global a, b, c, u, v, w, x, y, z, Gewonnen_Text, Verloren_Text, Ohne_Wechsel_Text, Mit_Wechsel_Text
    c = a + b
    w = u + x
    z = v + y
    Gewonnen_Text = 'Gewonnen:', a, 'mal'
    Verloren_Text = 'Verloren:', b,'mal'
    Ohne_Wechsel_Text_Gew = 'Gewonnen:', u, 'mal'
    Ohne_Wechsel_Text_Ver = 'Verloren:', x, 'mal'
    Mit_Wechsel_Text_Gew = 'Gewonnen:', v, 'mal'
    Mit_Wechsel_Text_Ver = 'Verloren:', y, 'mal'
    Prozent_Text = int(round(100 / c * a, 0)),'%','Zu', int(round(100 / c * b, 0)),'%'
    if u >= 1 or x >= 1:
        Ohne_Wechsel_Prozent = int(round(100 / w * u, 0)), '%', 'Zu', int(round(100 / w * x, 0)),'%'
        if u >= 0 and x >= 1:
            Statistik_Label_Ohne_Wechsel.config(text=Ohne_Wechsel_Prozent)
        elif u >= 1 and x >= 0:
            Statistik_Label_Ohne_Wechsel.config(text="100% zu 0%")
        else:
            Statistik_Label_Ohne_Wechsel.config(text="0% zu 0%")
        Statistik_Ohne_Wechsel_Gewonnen.config(text=Ohne_Wechsel_Text_Gew, fg="green")
        Statistik_Ohne_Wechsel_Verloren.config(text=Ohne_Wechsel_Text_Ver, fg="red")
    if v >= 1 or y >= 1:
        Mit_Wechsel_Prozent = int(round(100 / z * v, 0)), '%', 'Zu', int(round(100 / z * y, 0)),'%'
        if v >= 0 and y >= 1:
            Statistik_Label_Mit_Wechsel.config(text=Mit_Wechsel_Prozent)
        elif v >= 1 and y >= 0:
            Statistik_Label_Mit_Wechsel.config(text="100% zu 0%")
        else:
            Statistik_Label_Mit_Wechsel.config(text="0% zu 0%")
        Statistik_Mit_Wechsel_Gewonnen.config(text=Mit_Wechsel_Text_Gew, fg="green")
        Statistik_Mit_Wechsel_Verloren.config(text=Mit_Wechsel_Text_Ver, fg="red")
    if a >= 0 and b >= 1:
        Statistik_Main_Gewonnen.config(text=Gewonnen_Text)
        Statistik_Main_Verloren.config(text=Verloren_Text)
        Statistik_Main_Prozent.config(text=Prozent_Text)
    elif a >= 1 and b >= 0:
        Statistik_Main_Gewonnen.config(text=Gewonnen_Text)
        Statistik_Main_Verloren.config(text=Verloren_Text)
        Statistik_Main_Prozent.config(text="100% zu 0%")
    else:
        Statistik_Main_Prozent.config(text="0% zu 0%")

def Reset_Message():
    result = messagebox.askquestion("Reset", "Deine Statistik wird gelöscht\n\nBist du Sicher?", icon='warning')
    if result == 'yes':
        Reset_Commando()

def Reset_Commando():
    global MeineTuer, Zweite_Wahl, a, b, c, u, v, x, y, Gewonnen_Text, Verloren_Text
    a, b, c = 0, 0, 0
    u, v, x, y, = 0, 0, 0, 0
    MeineTuer = 0
    Zweite_Wahl = 0
    Statistik_Main_Gewonnen.config(text='Noch nicht Gewonnen')
    Statistik_Main_Verloren.config(text='Noch nicht Verloren')
    Statistik_Ohne_Wechsel_Gewonnen.config(text='Gewonnen 0 mal')
    Statistik_Ohne_Wechsel_Verloren.config(text='Verloren 0 mal')
    Statistik_Mit_Wechsel_Gewonnen.config(text='Gewonnen 0 mal')
    Statistik_Mit_Wechsel_Verloren.config(text='Verloren 0 mal')
    Statistik_Main_Prozent.config(text="0% zu 0%")
    Statistik_Label_Ohne_Wechsel.config(text="0% zu 0%")
    Statistik_Label_Mit_Wechsel.config(text="0% zu 0%")
    Button_Eins.config(text='1', height=105, width=105, command=Wahl_Eins, state=NORMAL, fg='black', bg=Original_Button_Farbe, image=Tuer_1)
    Button_Zwei.config(text='2', height=105, width=105, command=Wahl_Zwei, state=NORMAL, fg='black', bg=Original_Button_Farbe, image=Tuer_2)
    Button_Drei.config(text='3', height=105, width=105, command=Wahl_Drei, state=NORMAL, fg='black', bg=Original_Button_Farbe, image=Tuer_3)
    Spiel_Text.config(text='Wähle eine Türe')        

def Steuerung():
    Steuerungs_Nachricht = """
************************
Steuern kann man das Spiel
mit der Maus!
************************"""
    messagebox.showinfo(message=Steuerungs_Nachricht, title="Steuerung")

def Anleitung():
    Anleitung_Nachricht = """
Sie Wählen als erstes
eine der Türen aus.
Als nächstes öffnet
der Moderator eine Tür
mit eine Ziege drinnenn
Jetzt können sie entscheiden
ob Sie Ihre Türe behalten
oder sie wechseln um das Auto
zu gewinnen."""
    messagebox.showinfo(message=Anleitung_Nachricht, title="Anleitung")

def Hide_Statistik():
    if Zeige_Statistik.get() == 1:
        pass
#        Statistik_Main_Titel.grid_remove()
#        Statistik_Main_Gesamt_Titel.grid_remove()
#        Statistik_Main_Gewonnen.grid_remove()
#        Statistik_Main_Verloren.grid_remove()
#        Statistik_Main_Prozent.grid_remove()
#        Statistik_Titel_Prozenz.grid_remove()
#        Statistik_Main_Info.grid_remove()
#        Statistik_Titel_Ohne_Wechsel.grid_remove()
#        Statistik_Label_Ohne_Wechsel.grid_remove()
#        Statistik_Ohne_Wechsel_Gewonnen.grid_remove()
#        Statistik_Ohne_Wechsel_Verloren.grid_remove()
#        Statistik_Titel_Mit_Wechsel.grid_remove()
#        Statistik_Label_Mit_Wechsel.grid_remove()
#        Statistik_Mit_Wechsel_Gewonnen.grid_remove()
#        Statistik_Mit_Wechsel_Verloren.grid_remove()
#        Abstand_Label_3.grid_remove()
    elif Zeige_Statistik.get() == 0:
        pass
#        Statistik_Main_Titel.grid(row=6, column=2)
#        Statistik_Main_Gesamt_Titel.grid(row=7, column=2)
#        Statistik_Main_Gewonnen.grid(row=8, column=2)
#        Statistik_Main_Verloren.grid(row=9, column=2)
#        Statistik_Titel_Ohne_Wechsel.grid(row=7, column=1)
#        Statistik_Ohne_Wechsel_Gewonnen.grid(row=8, column=1)
#        Statistik_Ohne_Wechsel_Verloren.grid(row=9, column=1)
#        Statistik_Titel_Mit_Wechsel.grid(row=7, column=3)
#        Statistik_Mit_Wechsel_Gewonnen.grid(row=8, column=3)
#        Statistik_Mit_Wechsel_Verloren.grid(row=9, column=3)
#        Abstand_Label_3.grid(row=10, column=2)
#        Statistik_Titel_Prozenz.grid(row=11, column=2)
#        Statistik_Main_Prozent.grid(row=12, column=2)
#        Statistik_Main_Info.grid(row=13, column=2)
#        Statistik_Label_Ohne_Wechsel.grid(row=12, column=1)
#        Statistik_Label_Mit_Wechsel.grid(row=12, column=3)

def rcpath(rel_path):
    return os.path.join(os.getcwd(), rel_path)

fenster = tk.Tk() #Fenster
fenster.title("Ziegenproblem") #Fenstertitel
fenster.resizable(0,0) #Nicht Vergröss- kleinerbar
fenster.iconbitmap(rcpath('Bilder/Favicon.ico'))
#fenster.iconbitmap(r'C:\Users\chgm\LocalData\Projekte\python\Aufgabe 3.1 Ziegenproblem tkinter\Bilder\Favicon.ico')
fenster.configure(background='white')

#Bilder
#Tuer_1 = tk.PhotoImage(file=r"C:\Users\chgm\LocalData\python\Aufgabe 3.1 Ziegenproblem tkinter\Bilder\Door1.gif")
#Tuer_2 = tk.PhotoImage(file=r"C:\Users\chgm\LocalData\python\Aufgabe 3.1 Ziegenproblem tkinter\Bilder\Door2.gif")
#Tuer_3 = tk.PhotoImage(file=r"C:\Users\chgm\LocalData\python\Aufgabe 3.1 Ziegenproblem tkinter\Bilder\Door3.gif")
#Ziege = tk.PhotoImage(file=r"C:\Users\chgm\LocalData\python\Aufgabe 3.1 Ziegenproblem tkinter\Bilder\Ziege.gif")
#Auto = tk.PhotoImage(file=r"C:\Users\chgm\LocalData\python\Aufgabe 3.1 Ziegenproblem tkinter\Bilder\Auto.gif")

script_dir = os.path.dirname(__file__)
rel_path = "Bilder/"
abs_file_path = os.path.join(script_dir, rel_path)

#path = r"C:\\Users\\chgm\\LocalData\\Projekte\\python\\Aufgabe 3.1 Ziegenproblem tkinter\\Bilder\\"
Tuer_1, Tuer_2, Tuer_3, Ziege, Auto = [tk.PhotoImage(file=abs_file_path + file) for file in ["Door1.gif", "Door2.gif", "Door3.gif", "Ziege.gif", "Auto.gif"]]

#Widgets
Titel_Label = tk.Label(fenster,font=("Calibri", 20,'bold'), background='white', text='Ziegenproblem', fg='green', height=3, width=20)
Spiel_Text = tk.Label(fenster,font=("Calibri", 14), background='white', text='Wähle eine Türe', height=1, width=25)
Button_Eins = tk.Button(fenster,font=("Calibri", 14), text='1', height="105", width="105", command=Wahl_Eins, image=Tuer_1,bg="white", highlightthickness = 0, bd = 0, activebackground="white")
Button_Zwei = tk.Button(fenster,font=("Calibri", 14), text='2', height=105, width=105, command=Wahl_Zwei, image=Tuer_2,bg="white", highlightthickness = 0, bd = 0, activebackground="white")
Button_Drei = tk.Button(fenster,font=("Calibri", 14), text='3', height=105, width=105, command=Wahl_Drei, image=Tuer_3,bg="white", highlightthickness = 0, bd = 0, activebackground="white")
Abstand_Label = tk.Label(fenster, background='white', text='', height=1)
Neuer_Versuch_Button = tk.Button(fenster, background="#879F38", activebackground="#6e822d",activeforeground="white", font=("Calibri", 14), 
    foreground="white", text='Neuer Versuch?', height=1, width=20, command=Neuer_Versuch)
Abstand_Label_2 = tk.Label(fenster, background='white', text='', height=1)
#Statistiken
Statistik_Main_Titel= tk.Label(fenster,font=("Calibri", 20, 'bold'), background='white', text='Statistik', fg='#879F38')
Statistik_Main_Gesamt_Titel = tk.Label(fenster,font=("Calibri", 16, 'bold'), background='white', text='Gesamt', fg='#879F38')
Statistik_Main_Gewonnen = tk.Label(fenster,font=("Calibri", 14), background='white', text='Noch nicht Gewonnen', fg='green')
Statistik_Main_Verloren = tk.Label(fenster,font=("Calibri", 14), background='white', text='Noch nicht Verloren', fg='red')
Statistik_Main_Prozent = tk.Label(fenster,font=("Calibri", 14), background='white', text='0% zu 0%')
Statistik_Titel_Prozenz = tk.Label(fenster,font=("Calibri", 18, 'bold'), background='white', text='In Prozent', fg='#879F38')
Statistik_Main_Info = tk.Label(fenster,font=("Calibri", 14), background='white', text='Gewonnen / Verloren')
Statistik_Titel_Ohne_Wechsel = tk.Label(fenster,font=("Calibri", 16, 'bold'), background='white', fg='#879F38', text='Ohne Wechsel')
Statistik_Label_Ohne_Wechsel = tk.Label(fenster,font=("Calibri", 14), background='white', text='0% zu 0%')
Statistik_Ohne_Wechsel_Gewonnen = tk.Label(fenster,font=("Calibri", 14), background='white', text='Gewonnen 0 mal', fg="green")
Statistik_Ohne_Wechsel_Verloren = tk.Label(fenster,font=("Calibri", 14), background='white', text='Verloren 0 mal', fg="red")
Statistik_Titel_Mit_Wechsel = tk.Label(fenster,font=("Calibri", 16, 'bold'), background='white', fg='#879F38', text='Mit Wechsel')
Statistik_Label_Mit_Wechsel = tk.Label(fenster,font=("Calibri", 14), background='white', text='0% zu 0%')
Statistik_Mit_Wechsel_Gewonnen = tk.Label(fenster,font=("Calibri", 14), background='white', text='Gewonnen 0 mal', fg="green")
Statistik_Mit_Wechsel_Verloren = tk.Label(fenster,font=("Calibri", 14), background='white', text='Verloren 0 mal', fg='red')
Abstand_Label_3 = tk.Label(fenster, background='white', text='', height=1)

Original_Button_Farbe = Button_Eins.cget("background")

Zeige_Statistik = IntVar()

#Menüleiste
Menu_Leiste = Menu(fenster)
Spiel_Menu = Menu(Menu_Leiste, tearoff = 0)
Einstellung_Menu = Menu(Menu_Leiste, tearoff = 0)
Hilfe_Menu = Menu(Menu_Leiste, tearoff = 0)
#Menüs
Spiel_Menu.add_command(label="Neu",font=("Calibri", 14), command=Neuer_Versuch)
Spiel_Menu.add_command(label="Reset",font=("Calibri", 14), command=Reset_Message)#lambda: messagebox.showinfo(message="in bearbeitung", title = "Reset"))
Spiel_Menu.add_separator()#Trennlinie
Spiel_Menu.add_command(label="Exit",font=("Calibri", 14), command=fenster.quit)

Hilfe_Menu.add_command(label="Info",font=("Calibri", 14), command=Info_Dialog_Nachricht)
Hilfe_Menu.add_command(label="Anleitung",font=("Calibri", 14), command=Anleitung)
Hilfe_Menu.add_separator()
Hilfe_Menu.add_command(label="Steuerung",font=("Calibri", 14), command=Steuerung)

Einstellung_Menu.add_checkbutton(label="Hide Stats", font=("Calibri", 14), command=Hide_Statistik, variable=Zeige_Statistik, onvalue=1, offvalue=0)

#Dropdownmenü
Menu_Leiste.add_cascade(label="Spiel", menu=Spiel_Menu)
Menu_Leiste.add_cascade(label="Einstellungen", menu=Einstellung_Menu)
Menu_Leiste.add_cascade(label="Hilfe", menu=Hilfe_Menu)
fenster.config(menu=Menu_Leiste)

#Zuordung und Standort
Titel_Label.grid(row=0, column=2)
Spiel_Text.grid(row=1, column=2)
#Türen und Reset knopf
Button_Eins.grid(row=2, column=1, padx=20)
Button_Zwei.grid(row=2, column=2)
Button_Drei.grid(row=2, column=3, padx=20)
Abstand_Label.grid(row=3, column=2)
Neuer_Versuch_Button.grid(row=4, column=2)
Abstand_Label_2.grid(row=5, column=2)
#Statistik
Statistik_Main_Titel.grid(row=6, column=2)
Statistik_Main_Gesamt_Titel.grid(row=7, column=2)
Statistik_Main_Gewonnen.grid(row=8, column=2)
Statistik_Main_Verloren.grid(row=9, column=2)
Statistik_Titel_Ohne_Wechsel.grid(row=7, column=1)
Statistik_Ohne_Wechsel_Gewonnen.grid(row=8, column=1)
Statistik_Ohne_Wechsel_Verloren.grid(row=9, column=1)
Statistik_Titel_Mit_Wechsel.grid(row=7, column=3)
Statistik_Mit_Wechsel_Gewonnen.grid(row=8, column=3)
Statistik_Mit_Wechsel_Verloren.grid(row=9, column=3)
Abstand_Label_3.grid(row=10, column=2)
#Statistik Prozent
Statistik_Titel_Prozenz.grid(row=11, column=2)
Statistik_Main_Prozent.grid(row=12, column=2)
Statistik_Main_Info.grid(row=13, column=2)
Statistik_Label_Ohne_Wechsel.grid(row=12, column=1)
Statistik_Label_Mit_Wechsel.grid(row=12, column=3)

fenster.mainloop()
 
