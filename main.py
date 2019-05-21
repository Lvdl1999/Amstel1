from hillclimber import hillclimber
from rand_hillclimber import rand_hillclimber
from random_walk import random_walk
from random_walk import visualisatie_random_walk
from annealing import annealing, linear_afkoeling, log_afkoeling
from amstel import Amstel
from plattegrond import Plattegrond


if __name__ == '__main__':
    """
    De 'main' functie ontvangt input van de gebruiker met betrekking tot welke algoritmes
    zullen worden gebruikt.
    """

    print("\nWelcome to AmstelHaege!\n")
    print("______________________________________________________________ \n")
    amstel = Amstel()
    print("______________________________________________________________")
    plattegrond = Plattegrond(160, 180)
    amstel.plaats_huizen(plattegrond)

while True:
    antwoord = input("\nWerken met random_hillclimber, hillclimber, random_walk of annealing?:  ")
    print("______________________________________________________________ \n")
    if antwoord not in ["random_hillclimber", "hillclimber", "random_walk", "annealing"]:
        print("Beantwoord vraag met: random_hillclimber, hillclimber, random_walk of annealing")
        # amstel.visualisatie()
    elif antwoord == "random_hillclimber":
        rand_hillclimber(amstel, plattegrond)
        visualisatie_rand_hillclimber(amstel)
        break
    elif antwoord == "random_walk":
        random_walk(amstel, plattegrond)
        visualisatie_random_walk(amstel)
        break
    elif antwoord == "annealing":
        soort_afkoeling = input("Welk koelsysteem wilt u gebruiken: linear_afkoeling, log_afkoeling of exp_afkoeling?:  ")
        print("______________________________________________________________ \n")
        if soort_afkoeling not in ["linear_afkoeling", "log_afkoeling", "exp_afkoeling"]:
            print("Beantwoord vraag met: linear_afkoeling, log_afkoeling of exp_afkoeling")
        elif soort_afkoeling == "linear_afkoeling":
            for i in range(5):
                annealing(amstel, plattegrond, linear_afkoeling, 1000000)
                hillclimber(amstel, plattegrond)
            visualisatie_annealing(amstel)
            break
            # amstel = annealing(linear_afkoeling, 1000000)
        elif soort_afkoeling == "log_afkoeling":
            for i in range(5):
                annealing(amstel, plattegrond, log_afkoeling, 1000000)
                hillclimber(amstel, plattegrond)
            visualisatie_annealing(amstel)
            break
            # amstel = annealing(log_afkoeling, 1000000)
        elif soort_afkoeling == "exp_afkoeling":
            for i in range(5):
                annealing(amstel, plattegrond, exp_afkoeling, 1000000)
                hillclimber(amstel, plattegrond)
            visualisatie_annealing(amstel)
            break
            # amstel = annealing(exp_afkoeling, 1000000)
    else:
        hillclimber(amstel, plattegrond)
        break
