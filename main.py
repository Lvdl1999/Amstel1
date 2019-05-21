from hillclimber import hillclimber
import greedy
from random_walk import random_walk
from random_walk import visualisatie_random_walk
from annealing import annealing, linear_afkoeling


if __name__ == '__main__':

    antwoord = input("Werken met greedy, hillclimber, random_walk of annealing?:  ")
    if antwoord not in ["greedy", "hillclimber", "random_walk", "annealing"]:
        print("Beantwoord vraag met: greedy, hillclimber, random_walk of annealing")
    elif antwoord == "greedy":
        greedy.greedy()
        print(f"Totale wijk waarde is: {int(amstel.totale_nieuwe_huiswaarde())} euro")
        # amstel.visualisatie()
    elif antwoord == "random_walk":
        amstel = random_walk()
        visualisatie_random_walk(amstel)
    elif antwoord == "annealing":
        soort_afkoeling = input("linear_afkoeling, log_afkoeling of exp_afkoeling?:  ")
        if soort_afkoeling not in ["linear_afkoeling, log_afkoeling of exp_afkoeling"]:
            print("Beantwoord vraag met: linear_afkoeling, log_afkoeling of exp_afkoeling")
        elif soort_afkoeling == "linear_afkoeling":
            linear_afkoeling = linear_afkoeling()
            afkoeling(begin_temperatuur, temperatuur, iteraties)
            amstel = annealing(linear_afkoeling, 1000000)
        elif soort_afkoeling == "log_afkoeling":
            amstel = annealing(log_afkoeling, 1000000)
        else:
            amstel = annealing(exp_afkoeling, 1000000)
    else:
        hillclimber()
