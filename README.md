# AmstelHaege
## Door Levy van der Linde & Lisa Lansu
### Minor Programmeren

<img width="294" alt="image" src="https://user-images.githubusercontent.com/47352487/58120398-75876900-7c05-11e9-8a51-82610d15c29d.png">
http://heuristieken.nl/wiki/index.php?title=Heuristieken

#### Casus AmstelHaege
In een ooit beschermd natuurgebied zal een nieuwe woonwijk worden geplaatst. De wijk, met een afmeting van 160 bij 180m, zal zo optimaal mogelijk worden ingedeeld rekening houdend met verscheidene restricties. De verhoudingen tussen de drie soorten huizen **(eengezinswoning, bungolow en maison)** zijn vastgesteld op 60%, 25% en 15%. Daarnaast hebben de huizen verschillende attributen. Zo zijn de prijzen, oppervlaktes, minimale verplichte vrijstand en prijsverbetering oplopend van eengezinswoning tot maison. In de wijk zullen ook (maximaal 4) sloten worden aangelegd, welke 20% van de wijk in beslag zullen nemen, en waarbij de sloten een uiterlijke verhouding van 1:4 hebben. Om zo veel mogelijk waarde te genereren moet er gekeken worden naar de vrijstand, **des te meer vrijstand, des te hoger de waarde** (niet cumulatief).

### Vereisten

Deze codebase is volledig geschreven in [Python3.6.3](https://www.python.org/downloads/). In requirements.txt staan alle benodigde packages om de code succesvol te draaien. Deze zijn gemakkelijk te installeren via pip dmv. de volgende instructie:

```
pip install -r requirements.txt
```

### Gebruik
| Step | Choice|
|--------|------------------------------|
| 0 | `pythonw main.py`
| 1 | U kunt een wijk van '20', '40' of '60' huizen kiezen. |
| 2 | Vervolgens kunt u minimaal '1' en maximaal '4' sloten in de wijk plaatsen.  |
| 3 | Selecteer vervolgens welk algoritme u wilt runnen. U kunt kiezen tussen `random_hillclimber,    hillclimber, random_walk of annealing`. |
| 4 | For more information regarding the algorithms type `info` |
| 5 | Wanneer is gekozen voor simulated annealing heeft u keuze uit verschillende koelsystemen.
- Voor een lineair afkoelschema dient `linear_afkoeling` te worden ingevoerd.
- Voor een logaritmisch afkoelschema dient `log_afkoeling` te worden ingevoerd.
- Voor een exponentieel afkoelschema dient `exp_afkoeling` te worden ingevoerd. |
| 6 | Zodra een algoritme heeft gerund kunt u deze beeindigen door het figuur van de visualisatie te sluiten. |

### Structuur

Alle Python scripts staan in de folder Code. In de map Data zitten alle input waardes en in de map resultaten worden alle resultaten opgeslagen door de code.

### Test 
Om de code te draaien met de standaardconfiguratie (bv. brute-force en voorbeeld.csv) gebruik de instructie:

```
pythonw main.py
```

### Bounds


## Auteurs

* Levy van der Linde
* Lisa Lansu

## Dankwoord

Hierbij willen wij graag onze TechAssistent Quinten bedanken voor zijn behulpzaamheid en positiviteit. 
Daarnaast Bram voor de feedback op onze presentaties en Daan van den Berg voor leerzame en vermakelijke colleges. 
* minor programmeren van de UvA

