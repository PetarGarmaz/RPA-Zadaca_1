from Missile import Missile
import random

class Warship(Missile):
	def __init__(self, x = 0, y = 0, route = 0):
		super().__init__(x, y)
		self.route = route

	def ShowTitleCard(self):
		print(" ~~~~~~~~~~~~~~~~~~~~~")
		print(" ~~~ Borba brodova ~~~")
		print(" ~~~~~~~~~~~~~~~~~~~~~")
	
	def Fight(self):
		shipNum = int(input("Unesite broj brodova na ratnom polju: "))

		ships = []
		missiles = []

		for x in range(0, shipNum):
			x = random.randint(0, 100)
			y = random.randint(1, 100)

			self.route = random.randint(0, 10)

			ships.append(Warship(x, y, self.route))

		for x in range(0, shipNum):
			x = random.randint(0, 100)
			y = random.randint(1, 100)

			missiles.append(Missile(x, y))

		for index, ship in enumerate(ships):
			print("Brod #{} je napravio {} ruta.".format(index + 1, ship.route))

		print("\n")

		yourShip = int(input("Od {} brodova, Vaš brod je pod brojem: ".format(shipNum)))

		chosenShip = ships[yourShip-1]

		for index, ship in enumerate(ships):
			distance = chosenShip.GetDistance(ship)
			print("Vaš brod je udaljen {} kilomenara od broda broj {}.".format(distance, index + 1))

		print("\n")

		for index, missile in enumerate(missiles):
			distance = chosenShip.GetDistance(missile)
			print("Vaš tenk je udaljen {} kilomenara od projektila broj {}.".format(distance, index + 1))