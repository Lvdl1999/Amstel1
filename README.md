# AmstelHaege
## Door Levy van der Linde & Lisa Lansu
### Minor Programmeren

<img width="200" alt="image" src="https://user-images.githubusercontent.com/47352487/58120398-75876900-7c05-11e9-8a51-82610d15c29d.png">
http://heuristieken.nl/wiki/index.php?title=Heuristieken

#### Casus AmstelHaege
In een ooit beschermd natuurgebied zal een nieuwe woonwijk worden geplaatst. De wijk, met een afmeting van 160 bij 180m, zal zo optimaal mogelijk worden ingedeeld rekening houdend met verscheidene restricties. De verhoudingen tussen de drie soorten huizen **(eengezinswoning, bungolow en maison)** zijn vastgesteld op 60%, 25% en 15%. Daarnaast hebben de huizen verschillende attributen. Zo zijn de prijzen, oppervlaktes, minimale verplichte vrijstand en prijsverbetering oplopend van eengezinswoning tot maison. In de wijk zullen ook (maximaal 4) sloten worden aangelegd, welke 20% van de wijk in beslag zullen nemen, en waarbij de sloten een uiterlijke verhouding van 1:4 hebben. Om zo veel mogelijk waarde te genereren moet er gekeken worden naar de vrijstand, **des te meer vrijstand, des te hoger de waarde** (niet cumulatief).


### Vereisten
Deze codebase is volledig geschreven in [Python3.7.1](https://www.python.org/downloads/). In requirements.txt staan alle benodigde packages om de code succesvol te draaien. Deze zijn gemakkelijk te installeren via pip dmv. de volgende instructie:
```
pip install -r requirements.txt
```

### Gebruik
| Stap | Keuze|
|--------|------------------------------|
| 0 | Download of clone de 'Amstel1' GitHub repository.
| 1 | `pythonw main.py` voor een MacBook en `python main.py` voor Windows laptops.
| 2 | U kunt een wijk van '20', '40' of '60' huizen kiezen.*** |
| 3 | Vervolgens kunt u minimaal '1' en maximaal '4' sloten in de wijk plaatsen.  |
| 4 | Selecteer vervolgens welk algoritme u wilt runnen. U kunt kiezen tussen `schuif_hillclimber, verplaats_hillclimber, random_walk of annealing`.*** |
| 5 | Wanneer is gekozen voor annealing (oftewel simulated annealing) heeft u keuze uit verschillende koelsystemen. Voor een lineair afkoelschema dient `lineair_afkoeling` te worden ingevoerd. Voor een logaritmisch afkoelschema dient `log_afkoeling` te worden ingevoerd. Voor een exponentieel afkoelschema dient `exp_afkoeling` te worden ingevoerd.
| 6 | Zodra een algoritme heeft gerund kunt u deze beëindigen door het pop-up figuur van de visualisatie te sluiten. |

#### *** Opmerking 60 huizen-variant
Bij het plaatsen van 60 huizen, in combinatie met de sloten, werkte de random_walk en verplaats_hillclimber algoritmes niet voldoende. Na enkele iteraties liep soms de berekening vast. Dit komt waarschijnlijk doordat er in de wijk niet genoeg ruimte was om het huis random te verplaatsen. 
De simulated annealing, in combinatie met het schuif_hillclimber algoritme, gaf de voor de 60 huizen variant de meest relevante resultaten. Door, de naar ons inzien, mindere relevantie van random_walk en verplaats_hillclimber hebben wij ervoor gekozen het aantal algoritmes voor 60 huizen aan te passen. De optie van 60 huizen is nu alleen te runnen met simulated annealing in combinatie met het schuif_hillclimber algoritme en het schuif_hillclimber algoritme alleen. Bij de 20 en 40 huizen variant kunnen uiteraard wel alle algoritmes worden gerund.

### Structuur
Alle Python scripts staan in de folder Code. 

### Bounds
De lowerbound en upperbound zijn beide berekend voor de case AmstelHaege.

#### Lowerbound
Onder de lowerbound wordt verstaan hoeveel de wijk waard is in de minst optimale situatie. Dat is wanneer ieder huis alleen z'n minimale vrijstand in de wijk heeft, dit is de originele huiswaarde. Voor ieder huis in de wijk worden deze waardes opgeteld.

- Voor de 20-huizenvariant is de lowerbound: 7245000 euro.
- Voor de 40-huizenvariant is de lowerbound: 14490000 euro.
- Voor de 60-huizenvariant is de lowerbound: 21735000 euro.     

#### Upperbound
De upperbound geeft aan hoeveel de wijk waard is in de meest optimale situatie. Dat is zodra ieder huis in het midden van de wijk wordt geplaatst zonder andere huizen op de plattegrond. Door deze maximale vrijstand zijn de huisprijzen optimaal en zullen deze bij elkaar worden opgeteld.

- Voor de 20-huizenvariant is de upperbound: 38702925 euro.
- Voor de 40-huizenvariant is de upperbound: 77405850 euro.
- Voor de 60-huizenvariant is de upperbound: 116108775 euro

De berekening van de upper- en de lowerbound zijn in de map Amstel1 te vinden in een file genaamd bounds.py. Met het volgende stappen plan kan deze code eventueel worden gerund bij interesse:

| Stap | Keuze|
|--------|------------------------------|
| 0 |  `pythonw bounds.py` voor een MacBook en `python bounds.py` voor Windows laptops.
| 1 | U kunt een wijk van '20', '40' of '60' huizen kiezen. |
| 2 | Vervolgens kunt u minimaal '1' en maximaal '4' sloten in de wijk plaatsen.  |
| 3 | In dit commando mag worden meegegeven of u de lowerbound, upperbound of beide wilt berekenen. -Voor de lowerbound dient `lowerbound` te worden ingevoerd. -Voor de upperbound dient `upperbound` te worden ingevoerd. -Om beide te berekenen mag `beide` worden ingevoerd.|

## Auteurs

* Levy van der Linde
* Lisa Lansu

## Dankwoord

* Hierbij willen wij graag onze TechAssistent Quinten bedanken voor zijn behulpzaamheid en positiviteit.
* Daarnaast Bram voor zijn goede feedback op onze presentaties en Daan van den Berg voor leerzame en vermakelijke colleges. 
Wij zijn zeer blij met onze behaalde resultaten en het kiezen van de case AmstelHaege.
* minor programmeren van de UvA
