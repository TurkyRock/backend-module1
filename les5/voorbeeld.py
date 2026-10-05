
import math
import time
print("Voorbeelden van if-statements")

leeftijd = 16

# Een eenvoudige if: de code wordt alleen uitgevoerd als de voorwaarde waar is.
if leeftijd >= 18:
	print("Je bent volwassen.")

# Met else kies je wat er gebeurt als de voorwaarde niet waar is.
if leeftijd >= 18:
	print("Je mag stemmen.")
else:
	print("Je bent nog geen 18.")

# Met elif controleer je meerdere mogelijkheden.
cijfer = 7

if cijfer >= 8:
	print("Goed gedaan!")
elif cijfer >= 6:
	print("Je hebt een voldoende.")
else:
	print("Je hebt een onvoldoende.")

# Je kunt voorwaarden combineren met and en or.
heeft_kaartje = True
is_uitverkocht = False

if heeft_kaartje and not is_uitverkocht:
	print("Je mag naar binnen.")
else:
	print("Je mag niet naar binnen.")


print("\nVoorbeelden van functies")

# Een functie zonder parameters.
def zeg_hallo():
	print("Hallo!")


# Een functie met een parameter.
def begroet(naam):
	print("Hallo", naam)


# Een functie die een waarde teruggeeft met return.
def tel_op(getal1, getal2):
	return getal1 + getal2


# Een functie kan ook een if-statement bevatten.
def controleer_leeftijd(leeftijd):
	if leeftijd >= 18:
		return "volwassen"
	else:
		return "minderjarig"


# Functies voer je uit door ze aan te roepen.
zeg_hallo()
begroet("Sam")
som = tel_op(4, 5)
print("4 + 5 =", som)
print("Je bent", controleer_leeftijd(leeftijd))
