# Servo

## Sisältö

1. Laitteisto
1. Aloitus
    1. Kytkentä
    1. Arduino kytkentä tietokoneeseen
1. Ohjelma
    1. Ohjelma rivi riviltä
1. Kysymys


## Laitteisto

Tämän kokeen suorittamiseksi tarvitset:
 
* 1 x [Servomoottori SG90](https://fi.wikipedia.org/wiki/Servo)
* 3 x hyppykaapeleita
* 1 x [Arduino UNO](https://www.arduino.cc/en/Guide/ArduinoUno)
* 1 x [Koekytkentälevy](https://fi.wikipedia.org/wiki/Koekytkent%C3%A4levy)

## Aloitus

Kokeen alussa tulee tehdä tarvittavat kytkennät jonka jälkeen Arduinon voi liittää tietokoneeseen kiinni. *MUISTA* aina tehdä kytkennät kun virta on pois päältä (irti tietokoneesta). Näin vältytään laitteiston mahdolliselta hajoamiselta.

## Kytkentä

![Kytkentäkaavio](https://github.com/Atihinen/a4kidsWs/raw/master/media/labs/servo/servo-c_wiring.jpg)

Liitetään yleensä rusehtava kaapeli koekytkentälevyn pitkään siniseen viivaan, joka on yhteydessä Arduinon GROUND IO pinniin. Punainen johto kiinnitetään koekytkentälevyn pitkään punaiseen viivaan, joka on yhteydessä Arduinon 5V IO pinniin. 

Viimeinen oranssi kaapeli servosta kiinnitetään Arduinon IO pinniin 8.

## Arduino kytkentä tietokoneeseen

Liitä Arduinon mukana tuleva USB kaapeli Arduinoon ja tietokoneessa vapaana olevaan USB porttiin.

## Ohjelma

```cpp
#include <Servo.h>

Servo servo;  // luo servo-objekti servon ohjaamiseksi

void setup() {
    servo.attach(8);  // kiinnittää servon pinniin 8 servo-objektiin
}

void loop() {
    servo.write(0);  // käskee servoa menemään asentoon 0
    delay(1000);       // odota sekunti
    servo.write(90); // käskee servoa menemään asentoon 90
    delay(1000);       // odota sekunti
}
```

## Ohjelma rivi riviltä

`#include <Servo.h>` rivillä haetaan ohjelmalle valmis kirjasto nimeltä Servo. Kirjasto on kuin iso laatikko, jossa on valmiita ohjeita ja työkaluja, joita ohjelma voi käyttää.

Servo-kirjasto auttaa ohjelmaa ohjaamaan servomoottoria, joka on pieni moottori, jota voidaan liikuttaa tarkasti tiettyyn asentoon. Tämä rivi siis kertoo ohjelmalle, että se voi käyttää näitä valmiita ohjeita ja työkaluja servomoottorin ohjaamiseen.

`servo.attach(8);` -komento kiinnittää servomoottorin ohjauksen Arduino-ohjelmassa digitaaliseen pinniin 8. Tämä tarkoittaa, että servomoottori saa ohjaussignaalinsa tästä pinnistä, jolloin voit hallita servon liikettä ohjelmallisesti. Tätä käytetään yleensä servomoottorin alustamiseen ennen sen käyttöä.

`servo.write(0);` -komennolla asetetaan servomoottorin kulmaksi 0 astetta. Tämä tarkoittaa, että servomoottori kääntyy alkuasentoonsa. Tätä käytetään usein servon nollaamiseen tai asettamiseen tiettyyn asentoon.

### Wokwi esimerkki
[https://wokwi.com/projects/416998881788984321](https://wokwi.com/projects/416998881788984321)

## Kysymys

Muuta ensimmäisen `servo.write()` metodin arvo `0` arvoon `45`. Päivitä ohjelmakoodi arduinoon. Mitä tapahtuu servolle?

