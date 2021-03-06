# Algoritmes
De Code bevat onder anderen alle algoritmes die voor deze case zijn gebruikt.
Per algoritme wordt verderop een korte samenvatting gegeven.

De folder bevat de volgende algoritmes:
random_walk.py
schuif_hillclimber.py
verplaats_hillclimber.py
annealing.py

## Opmerking 60 huizen-variant
Bij het plaatsen van 60 huizen, in combinatie met de sloten, werkte de random_walk en verplaats_hillclimber algoritmes niet voldoende. Na enkele iteraties liep soms de berekening vast. Dit komt waarschijnlijk doordat er in de wijk niet genoeg ruimte was om het huis random te verplaatsen. 
De simulated annealing, in combinatie met het schuif_hillclimber algoritme, gaf de voor de 60 huizen variant de meest relevante resultaten. Door, de naar ons inzien, mindere relevantie van random_walk en verplaats_hillclimber hebben wij ervoor gekozen het aantal algoritmes voor 60 huizen aan te passen. De optie van 60 huizen is nu alleen te runnen met simulated annealing in combinatie met het schuif_hillclimber algoritme en het schuif_hillclimber algoritme alleen. Bij de 20 en 40 huizen variant kunnen uiteraard wel alle algoritmes worden gerund.

## Random walk *(random_walk.py)*
Door het random_walk algoritme wordt een wijk random geplaatst. Vervolgens wordt random een huis uit de wijk gekozen en ook weer random verschoven. Er wordt hierin niet gekeken naar verbetering en verslechtering. Het huis krijgt een nieuwe x en y coordinaat en wordt daarmee herplaatst. Bij de random walk algoritme wordt een kijkje in het oplossingslandschap weergegeven.

## Hillclimber *(schuif_hillclimber.py)*
De 'schuif_hillclimber' kiest een random huis uit de wijk en verschuift het met
een random waarde tussen de -10 en 10 meter naar onder, boven, links of rechts. Vervolgens wordt gekeken of dit een betere oplossing genereert. Zo niet, dan wordt het huis weer teruggeplaatst op de oude plek.

## Hillclimber *(verplaats_hillclimber.py)*
De 'verplaats_hillclimber' kiest een random huis uit de wijk en verplaatst het naar een random plek en kijkt of dit een betere oplossing genereert. De defenitie van 'verplaatsen' in het algoritme is het random vervangen van de huidige x en y coordinaat.
Als de nieuwe oplossing slechter is dan de vorige, dan wordt het huis weer teruggeplaatst. Als het een verbetering is blijft het huis staan en zal er gekeken worden naar een nieuwe verbetering.

## Simulated Annealing *(annealing.py)*
Beginnend met de schuif_hillclimber om vervolgens met een bepaalde kans een
verslechtering toe te laten. Bij een verslechtering moet de kans op
toelating kleiner zijn dan bij een verbetering van de waarde. Dit wordt gebruikt om
uit een lokaal optimum te komen en een betere oplossing te vinden.
In onze code zijn er 3 soorten koelschema's mogelijk: lineair, exponentieel en logaritmisch. 


