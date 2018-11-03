import sys
def test():
	print("Hela listan:")
	print(sys.argv)
	print("")
	print("Bara forsta elementet:")
	print(sys.argv[0])
	input("Tryck Enter: ")
	s = input("Skriv nagot: ")
	print("Varfor skrev du '" + s + "'?")

test()