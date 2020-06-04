from Missile import Missile
import random

class Tank(Missile):
	def __init__(self, x = 0, y = 0, route = 0):
		super().__init__(x, y)
		self.route = route

	def ShowTitleCard(self):
		print(" ~~~~~~~~~~~~~~~~~~~~~")
		print(" ~~~ Borba Tenkova ~~~")
		print(" ~~~~~~~~~~~~~~~~~~~~~")
	
	def Fight(self):
		tankNum = int(input("Unesite broj tenkova na ratnom polju: "))

		tanks = []
		missiles = []

		for x in range(0, tankNum):
			x = random.randint(0, 100)
			y = random.randint(1, 100)

			self.route = random.randint(0, 10)

			tanks.append(Tank(x, y, self.route))

		for x in range(0, tankNum):
			x = random.randint(0, 100)
			y = random.randint(1, 100)

			missiles.append(Missile(x, y))

		for index, tank in enumerate(tanks):
			print("Tenk #{} je napravio {} ruta.".format(index + 1, tank.route))

		print("\n")

		yourTank = int(input("Od {} tenkova, Vaš tenk je pod brojem: ".format(tankNum)))

		chosenTank = tanks[yourTank-1]

		for index, tank in enumerate(tanks):
			distance = chosenTank.GetDistance(tank)
			print("Vaš tenk je udaljen {} kilomenara od tenka broj {}.".format(distance, index + 1))

		print("\n")

		for index, missile in enumerate(missiles):
			distance = chosenTank.GetDistance(missile)
			print("Vaš tenk je udaljen {} kilomenara od projektila broj {}.".format(distance, index + 1))
