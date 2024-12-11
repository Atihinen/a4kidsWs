# Arduino
**Arduino* on pieni tietokone, jota kutsutaan myös mikrokontrolleriksi.
Sitä käytetään erilaisten laitteiden ja projektien rakentamiseen, kuten robottien, valojen ja antureiden ohjaamiseen.
Arduino on helppo oppia ja käyttää, joten se sopii hyvin lapsille ja aloittelijoille.
Voit ohjelmoida Arduinoa tietokoneella ja kertoa sille, mitä sen pitää tehdä.
Kun olet kirjoittanut ohjelman, voit ladata sen Arduinoon ja nähdä, miten se toimii oikeassa elämässä!

# Tarvikkeet

- Arduino-alusta
- USB-johto
- Tietokone

Lisäksi, riippuen projektista, saatat tarvita muita komponentteja, kuten:
- Antureita
- Moottoreita
- LED-valoja
- Vastuksia
- Johtoja
- Painikkeita
- Leipälauta (breadboard)
- Juotostarvikkeet
- Paristot tai virtalähde

Mikäli tarvikkeita ei löydy tai haluat vain kokeilla niin voit myös käyttää palvelua https://wokwi.com/

## Tietokoneelle asennettavat ohjelmat

Helpoiten pääset arduino ohjelmointiin kun käytät Arduino IDE kehitysympäristöä.

https://www.kasityokoulurobotti.fi/2017/11/arduino-ohjelmointiympariston-asennus/

# Ohjelmointi

Ohjelmointi tarkoittaa tietokoneohjelmien luomista ja kehittämistä käyttämällä erilaisia ohjelmointikieliä, kuten Python, Java tai C++. Ohjelmoinnissa kirjoitetaan koodia, joka kertoo tietokoneelle, mitä tehtäviä sen tulee suorittaa. Tämä prosessi sisältää ongelmanratkaisua, logiikan suunnittelua ja algoritmien kehittämistä, jotta tietokone voi suorittaa halutut toiminnot tehokkaasti ja oikein.

# Arduino ohjelmointi

Arduino ohjelmoidaan Arduino C ohjelmointikielellä.

Arduino C eroaa perinteisestä C-ohjelmointikielestä muutamalla tavalla. Ensinnäkin, Arduino-koodissa on kaksi pääfunktiota: `setup()` ja `loop()`, jotka korvaavat perinteisen `main()`-funktion. `setup()` ajetaan kerran ohjelman alussa, kun taas `loop()` toistuu jatkuvasti ohjelman suorittamisen aikana. Lisäksi Arduino tarjoaa laajan kirjaston valmiita funktioita ja makroja, jotka helpottavat laitteiston hallintaa, kuten digitaalisten ja analogisten pinien lukemista ja kirjoittamista. Tämä tekee Arduino C:stä helpommin lähestyttävän erityisesti aloittelijoille ja nopeuttaa kehitystyötä.


## Ohjelmoinnin osat

### Funktiot

Funktiot ovat ohjelmoinnin perusyksiköitä, jotka sisältävät joukon käskyjä, jotka suorittavat tietyn tehtävän. Funktioita käytetään koodin uudelleenkäytettävyyden parantamiseksi ja ohjelman rakenteen selkeyttämiseksi. Arduino-ohjelmoinnissa funktiot määritellään avainsanalla `void` tai palautustyypillä, ja niitä kutsutaan nimellä.

### Toistorakenteet

Toistorakenteet, kuten `for`- ja `while`-silmukat, mahdollistavat koodin suorittamisen toistuvasti tietyn ehdon perusteella. Tämä on hyödyllistä, kun halutaan suorittaa sama tehtävä useita kertoja, kuten LED-valon vilkuttaminen tietyin väliajoin.

### Ehtolauseet

Ehtolauseet, kuten `if`, `else if` ja `else`, mahdollistavat ohjelman suorittamisen eri tavoin eri tilanteissa. Ehtolauseet tarkistavat tietyn ehdon ja suorittavat koodin vain, jos ehto täyttyy. Tämä on tärkeää, kun halutaan tehdä päätöksiä ohjelman suorituksen aikana, kuten tarkistaa, onko painiketta painettu.

### Muuttujat

Muuttujat ovat nimettyjä paikkoja muistiin, joissa voidaan säilyttää tietoa ohjelman suorituksen aikana. Arduino C:ssä on useita muuttujatyyppejä, joita käytetään erilaisten tietojen tallentamiseen. Tässä ovat yleisimmät muuttujatyypit:

- `int`: Kokonaisluku, joka voi olla positiivinen tai negatiivinen. Esimerkiksi: `int ledPin = 13;`
- `float`: Liukuluku, joka voi sisältää desimaaleja. Esimerkiksi: `float temperature = 23.5;`
- `char`: Yksittäinen merkki. Esimerkiksi: `char letter = 'A';`
- `boolean`: Totuusarvo, joka voi olla joko `true` (tosi) tai `false` (epätosi). Esimerkiksi: `boolean isButtonPressed = false;`
- `byte`: 8-bittinen kokonaisluku, joka voi olla välillä 0-255. Esimerkiksi: `byte sensorValue = 255;`
- `long`: Pitkä kokonaisluku, joka voi olla suurempi kuin `int`. Esimerkiksi: `long distance = 100000L;`
- `unsigned int`: Positiivinen kokonaisluku, joka ei voi olla negatiivinen. Esimerkiksi: `unsigned int counter = 0;`
- `unsigned long`: Positiivinen pitkä kokonaisluku. Esimerkiksi: `unsigned long time = 100000UL;`

Näitä muuttujatyyppejä käyttämällä voit tallentaa ja käsitellä erilaisia tietotyyppejä Arduino-ohjelmissasi.