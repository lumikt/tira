## Testausdokumentti


### Testauksen yleiskuvaus

Testit keskittyvät tällä hetkellä tärkeimpien moduulien testaukseen, eli trie.py sekä generator.py moduuleihin. Testien tarkoitus on varmistaa, että moduulit toimivat halutusti kehityksen edistyessä. Tarkemmat kuvaukset testauksesta löytyvät alta.

Testit voidaan ajaa komennolla poetry run pytest src, tai vain pytest src. Testejä on kahdessa eri tiedostossa, jokainen omalle moduulilleen. Testit on kirjoitettu käyttäen pythonin unittest-kirjastoa sekä pytest-kirjastoa testien ajamiseen.

### Trie.py
Trie-oliolla on apuluokka Node jota ei tällä hetkellä testata suoraan, Noden koodia kuitenkin testataan kuitenkin epäsuorasti Trie-luokan testeillä sillä Trien toiminnot vaativat Noden toimivuutta jotta ne läpäisisivät testit.

Trie-rakennetta testataan luomalla Trie()-luokka, johon lisätään sanoja trien omilla komennoilla. Ensin testaus varmistaa, että trie voidaan lisätä onnistuneesti yksi merkki, eli luoda trie joka on syvyydeltään 2, sisältäen tyhjän alkusolmun sekä lisätyn merkin solmun. Solmun lisäys varmistetaan tarkastmalla aloitussolmun lapsisanakirjan sisältö.

Seuraavaksi testataan trien hakutoimintoa, jota tarvitaan monimutkaisempien merkkijonojen lisäyksessä. Haun tulee palauttaa Node-olio tai None jos haettua merkkijonoa ei ole. Haku etsi rekursiivisesti trien läpi. 

Kun haku on todettu toimivaksi, testaan monimutkaisempien sanoja lisäystä, jossa varmistetaan, että sana tallentuu asteen mukaisesti. Kun tämä on tehty, testataan useampien sanojen lisäämistä ja hakemista, jotta varmistutaan että trie lisää kaikki halutut merkkijonot.
Trie-rakenteen tulee toimia mielivaltaisella asteella, joten seuraavaksi testataan useampien trie-rakenteiden toimivuutta luomalla Trie-olioita asteilla 1–10 ja lisäämällä niihin sama sana. Sanasta muodostuvaa merkkijonoa haetaan triestä jotta nähdään että sana on lisätty oikein (ja trien syvyys vastaa aste+1 lukua).

Lopuksi varmistetaan, että lisättäessä triehen merkkijono sen esiintyvyys päivittyy ensilisäyksellä (arvoon 1) sekä myöhemmin jos sama merkkijono lisätään vielä n kertaa, arvoon n+1.

### Generator.py
Generaattorin testaaminen on haastavampaa, sillä se perustuu todennäköisyyksiin ja tulosteen arviointi vaatii sanan ”oikeellisuuden” arviointia, eli kuinka hyvin generoitu sana vastaa harjoitusdatan antamia esimerkkejä oikeasta kielistä tai vaikka nimistä.
Generaattorista testataan tällä hetkellä annettujen parametrien toteutumista eli sanan pituuden ja sanojen määrän pituutta. 

