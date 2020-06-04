class RPS_Error(Exception):
    def __init__(self, code = 000):
        self.errorMessage = "~" * 50 + "\n"

        self.errorDict = {
            000 : "Error 000 : Unspecified error",
            101 : "Error 101 : One of the players entered the wrong value"
        }

        try:
            self.errorMessage += self.errorDict[code]
        except KeyError:
            self.errorMessage += self.errorDict[000]

        print(self.errorMessage + "\n" + "~" * 50 + "\n")