import random, time, winsound, os
a, b, c, d = 0, 0, 0, 0
print("╔═══════════════╗\n║ Ziegenproblem ║\n╚═══════════════╝")

def stats():
	#a = 1 lose // b = 1 win // def unten
	print("\n", c, "Mal Gewonnnen", d, "mal verloren")
	a = c + d
	if c >= 0 and d >= 1:
		print("\n", 100 / a * c,"Prozent Gewonnen", 100 / a * d,"Prozent Verloren\n")
	elif c >= 1 and d >= 0:
		print("\n", 100 / a * c,"Prozent Gewonnen", 100 / a * d,"Prozent Verloren\n")
	else:
		print("\n 0 Prozent Gewonnen 0 Prozent Verloren\n")	

while True:
	try:
		preise = ["ziege", "ziege", "auto"]
		random.shuffle(preise)
		
		print("Hinter einer der drei Türen ist ein Auto in den anderen Ziegen. Viel Glück!")
		print("┌───┐   ┌───┐   ┌───┐\n│ 1 │   │ 2 │   │ 3 │\n│  *│   │  *│   │  *│\n│ ? │   │ ? │   │ ? │\n└───┘   └───┘   └───┘")
		meinetür = input("Welche Tür? ") #input("Welche Tür? ") für hilfe / int(input("Welche Tür? "))
		
		if(meinetür.lower() == "hilfe") or (meinetür.lower() == "help"):
			print("\n╔═══════════════════════════════════╗\n║              Befehle              ║\n║ Hilfe für diese Seite             ║\n║ Zahlen 1,2,3 für die Türen        ║\n║ Clear um das fenster zu löschen   ║\n║ Stats für die Spiel Statistik     ║\n║ Restart um das Spiel Neuzustarten ║\n╚═══════════════════════════════════╝\n")
		elif(meinetür.lower() == "clear") or (meinetür.lower() == "c"):
			os.system('cls')
			print("╔═══════════════╗\n║ Ziegenproblem ║\n╚═══════════════╝")
		elif(meinetür == "") or (meinetür == " "):
			print("\nBitte Zahlen von 1-3 oder Hilfe eingeben\n")
		elif meinetür == "1" or meinetür == "2" or meinetür == "3":
			meinetür = int(meinetür)
			meinetür = meinetür - 1
			while True:
				moderator = random.randrange(3)
				if preise[moderator] != "auto" and moderator != meinetür:
					break
			print("╔══════════════════════════════╗\n║ Hinter Tür",moderator + 1,"ist eine Ziege. ║\n╚══════════════════════════════╝\n")
			while True:
				try:
					if moderator == 0:
						print("╔═══╗   ┌───┐   ┌───┐\n║ 1 ║   │ 2 │   │ 3 │\n║  *║   │  *│   │  *│\n║ Z ║   │   │   │   │\n╚═══╝   └───┘   └───┘\n")
					elif moderator == 1:					
						print("┌───┐   ╔═══╗   ┌───┐\n│ 1 │   ║ 2 ║   │ 3 │\n│  *│   ║  *║   │  *│\n│   │   ║ Z ║   │   │\n└───┘   ╚═══╝   └───┘\n")
					elif moderator == 2:					
						print("┌───┐   ┌───┐   ╔═══╗\n│ 1 │   │ 2 │   ║ 3 ║\n│  *│   │  *│   ║  *║\n│   │   │   │   ║ Z ║\n└───┘   └───┘   ╚═══╝\n")
					wahl2 = int(input("Türe Wechseln oder Behalten? "))
					wahl2 = wahl2 - 1

					if preise[wahl2] == "auto" and wahl2 != moderator:
						print("\nDu hast das Auto gewonnen")
						print("\n      ____________\n ____//__][__\\\___\ \n(o _ |  -|   _   o|\n `(_)-------(_)---'\n")
						#print("  ______\n /|_||_\`.__\n(   _    _ _\ \n=`-(_)--(_)-'\n")
						c = c + 1
						winsound.PlaySound("C:/Windows/Media/tada.wav", winsound.SND_FILENAME)
						break
					elif preise[wahl2] == "ziege" and wahl2 != moderator:
						print("\nDu bekommst eine Ziege")
						print("(_(\n/_/'_____/)\n\"  |      |\n   |\"\"\"\"\"\"|\n")
						d = d + 1
						winsound.PlaySound("C:/Windows/Media/Windows Foreground.wav", winsound.SND_FILENAME)
						break
					elif wahl2 == moderator:
						print("\nDiese türe ist bereits offen\n")
					else:
						print("\nnur zahlen von 1-3 (1,2,3)\n")
				except IndexError:
					print("\nnur zahlen von 1-3 (1,2,3)\n")
				except ValueError:
					print("\nNur Zahlen\n")
		elif(meinetür.lower() == "stats") or (meinetür.lower() == "statistik"):
			stats()
		elif(meinetür.lower() == "restart"):
			print("\nBeim Restart werden deine Statistiken Gelöscht\n")
			sicher = input("\nBist du dir sicher ? (ja/nein): ")
			if(sicher.lower() == "ja") or (sicher.lower() == "yes") or (sicher.lower() == "j") or (sicher.lower() == "y"):
				os.system('cls')
				a, b, c, d = 0, 0, 0, 0
				print("╔═══════════════╗\n║ Ziegenproblem ║\n╚═══════════════╝")
			elif(sicher.lower() == "nein") or (sicher.lower() == "no") or (sicher.lower() == "n"):
				print("\nok kehre Zurück\n")
			else:
				print("\nNichts oder was falsches eingegeben.\nKehrt zurück\n")
		elif(meinetür.lower() == "exit"):
			print("\nTschüss")
			time.sleep(1)
			exit()
		else:
			print("\nnur zahlen von 1-3 (1,2,3), oder hilfe eingeben\n")
	except ValueError:
		print("\nDu hast was falsches eingegeben. Hilfe für hilfe\n")
	except NameError:
		print("\nDu hast was falsches eingegeben. Hilfe für hilfe\n")