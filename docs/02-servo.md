# Servo

# Sisältö

1. Laitteisto
1. Aloitus
    1. Kytkentä
    1. Arduino kytkentä tietokoneeseen
    1. Avaan S4A
1. Ohjelmakoodi
    1. Ohjelmakoodin vaiheet
    1. Lopullinen ohjelmakoodi
    1. Käynnistä ohjelmakoodi
    1. Lopeta ohjelmakoodi
1. Kysymys


# Laitteisto

Tämän kokeen suorittamiseksi tarvitset:
 
* 1 x [Servomoottori SG90](https://fi.wikipedia.org/wiki/Servo)
* 3 x hyppykaapeleita
* 1 x [Arduino UNO](https://www.arduino.cc/en/Guide/ArduinoUno)
* 1 x [Koekytkentälevy](https://fi.wikipedia.org/wiki/Koekytkent%C3%A4levy)

# Aloitus

Kokeen alussa tulee tehdä tarvittavat kytkennät jonka jälkeen Arduinon voi liittää tietokoneeseen kiinni. *MUISTA* aina tehdä kytkennät kun virta on pois päältä (irti tietokoneesta). Näin vältytään laitteiston mahdolliselta hajoamiselta.

## Kytkentä

![Kytkentäkaavio](https://github.com/Atihinen/a4kidsWs/raw/master/media/labs/servo/servo_wiring.jpg)

Liitetään yleensä rusehtava kaapeli koekytkentälevyn pitkään siniseen viivaan, joka on yhteydessä Arduinon GROUND IO pinniin. Punainen johto kiinnitetään koekytkentälevyn pitkään punaiseen viivaan, joka on yhteydessä Arduinon 5V IO pinniin. 

Viimeinen oranssi kaapeli servosta kiinnitetään Arduinon IO pinniin 8.


## Arduino kytkentä tietokoneeseen

Liitä Arduinon mukana tuleva USB kaapeli Arduinoon ja tietokoneessa vapaana olevaan USB porttiin.

## Avaa S4A

Nyt voimme avata S4A sovellus jonka tulisi huomata Arduinon olevan kiinni.

# Ohjelmakoodi

Ohjelmakoodin tarkoituksena on tehdä ohjelma joka 

Tätä sykliä on tarkoitus jatkaa niin kauan kuin ohjelma on ajossa.

Ohjelmakoodi rakkentaan S4A ympäristössä kuin LEGO palikat. Valitaan sopiva toimenpide ja raahataan se keskelle. Palikoita voi yhdistellä toisiinsa raahamalla ne lähekkäin.

## Ohjelmakoodin vaiheet


## Lopullinen ohjelmakoodi


## Käynnistä ohjelma

S4A oikeassa yläreunassa on vihreä lipun kuva. Tästä painamalla pitäisi ohjelmakoodi lähteä ajoon ja LED valo tulisi alkaa vilkkumaan.
![Vihreä aloita ohjelmakoodi lippu](https://github.com/Atihinen/a4kidsWs/raw/master/media/start_script.jpg) 

Mikäli näin ei tapahdu. Tarkista kytkennät ja että oikeat IO pinnit on käytössä.

## Lopeta ohjelma

S4A oikeassa yläreunassa on punainen kahdeksankulmio. Tästä painamalla pitäisi ohjelmakoodin suoritus loppua ja servo jää siihen asentoon mikä oli viimeksi ollut.
![Punainen lopeta ohjelmakoodi kahdeksankulmio](https://github.com/Atihinen/a4kidsWs/raw/master/media/stop_script.jpg)

# Kysymys

Muuta ohjelmakoodia esimerkin mukaisesti.



Muutos ei tarvitse uudelleen kytkentää joten Arduinoa ei tarvitse irrottaa tietokoneesta.

_Miten servomoottori käyttäytyy kun ohjelmakoodi käynnistetään? Miksi näin tapahtui?_