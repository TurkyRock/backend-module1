"""Workshop 2 - Game Character Generator.

Een eenvoudig oefenprogramma met input, variabelen, berekeningen en print().
"""


def vraag_getal(vraag):
    """Blijf vragen totdat de speler een positief geheel getal invoert."""
    while True:
        try:
            getal = int(input(vraag))
            if getal >= 0:
                return getal
            print("Voer een getal van 0 of hoger in.")
        except ValueError:
            print("Dat is geen geldig geheel getal. Probeer het opnieuw.")


print("=" * 46)
print("        GAME CHARACTER GENERATOR")
print("=" * 46)

# 1. GEGEVENS: de speler vult de variabelen in.
naam = input("Hoe heet jouw character? ").strip() or "Naamloze held"
soort = input("Wat is het (ridder, tovenaar, ninja...)? ").strip() or "avonturier"
speciale_kracht = input("Wat is de speciale kracht? ").strip() or "supersnel denken"
level = vraag_getal("Welk level heeft het character? ")
levens = vraag_getal("Hoeveel levens heeft het character? ")
kracht = vraag_getal("Hoeveel krachtpunten heeft het character? ")
bonus = vraag_getal("Hoeveel bonuspunten krijgt het character? ")
schade = vraag_getal("Hoeveel schade heeft het character opgelopen? ")

# 2. REKENEN: met de ingevoerde variabelen worden nieuwe waarden berekend.
totale_kracht = kracht + bonus + level
levens_over = max(0, levens - schade)
score = level * 100 + totale_kracht * 10 + levens_over

# 3. TOON: een nette character-pagina met alle gegevens en uitkomsten.
print("\n" + "=" * 46)
print(f"           CHARACTER: {naam.upper()}")
print("=" * 46)
print(f"Soort              : {soort}")
print(f"Level              : {level}")
print(f"Speciale kracht    : {speciale_kracht}")
print("-" * 46)
print(f"Levens bij start   : {levens}")
print(f"Opgelopen schade   : {schade}")
print(f"Levens over        : {levens_over}")
print(f"Basiskracht        : {kracht}")
print(f"Bonus              : {bonus}")
print(f"Totale kracht      : {totale_kracht}")
print(f"Game-score         : {score}")
print("=" * 46)

if levens_over == 0:
    print(f"{naam} moet herstellen voor het volgende gevecht!")
else:
    print(f"{naam} de {soort} is klaar voor het avontuur!")
