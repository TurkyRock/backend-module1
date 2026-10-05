games = ["Minecraft", "Fortnite", "FIFA", "Mario Kart", "The Sims"]

# 1. De hele lijst in een keer afdrukken
print(games)

# 2. Games los afdrukken met hun plaats in de lijst
print(games[0])
print(games[1])
print(games[2])
print(games[3])
print(games[4])

# 3. Elke game afdrukken met een for-loop
for game in games:
	print(game)

# 4. Elke game afdrukken met een nummer
for nummer, game in enumerate(games, start=1):
	print(nummer, game)

# 5. Een game toevoegen
games.append("Rocket League")
print(games)

# 6. Alleen de eerste drie games afdrukken
print(games[:3])
