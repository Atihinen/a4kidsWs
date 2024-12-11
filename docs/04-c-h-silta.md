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
 
* 1 x [H-silta L9110](https://en.wikipedia.org/wiki/H-bridge)
* 1 x [Sähkömoottori](https://fi.wikipedia.org/wiki/S%C3%A4hk%C3%B6moottori)
* 3 x hyppykaapeleita
* 1 x [Arduino UNO](https://www.arduino.cc/en/Guide/ArduinoUno)
* 1 x [Koekytkentälevy](https://fi.wikipedia.org/wiki/Koekytkent%C3%A4levy)

## Aloitus

Kokeen alussa tulee tehdä tarvittavat kytkennät jonka jälkeen Arduinon voi liittää tietokoneeseen kiinni. *MUISTA* aina tehdä kytkennät kun virta on pois päältä (irti tietokoneesta). Näin vältytään laitteiston mahdolliselta hajoamiselta.

## Kytkentä

## Ohjelma

```cpp
// Määrittele L9110 H-sillan pinnit
const int A1A = 3;  // määrittele pinni 3 A-1A:lle (PWM-nopeus)
const int A1B = 4;  // määrittele pinni 4 A-1B:lle (suunta)

void setup() {
  pinMode(A1A, OUTPUT);     // määrittele nämä pinnit lähtöpinneiksi
  pinMode(A1B, OUTPUT);
  analogWrite(A1A, 0);   // aloita moottorit pois päältä
  digitalWrite(A1B, LOW);
}

void loop() {
  // käynnistä moottori alhaisella nopeudella
  analogWrite(A1A, 150);
  digitalWrite(A1B, LOW);
  delay(4000);              // anna moottorin käydä 4 sekuntia

  // pysäytä moottori
  analogWrite(A1A, 0);   // molempien pinien asettaminen LOW:ksi pysäyttää moottorin
  delay(2000);              // pidä moottori pois päältä 2 sekuntia

  // käynnistä moottori vastakkaiseen suuntaan samalla nopeudella
  digitalWrite(A1B, HIGH);  // vaihda suuntaa
  analogWrite(A1A, 255-150); // tässä logiikka nopeudelle on käänteinen
  delay(4000);              // anna moottorin käydä 4 sekuntia

  // nopeuta moottoria
  analogWrite(A1A, 0);   // tässä logiikka nopeudelle on käänteinen
  delay(2000);

  // pysäytä moottori
  analogWrite(A1A, 0);   // molempien pinien asettaminen LOW:ksi pysäyttää moottorin
  digitalWrite(A1B, LOW);
  delay(2000);

}
```

### Ohjelma rivi riviltä

# Kysymys