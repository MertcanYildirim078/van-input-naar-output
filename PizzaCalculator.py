print("- - - - - - - - - - - - - - - - - - - - - ")
print("pizza small         $6")
print("pizza medium        $9")   #Mertcan Yildirim Pizza calculator
print("pizza large         $12")
print("- - - - - - - - - - - - - - - - - - - - - ")


pizza = input("Welke grootte pizza wil je? ")
aantal = int(input("Hoeveel wil je? "))
if pizza == "small":
    berekening = 6 * aantal
    print("Dat word dan " + str(berekening) + "$")

elif pizza == "medium":
    berekening = 9 * aantal
    print("Dat word dan " + str(berekening) + "$")

elif pizza == "large":
    berekening = 12 * aantal
    print("Dat word dan " + str(berekening) + "$")
#if is wanneer je als een actie worden uitgevoerd wanneer er een getal correct bij past
#elif is als de if niet geldig is
