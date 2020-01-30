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

1. Aloitataan ohjelman aloitus. Tämä tapahtuu lisäämällä `When FLAG clicked` komento
![When FLAG clicked komento](https://github.com/Atihinen/a4kidsWs/raw/master/media/code_commands/when_flag_clicked.jpg)
1. Lisätään loputon silmukka
![Forever loop komento](https://github.com/Atihinen/a4kidsWs/raw/master/media/code_commands/forver_loop.jpg)
1. Lisätään motor komento kulmaan 0
![Motor komento kulmassa 0](https://github.com/Atihinen/a4kidsWs/raw/master/media/code_commands/motor_0_angle.jpg) tämä asettaa servo moottorin 0 asteen kulmaan
1. Listään odota sekuntti, jolloin servomoottorin asento on odotusajan verran sama. Huomaa että tähän voidaan asettaa kaksi arvoa. Servomoottorin pinnin numero ja kulma joka voi olla mitä vain 0-360 väliltä.
![wait for x secs komento](https://github.com/Atihinen/a4kidsWs/raw/
1. Lisätään motor komento kulmaan 90
![Motor komento kulmassa 0](https://github.com/Atihinen/a4kidsWs/raw/master/media/code_commands/motor_90_angle.jpg) tämä asettaa servo moottorin 90 asteen kulmaan
1. Tähän laitetaan vielä 1 sekunnin odotus jotta servomoottori ei liiku yhden sekunnin.
![wait fo x secs komento](https://github.com/Atihinen/a4kidsWs/raw/master/media/code_commands/wait_for_x_secs.jpg)
1. Lisätään motor komento kulmaan 180
![Motor komento kulmassa 0](https://github.com/Atihinen/a4kidsWs/raw/master/media/code_commands/motor_180_angle.jpg) tämä asettaa servo moottorin 180 asteen kulmaan
1. Lopuksi laitetaan vielä 1 sekunnin odotus jotta servomoottori ei liiku yhden sekunnin, ennenkuin silmukka alkaa alusta.
![wait fo x secs komento](https://github.com/Atihinen/a4kidsWs/raw/master/media/code_commands/wait_for_x_secs.jpg)


## Lopullinen ohjelmakoodi

Lopullinen ohjelmakoodi näyttää kutakuinkin tältä
![Lopullinen ohjelamoodi](https://github.com/Atihinen/a4kidsWs/raw/master/media/labs/servo/servo_script.jpg)

## Käynnistä ohjelma

S4A oikeassa yläreunassa on vihreä lipun kuva. Tästä painamalla pitäisi ohjelmakoodi lähteä ajoon ja servo moottori alkaisi liikkumaan.
![Vihreä aloita ohjelmakoodi lippu](https://github.com/Atihinen/a4kidsWs/raw/master/media/start_script.jpg) 

Mikäli näin ei tapahdu. Tarkista kytkennät ja että oikeat IO pinnit on käytössä.

## Lopeta ohjelma

S4A oikeassa yläreunassa on punainen kahdeksankulmio. Tästä painamalla pitäisi ohjelmakoodin suoritus loppua ja servo jää siihen asentoon mikä oli viimeksi ollut.
![Punainen lopeta ohjelmakoodi kahdeksankulmio](https://github.com/Atihinen/a4kidsWs/raw/master/media/stop_script.jpg)

# Kysymys

Muuta ohjelmakoodia esimerkin mukaisesti.

![Keskimmäinen servomoottorin kulma muutetaan 45 asteen kulmaan](https://github.com/Atihinen/a4kidsWs/raw/master/media/labs/servo/servo_script_question.jpg)


Muutos ei tarvitse uudelleen kytkentää joten Arduinoa ei tarvitse irrottaa tietokoneesta.

_Miten servomoottori käyttäytyy kun ohjelmakoodi käynnistetään? Miksi näin tapahtui?_