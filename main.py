from hillclimber import hillclimber
import greedy
from random_walk import random_walk
from random_walk import visualisatie_random_walk


if __name__ == '__main__':

    antwoord = input("Wil je werken met greedy of hillclimber of random_walk:  ")
    if antwoord not in ["greedy", "hillclimber", "random_walk"]:
        print("Beantwoord vraag met greedy of hillclimber of random_walk")
    elif antwoord == "greedy":
        greedy.greedy()
        print(f"Totale wijk waarde is: {int(amstel.totale_nieuwe_huiswaarde())} euro")
        # amstel.visualisatie()
    elif antwoord == "random_walk":
        amstel = random_walk()
        visualisatie_random_walk(amstel)
    else:
        hillclimber()

    #huis = amster.huizen_lijst[0]
    #huis.linksboven = (0, 160)
    #huis.rechtsboven =
