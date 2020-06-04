class ContinueError(Exception):
    def __init__(self):
        self.error_message = "Kod 201: Unesena vrijednost je kriva, vrijednost mora biti d ili n."
        print("\n Opis greške: {}".format(self.error_message))