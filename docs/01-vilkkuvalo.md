# Vilkku valo

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
 
* 1 x [LED diodi](https://fi.wikipedia.org/wiki/LED)
* 2 x hyppykaapeleita
* 1 x [Arduino UNO](https://www.arduino.cc/en/Guide/ArduinoUno)
* 1 x [Koekytkentälevy](https://fi.wikipedia.org/wiki/Koekytkent%C3%A4levy)

# Aloitus

Kokeen alussa tulee tehdä tarvittavat kytkennät jonka jälkeen Arduinon voi liittää tietokoneeseen kiinni. *MUISTA* aina tehdä kytkennät kun virta on pois päältä (irti tietokoneesta). Näin vältytään laitteiston mahdolliselta hajoamiselta.

## Kytkentä

![Kytkentäkaavio](https://github.com/Atihinen/a4kidsWs/raw/master/media/labs/blink/blink_wiring.jpg)

Liitetään musta kaapeli koekytkentälevyn pitkään siniseen viivaan joka on yhteydessä Arduinon GROUND IO pinniin. Toinen pää kinnitetään LEDin miinus pinniin (viistetty kulma).

Värikäs kaapeli kiinnitetään vapaaseen jääneeseen LED pinniin ja Arduinon IO pinniin numero 13.

## Arduino kytkentä tietokoneeseen

Liitä Arduinon mukana tuleva USB kaapeli Arduinoon ja tietokoneessa vapaana olevaan USB porttiin.

## Avaa S4A

Nyt voimme avata S4A sovellus jonka tulisi huomata Arduinon olevan kiinni.

# Ohjelmakoodi

Ohjelmakoodin tarkoituksena on tehdä ohjelma joka väläyttää LED valoa sekunnin ajan ja sammuu sitten sekunniksi. Tätä sykliä on tarkoitus jatkaa niin kauan kuin ohjelma on ajossa.

Ohjelmakoodi rakkentaan S4A ympäristössä kuin LEGO palikat. Valitaan sopiva toimenpide ja raahataan se keskelle. Palikoita voi yhdistellä toisiinsa raahamalla ne lähekkäin.

## Ohjelmakoodin vaiheet

1. Aloitataan ohjelman aloitus. Tämä tapahtuu lisäämällä `When FLAG clicked` komento
![When FLAG clicked komento](https://github.com/Atihinen/a4kidsWs/raw/master/media/code_commands/when_flag_clicked.jpg)
1. Lisätään loputon silmukka
![Forever loop komento](https://github.com/Atihinen/a4kidsWs/raw/master/media/code_commands/forver_loop.jpg)
1. Lisätään `digital 13 on` komento. Tällä laitetaan LED valo päälle. Huomaa että tähän voi käyttää myös muita IO pinnejä kuin 13, mutta sitten pitää muuttaa kytkentää.
![Digital 13 on komento](https://github.com/Atihinen/a4kidsWs/raw/master/media/code_commands/digital_io_on.jpg)
1. Listään odota sekuntti, jolloin LED valo on odotusajan verran päällä. Huomaa että tähän voidaan asettaa mikä tahansa numero joka kuvastaa kuinka monta sekunttia pitäisi odottaa.
![wait for x secs komento](https://github.com/Atihinen/a4kidsWs/raw/master/media/code_commands/wait_for_x_secs.jpg)
1. Lisätään `digital 13 off` komento. Tällä laitetaan LED valo pois päältä. Huomaa että tässä vaihtoehto pitää olla sama numero kuin mikä oli `digital on` komennossa.
![Digital 13 off komento](https://github.com/Atihinen/a4kidsWs/raw/master/media/code_commands/digital_io_off.jpg)
1. Lopuksi laitetaan vielä 1 sekunnin odotus jotta valo on poissa päällä myös yhden sekunnin. Muuten emme välttämättä huomaa mikäli valo kävi pois päältä ollenkaan.
![wait fo x secs komento](https://github.com/Atihinen/a4kidsWs/raw/master/media/code_commands/wait_for_x_secs.jpg)

## Lopullinen ohjelmakoodi

Lopullinen ohjelmakoodi tulisi näyttää suurinpiirtein tältä

![Lopullinen ohjelmakoodi](https://github.com/Atihinen/a4kidsWs/raw/master/media/labs/blink/blink_code.jpg)

## Käynnistä ohjelma

S4A oikeassa yläreunassa on vihreä lipun kuva. Tästä painamalla pitäisi ohjelmakoodi lähteä ajoon ja LED valo tulisi alkaa vilkkumaan.
![Vihreä aloita ohjelmakoodi lippu](https://github.com/Atihinen/a4kidsWs/raw/master/media/start_script.jpg) 

Mikäli näin ei tapahdu. Tarkista kytkennät ja että oikeat IO pinnit on käytössä sekä LED valon toiminta erillisellä virtalähteellä.

## Lopeta ohjelma

S4A oikeassa yläreunassa on punainen kahdeksankulmio. Tästä painamalla pitäisi ohjelmakoodin suoritus loppua ja valo jää siihen tilaan mikä oli viimeksi ollut.
![Punainen lopeta ohjelmakoodi kahdeksankulmio](https://github.com/Atihinen/a4kidsWs/raw/master/media/stop_script.jpg)

Huomaa, LED valo voi jäädä vielä palamaan riippuen edellisestä valon tilasta. Sammuttaaksesi Arduino tulee sinun irrottaa se tietokoneesta irti.

# Kysymys

Muuta ohjelmakoodia esimerkin mukaisesti.

![Jälkimmäinen wait 1 secs muutetaan wait 4 secs](https://github.com/Atihinen/a4kidsWs/raw/master/media/labs/blink/blink_code_question.jpg)

Muutos ei tarvitse uudelleen kytkentää joten Arduinoa ei tarvitse irrottaa tietokoneesta.

_Miten LED valo käyttäytyy kun ohjelmakoodi käynnistetään? Miksi näin tapahtui?_