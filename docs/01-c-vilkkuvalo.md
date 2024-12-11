# Vilkkuvalo

## Sisältö

1. Laitteisto
1. Aloitus
    1. Kytkentä
    1. Arduino kytkentä tietokoneeseen
1. Ohjelmakoodi
    1. Ohjelmakoodi rivi riviltä
1. Kysymys


## Laitteisto

Tämän kokeen suorittamiseksi tarvitset:
 
* 1 x [LED diodi](https://fi.wikipedia.org/wiki/LED)
* 2 x hyppykaapeleita
* 1 x [Arduino UNO](https://www.arduino.cc/en/Guide/ArduinoUno)
* 1 x [Koekytkentälevy](https://fi.wikipedia.org/wiki/Koekytkent%C3%A4levy)
* 1 x [Vastus](https://fi.wikipedia.org/wiki/Vastus)

## Aloitus

Kokeen alussa tulee tehdä tarvittavat kytkennät jonka jälkeen Arduinon voi liittää tietokoneeseen kiinni. *MUISTA* aina tehdä kytkennät kun virta on pois päältä (irti tietokoneesta). Näin vältytään laitteiston mahdolliselta hajoamiselta.

### Kytkentä

![Kytkentäkaavio](https://github.com/Atihinen/a4kidsWs/raw/master/media/labs/blink/blink-c.jpg)

Kytke GND LEDin miinus pinniin (viistetty kulma). Kytke PIN 10 vastustajan toiseen pinniin ja vastuksen toinen pinni LEDin vapaaseen jääneeseen pinniin.

### Ohjelma

```cpp
// Määritellään LEDin pinni
const int ledPin = 10;

void setup() {
    // Asetetaan LEDin pinni OUTPUT-tilaan
    pinMode(ledPin, OUTPUT);
}

void loop() {

    // Laitetaan LED päälle
    digitalWrite(ledPin, HIGH);
    // Odotetaan 1 sekunti
    delay(1000);
    // Laitetaan LED pois päältä
    digitalWrite(ledPin, LOW);
    // Odotetaan 1 sekunti
    delay(1000);

}
```

# Ohjelma rivi riviltä

`const int ledPin = 10;` Tässä koodirivissä määritellään vakio ledPin, joka on tyyppiä int ja jonka arvoksi asetetaan 10. Tämä tarkoittaa, että muuttuja ledPin viittaa mikrokontrollerin (esim. Arduino) digitaaliseen pinnin numeroon 10, johon LED-valo on kytketty.

`void setup() { ... }` Tämä funktio ajetaan kerran, kun ohjelma käynnistyy. Tässä asetetaan LEDin pinni OUTPUT-tilaan.

`void loop() { ... }` Tämä funktio ajetaan jatkuvasti uudelleen ja uudelleen. Tässä laitetaan LED päälle, odotetaan 1 sekunti, laitetaan LED pois päältä ja odotetaan taas 1 sekunti.

`pinMode(ledPin, OUTPUT);` Tässä koodirivissä pinMode(ledPin, OUTPUT); määritellään, että mikrokontrollerin (esim. Arduino) ledPin-nasta toimii lähtönä (OUTPUT). Tämä tarkoittaa, että kyseistä nastaa käytetään ohjaamaan ulkoista laitetta, kuten LED-valoa. pinMode-funktiota käytetään asettamaan nastan toimintatila joko tuloksi (INPUT) tai lähdöksi (OUTPUT).

`digitalWrite(ledPin, HIGH);` -komennolla asetetaan ledPin-nimiseen muuttujaan tallennettu pinni korkeaan tilaan (HIGH). Tämä tarkoittaa, että kyseiseen pinniin kytketty LED-valo syttyy. Tämä komento on yleisesti käytössä Arduino-ohjelmoinnissa, jossa ohjataan mikrokontrollerin pinnejä.

`delay(1000);` kutsutaan funktiota `delay`, joka pysäyttää ohjelman suorituksen 1000 millisekunniksi (eli 1 sekunniksi). Tämä on hyödyllistä esimerkiksi silloin, kun halutaan odottaa tietyn ajan ennen seuraavan koodirivin suorittamista, kuten vilkkuvalon sytyttämisessä ja sammuttamisessa tietyin väliajoin.

`digitalWrite(ledPin, LOW);` -komennolla asetetaan ledPin-nimiseen muuttujaan tallennettu pinni matalaan tilaan (LOW). Tämä tarkoittaa, että kyseiseen pinniin kytketty LED-valo sammuu. Tämä komento on yleisesti käytössä Arduino-ohjelmoinnissa, jossa ohjataan mikrokontrollerin pinnejä.

# Kysymys

Muuta ohjelmassa jälkimmäisen `delay` arvo `1000` arvoon `10000`. Päivitä ohjelmakoodi Arduinoon. Mitä tapahtuu ledivalolle?