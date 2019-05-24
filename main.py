from Code.schuif_hillclimber import schuif_hillclimber, visualisatie_schuif_hillclimber
from Code.verplaats_hillclimber import verplaats_hillclimber, visualisatie_verplaats_hillclimber
from Code.random_walk import random_walk
from Code.random_walk import visualisatie_random_walk
from Code.annealing import visualisatie_annealing, annealing, lineair_afkoeling, log_afkoeling, exp_afkoeling
from Code.amstel import Amstel
from Code.plattegrond import Plattegrond
import csv
import statistics



if __name__ == '__main__':
    """
    De 'main' functie ontvangt input van de gebruiker met betrekking tot welke algoritmes
    zullen worden gebruikt.
    """

    print("\nWelkom, dit is AmstelHaege!\n")
    print("______________________________________________________________ \n")
    amstel = Amstel()
    print("______________________________________________________________")
    plattegrond = Plattegrond(160, 180)
    amstel.plaats_huizen(plattegrond)

while True:
    if amstel.aantal_huizen <= 40:
        antwoord = input("\nWerken met verplaats_hillclimber, schuif_hillclimber, random_walk of annealing?:  ")
        print("______________________________________________________________ \n")
        if antwoord not in ["verplaats_hillclimber", "schuif_hillclimber", "random_walk", "annealing"]:
            print("Beantwoord vraag met: verplaats_hillclimber, schuif_hillclimber, random_walk of annealing")
            # amstel.visualisatie()
        elif antwoord == "verplaats_hillclimber":
            verplaats_hillclimber(amstel, plattegrond)
            visualisatie_verplaats_hillclimber(amstel)
            break

        elif antwoord == "random_walk":
            random_walk(amstel, plattegrond)
            visualisatie_random_walk(amstel)
            break

        elif antwoord == "annealing":
            soort_afkoeling = input("Welk koelsysteem wilt u gebruiken: lineair_afkoeling, log_afkoeling of exp_afkoeling?:  ")
            print("______________________________________________________________ \n")
            if soort_afkoeling not in ["lineair_afkoeling", "log_afkoeling", "exp_afkoeling"]:
                print("Beantwoord vraag met: lineair_afkoeling, log_afkoeling of exp_afkoeling")
            elif soort_afkoeling == "lineair_afkoeling":
                for i in range(5):
                    annealing(amstel, plattegrond, lineair_afkoeling, 1000000)
                    schuif_hillclimber(amstel, plattegrond)
                visualisatie_annealing(amstel)
                break

            elif soort_afkoeling == "log_afkoeling":
                for i in range(5):
                    annealing(amstel, plattegrond, log_afkoeling, 100)
                    schuif_hillclimber(amstel, plattegrond)
                visualisatie_annealing(amstel)
                break

            elif soort_afkoeling == "exp_afkoeling":
                for i in range(5):
                    annealing(amstel, plattegrond, exp_afkoeling, 1000000000)
                    schuif_hillclimber(amstel, plattegrond)
                visualisatie_annealing(amstel)
                break

        else:
            schuif_hillclimber(amstel, plattegrond)
            visualisatie_schuif_hillclimber(amstel)
            break

    # 60 huizen-variant (zie Readme voor toelichting)
    else:
        antwoord = input("\nWerken met schuif_hillclimber of annealing?:  ")
        print("______________________________________________________________ \n")
        if antwoord not in ["schuif_hillclimber", "annealing"]:
            print("Beantwoord vraag met: schuif_hillclimber of annealing")

        elif antwoord == "annealing":
            soort_afkoeling = input("Welk koelsysteem wilt u gebruiken: lineair_afkoeling, log_afkoeling of exp_afkoeling?:  ")
            print("______________________________________________________________ \n")
            if soort_afkoeling not in ["lineair_afkoeling", "log_afkoeling", "exp_afkoeling"]:
                print("Beantwoord vraag met: lineair_afkoeling, log_afkoeling of exp_afkoeling")
            elif soort_afkoeling == "lineair_afkoeling":
                for i in range(5):
                    annealing(amstel, plattegrond, lineair_afkoeling, 1000000)
                    schuif_hillclimber(amstel, plattegrond)
                visualisatie_annealing(amstel)
                break

            elif soort_afkoeling == "log_afkoeling":
                for i in range(5):
                    annealing(amstel, plattegrond, log_afkoeling, 100)
                    schuif_hillclimber(amstel, plattegrond)
                visualisatie_annealing(amstel)
                break

            elif soort_afkoeling == "exp_afkoeling":
                for i in range(5):
                    annealing(amstel, plattegrond, exp_afkoeling, 1000000000)
                    schuif_hillclimber(amstel, plattegrond)
                visualisatie_annealing(amstel)
                break

        else:
            schuif_hillclimber(amstel, plattegrond)
            visualisatie_schuif_hillclimber(amstel)
            break
