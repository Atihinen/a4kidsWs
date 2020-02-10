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

Ohjelmakoodin tarkoituksena on tehdä ohjelma joka pitää LED valoa päällä niin kauan kuin tietokoneen välilyönti näppäintä on painettu. Tätä sykliä on tarkoitus jatkaa niin kauan kuin ohjelma on ajossa.

Ohjelmakoodi rakkentaan S4A ympäristössä kuin LEGO palikat. Valitaan sopiva toimenpide ja raahataan se keskelle. Palikoita voi yhdistellä toisiinsa raahamalla ne lähekkäin.

## Ohjelmakoodin vaiheet

1. Aloitataan ohjelman aloitus. Tämä tapahtuu lisäämällä `When FLAG clicked` komento
![When FLAG clicked komento](https://github.com/Atihinen/a4kidsWs/raw/master/media/code_commands/when_flag_clicked.jpg)
1. Lisätään loputon silmukka
![Forever loop komento](https://github.com/Atihinen/a4kidsWs/raw/master/media/code_commands/forver_loop.jpg)
1. Lisätään `if else` ehto lause, ehdon sisälle laitetaan `key pressed`. Tällä tarkkaillaan että onko VÄLILYÖNTI näppäin painettuna pohjaan. Tähän voi käyttää muita kirjaimia ja ei vaadi kytkentään muutoksia. Mikäli haluttu näppäin ei ole pohjassa suoritetaan `else` osioon laitettu koodi.
![Joko tai ehto, jossa ehtona on VÄLILYÖNTI pohjassa](https://github.com/Atihinen/a4kidsWs/raw/master/media/labs/pc_control/if_key_pressed_else.jpg)
1. Lisätään `digital 13 on` komento ehdon TOSI haaraan. Tällä laitetaan LED valo päälle, jos VÄLILYÖNTI on painettuna. Huomaa että tähän voi käyttää myös muita IO pinnejä kuin 13, mutta sitten pitää muuttaa kytkentää.
![Digital 13 on komento](https://github.com/Atihinen/a4kidsWs/raw/master/media/code_commands/digital_io_on.jpg)
1. Lisätään `digital 13 off` komento ehdon EPÄTOSI haaraan. Tällä laitetaan LED valo pois päältä, jos VÄLILYÖNTI ei ole painettuna pohjaan. Huomaa että tässä vaihtoehto pitää olla sama numero kuin mikä oli `digital on` komennossa.
![Digital 13 off komento](https://github.com/Atihinen/a4kidsWs/raw/master/media/code_commands/digital_io_off.jpg)

## Lopullinen ohjelmakoodi

Lopullinen ohjelmakoodi tulisi näyttää suurinpiirtein tältä

![Lopullinen ohjelmakoodi](https://github.com/Atihinen/a4kidsWs/raw/master/media/labs/pc_control/pc_control_code.jpg)

## Käynnistä ohjelma

S4A oikeassa yläreunassa on vihreä lipun kuva. Tästä painamalla pitäisi ohjelmakoodi lähteä ajoon ja LED valo tulisi mennä päälle jos VÄLILYÖNTI on painettuna, kun VÄLILYÖNTI näppäimen päästää irti niin LED valon tulisi sammua.
![Vihreä aloita ohjelmakoodi lippu](https://github.com/Atihinen/a4kidsWs/raw/master/media/start_script.jpg) 

Mikäli näin ei tapahdu. Tarkista kytkennät ja että oikeat IO pinnit on käytössä sekä LED valon toiminta erillisellä virtalähteellä.

## Lopeta ohjelma

S4A oikeassa yläreunassa on punainen kahdeksankulmio. Tästä painamalla pitäisi ohjelmakoodin suoritus loppua ja valo jää siihen tilaan mikä oli viimeksi ollut.
![Punainen lopeta ohjelmakoodi kahdeksankulmio](https://github.com/Atihinen/a4kidsWs/raw/master/media/stop_script.jpg)

Sammuttaaksesi Arduino tulee sinun irrottaa se tietokoneesta irti.

# Kysymys

Muuta ohjelmakoodia esimerkin mukaisesti.

![Korvataan if else pelkästään if ehdolla ja lisätään sisälle digital on, wait for sec ja digital off](https://github.com/Atihinen/a4kidsWs/raw/master/media/labs/pc_control/pc_control_code_question.jpg)

Muutos ei tarvitse uudelleen kytkentää joten Arduinoa ei tarvitse irrottaa tietokoneesta.

_Miten LED valo käyttäytyy kun ohjelmakoodi käynnistetään? Miksi näin tapahtui?_