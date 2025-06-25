## Testausdokumentti


### Testauksen yleiskuvaus

Testit keskittyvät tällä hetkellä tärkeimpien moduulien testaukseen, eli data_handler.py, trie.py sekä generator.py moduuleihin. Testien tarkoitus on varmistaa, että moduulit toimivat halutusti. Tarkemmat kuvaukset testauksesta löytyvät alta.

Testit voidaan ajaa komennolla poetry run pytest src, tai vain pytest src. Testejä on kolmessa eri tiedostossa, jokainen omalle moduulilleen. Testit on kirjoitettu käyttäen pythonin unittest-kirjastoa sekä pytest-kirjastoa testien ajamiseen.

### Testikattavuus
![cvgreport](https://github.com/user-attachments/assets/ad879d5e-8ceb-4eb3-9c8b-a2b39273f63b)

Testit kattavat moduulien osat hyvin. Puuttuvat osat ovat I/O-operaatioita data_handler.py:ssä, generator.py:ssä oleva Trie-lisäys joka testataan trien omissa testeissä sekä trie.py:ssä olevat olioiden repr-metodit joita käytettiin vain kehitykseen.

Kattavuusraportti on saataville ajamalla coveragen testipaketti.

Käynnistetään poetry:

    poetry shell

jonka jälkeen ajetaan:

    poetry run coverage --branch -m pytest

ja raportti generoidaan ajamalla:

    poetry run coverage html

jonka jälkeen kattavuusraportti on luettavissa automaattiesti muodostuvassa htmlcov-kansiossa.

### Trie.py

Trie-oliolla on apuluokka Node jota ei tällä hetkellä testata suoraan, Noden koodia kuitenkin testataan kuitenkin epäsuorasti Trie-luokan testeillä sillä Trien toiminnot vaativat Noden toimivuutta, jotta ne läpäisisivät testit.

Trie-rakennetta testataan luomalla Trie()-luokka, johon lisätään sanoja trien omilla komennoilla. Ensin testaus varmistaa, että trie voidaan lisätä onnistuneesti yksi merkki, eli luoda trie joka on syvyydeltään 2, sisältäen tyhjän alkusolmun sekä lisätyn merkin solmun. Solmun lisäys varmistetaan tarkastmalla aloitussolmun lapsisanakirjan sisältö.

Seuraavaksi testataan trien hakutoimintoa, jota tarvitaan monimutkaisempien merkkijonojen lisäyksessä. Haun tulee palauttaa Node-olio tai None jos haettua merkkijonoa ei ole. Haku etsi rekursiivisesti trien läpi. 

Kun haku on todettu toimivaksi, testaan monimutkaisempien sanoja lisäystä, jossa varmistetaan, että sana tallentuu asteen mukaisesti. Kun tämä on tehty, testataan useampien sanojen lisäämistä ja hakemista, jotta varmistutaan että trie lisää kaikki halutut merkkijonot.
Trie-rakenteen tulee toimia mielivaltaisella asteella, joten seuraavaksi testataan useampien trie-rakenteiden toimivuutta luomalla Trie-olioita asteilla 1–10 ja lisäämällä niihin sama sana. Sanasta muodostuvaa merkkijonoa haetaan triestä jotta nähdään että sana on lisätty oikein (ja trien syvyys vastaa aste+1 lukua).

Tämän jälkeen varmistetaan, että lisättäessä triehen merkkijono sen esiintyvyys päivittyy ensilisäyksellä (arvoon 1) sekä myöhemmin jos sama merkkijono lisätään vielä n kertaa, arvoon n+1.

Lopuksi testataan että trieen muodostuu oikeanlainen puurakenne vertaamalla käsin laskettua trie-rakennetta triestä löytyvään rakenteeseen.

### Generator.py
Generaattorin testaaminen on haastavampaa, sillä se perustuu todennäköisyyksiin ja tulosteen arviointi vaatii sanan ”oikeellisuuden” arviointia, eli kuinka hyvin generoitu sana vastaa harjoitusdatan antamia esimerkkejä oikeasta kielistä tai vaikka nimistä.
Generaattorista testataan tällä hetkellä annettujen parametrien toteutumista eli sanan pituuden ja sanojen määrän pituutta.

Generaattoria on testattu manuaalisesti generaation oikeellisuuden suhteen, generoituvat sanat vaikuttavat muistuttavan harjoitusdatan sanoja. Asteen muutos vaikuttaa sanojen "oikeellisuuteen" manuaalisesti havainnoituna kuten sen kuulukin tehdä.

### Data_handler.py
DataHandler-luokasta testataan, että se varmasti poistaa erikoismerkit sekä erityisesti tyhjät välilyönnit harjoitusdatasta. I/O-operaatioita ei testata ollenkaan ohjeistuksen mukaan. I/O operaatiot on testattu manuaalisesti.

### UI
Sovelluksen käyttöliittymää ei testata lainkaan testien kautta. Käyttöliittymää on testattu manuaalisesti, että se suorittaa tiedoston valinnan oikein, syötetyt parametrit tallentuvat oikein, datan harjoittelu toimii, tiedoston tallentaminen toimii sekä että sanojen generointi ja näyttö käyttäjälle toimii.
