class GameError(Exception):
	def __init__(self, code = 000):
		self.errorMessage = None

		self.errorDict = {
			000 : "Greška 000 : Nespecificirana greška",
			101 : "Greška 101 : Unijeli ste krivu vrijednost"
		}

		try:
			self.errorMessage = self.errorDict[code]
		except KeyError:
			self.errorMessage = self.errorDict[000]

		print("\n")
		print("=" * 75)
		print(self.errorMessage)
		print("=" * 75)
		print("\n")