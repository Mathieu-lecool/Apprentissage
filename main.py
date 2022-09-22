#trinket.io/sense-hat
from sense_hat import SenseHat

sense = SenseHat()

blue_color = (27, 172, 241)
orange_color = (241, 69, 27)
red_color = (255, 0, 0)

sense.show_message("Bonjour", text_colour=blue_color)

while True:
    temperature = int(sense.get_temperature())

    if temperature < 25:
        matrice_color = [blue_color] * 64
    elif temperature >= 25 and temperature < 30:
        matrice_color = [orange_color] * 64
    else:
        matrice_color = [red_color] * 64

    sense.set_pixels(matrice_color)
