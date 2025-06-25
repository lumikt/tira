## Aineopintojen harjoitustyö: Algoritmit ja tekoäly

[Määrittelydokumentti](https://github.com/lumikt/tira/blob/main/documentation/maarittelydokumentti.md)  
[Testausdokumentti](https://github.com/lumikt/tira/blob/main/documentation/testausdokumentti.md)  
[Toteutusdokumentti](https://github.com/lumikt/tira/blob/main/documentation/toteutusdokumentti.md)  

### Käyttöohje

Tämä ohjelma toteuttaa satunnaisten sanojen generointia käyttäen Markovin ketjua. Käyttäjä voi itse määrittää ketjun asteen ja asettaa muita parametrejä generointiin. Markovin ketju on satunnainen generointimetodi, joka käyttää hyväkseen asteensa mukaista tietoa edeltävistä tiloista. Harjoitusdata on tallennettu trie-rakenteeseen. 

Ohjelman käyttöohjeet löytyvät alta.

### Asennus ja käynnistys

Ohjelman kloonamisen jälkeen riippuvuudet, jotka ovat lähinnä testaamiseen liittyviä, voi asentaa poetryn kautta ajamalla

    poetry install

komentoriviltä. Itse generoinnilla ei ole ulkoisia riippuvaisuuksia pythonin peruskirjastojen ulkopuolelta. Täysien toiminnallisuuksien aktivoimiseksi käynnistetään seuraavaksi poetryn virtuaaliympäristö.

    poetry shell

Huomaa, että jos et ole konfiguroinut poetryn uusinta versiota käyttämään shell-komentoa, joudut käynnistämään venvin poetryn omien ohjeiden mukaan. Shell pluginin asennusohjeet sisältyvät poetryyn jos komentoa yrittää ajaa.

Saat käynnistettyä ohjelman ajamalla komentoriviltä 

    python main.py

jonka jälkeen graafinen käyttöliittymä aukeaa.


### Sovelluksen käyttöohje

![ui](https://github.com/user-attachments/assets/04155495-9ac7-451d-b918-1a5d079b13ef)


Graafisessa käyttöliittymässä tulee ensin valita harjoitustiedosto painamalla __Select training file__ ja valitsemalla haluamasi tiedoston.

Kätevän harjoitusdatan saa esim. Kotuksen nykysuomen sanalistasta, joka löytyy ladattavana tiedostona Kotuksen kotisivuilta. Vastaavasti mikä tahansa UTF-8 enkoodattu .txt muodossa oleva tiedosto voi toimia harjoitusdatana.

Kun harjoitusdata on valittu, aseta haluamasi parametrit generaatioon. __Markov chain degree__ asettaa generoinnin asteen, eli kuinka monta edeltävää tilaa tutkitaan seuraavaa merkkiä valitessa. Mitä suurempi aste, sen "oikeanlaisempaa" generoitu teksti, joskin jos aste on liian korkea, on todennäköisempää, että generoituva sana on todellinen sana harjoitusdatasta.

__Word length__ asettaa generoitavien sanojen pituuden ja __Word amount to generate__ kertoo, kuinka monta sanaa haluat generoida. Jos harjoitusdata on lyhyt, asteet korkeita (3+) sekä sanojen määrä on korkea, on todennäköistä, että generaattori ei pysty generoimaan haluamaasi määrää uniikkeja sanoja. Generaattori ilmoittaa tällöin ongelmasta ja pyytää joko vähentämään generoitavien sanojen määrä, laskemaan astetta tai antamaan enemmän harjoitusdataa.

Kun olet asettanut haluamasi parametrit, paina __Train__ joka populoi trien, eli taustalla olevan tietorakenteen. Harjoittelun jälkeen voit painaa __Run generation__ ja saat satunnaiset sanasi. Jos haluat tallentaa listan, paina __Save results__. Jos haluat ajaa generaation uudestaan, paina __Run generation__ uudestaan. Voit myös vaihtaa generoitavien sanojen määrää.

Jos haluat ajaa generaation toisella asteella tai sanapituudella, joudut painamaan __Train__ jotta muutokset tulevat voimaan.



