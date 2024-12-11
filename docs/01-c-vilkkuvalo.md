# Vilkku valo

## Sisältö

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
    // Odotetaan 10 sekunti
    delay(1000);

}
```