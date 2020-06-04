from Tank import Tank
from Warship import Warship
from GameError import GameError
import random

class Game():
	def ShowTitleCard(self):
		print(" ~~~~~~~~~~~~~~~~~~~~~")
		print(" ~~~~~~ Wargame ~~~~~~")
		print(" ~~~~~~~~~~~~~~~~~~~~~")

	def ShowUserMenu(self):
		print("\n[1] Pokreni borbu tenkova")
		print("[2] Pokreni borbu brodova")
		print("[x] Izlaz\n")

		return input("Odaberite što želite napraviti: ")

	def Play(self):
		choice = ""

		self.ShowTitleCard()
		
		while(choice != "x"):
			choice = self.ShowUserMenu()

			if(choice == "1"):
				Tank().ShowTitleCard()
				Tank().Fight()
			elif(choice == "2"):
				Warship().ShowTitleCard()
				Warship().Fight()
			elif(choice == "x"):
				print("\nDoviđenja!")
			else:
				raise GameError(101)
		
if __name__ == "__main__":
	Game().Play()