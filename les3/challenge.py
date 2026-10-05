games = [
    "Minecraft",
    "Fortnite",
    "Rocket League",
    "Mario Kart",
    "The Legend of Zelda",
    "Pokémon",
    "Roblox",
    "Stardew Valley"
]

print("Welkom bij de gamebibliotheek!")

while True:
    print("\nWat wil je doen?")
    print("1. Alle games bekijken")
    print("2. Eén game via het nummer bekijken")
    print("3. Een game aanpassen")
    print("4. Een game toevoegen")
    print("5. Een game verwijderen")
    print("6. Games alfabetisch sorteren")
    print("7. Volgorde omdraaien")
    print("8. Stoppen")

    keuze = input("Maak een keuze (1 t/m 8): ")

    if keuze == "1":
        print("\nDit zijn de games:")
        for index in range(len(games)):
            print(index, "-", games[index])

    elif keuze == "2":
        nummer = int(input("Welk indexnummer wil je bekijken? "))
        print("Op deze plek staat:", games[nummer])

    elif keuze == "3":
        nummer = int(input("Welk indexnummer wil je aanpassen? "))
        nieuwe_game = input("Wat is de nieuwe naam? ")
        games[nummer] = nieuwe_game
        print("De aangepaste lijst is:", games)

    elif keuze == "4":
        nieuwe_game = input("Welke game wil je toevoegen? ")
        games.append(nieuwe_game)
        print("De game is toegevoegd:", games)

    elif keuze == "5":
        nummer = int(input("Welk indexnummer wil je verwijderen? "))
        verwijderde_game = games.pop(nummer)
        print(verwijderde_game, "is verwijderd.")
        print("De nieuwe lijst is:", games)

    elif keuze == "6":
        games.sort()
        print("De lijst is alfabetisch gesorteerd:", games)

    elif keuze == "7":
        games.reverse()
        print("De volgorde is omgedraaid:", games)

    elif keuze == "8":
        print("Bedankt voor het gebruiken van de gamebibliotheek!")
        break

    else:
        print("Deze keuze bestaat niet. Kies een getal van 1 t/m 8.")
