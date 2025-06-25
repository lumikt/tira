## Toteutusdokumentti

Tämän harjoitustyön tavoitteena on sanageneraattorin toteuttaminen Markovin ketjulla sekä oman trie-rakenteen tekeminen. Tässä dokumentissa kuvataan ohjelmiston yleisrakenne sekä tiedetyt puutteet sekä parannusehdotuksia.

### Ohjelman yleisrakenne
Ohjelma on jaettu neljään päämoduuliin, datahandler, generator, trie sekä ui. Main-moduulia käytetään vain ohjelman käynnistämiseen.

Datahandlerin tehtävä on toteuttaa harjoitusdatan avaaminen tiedostosta sekä harjoitusdatan puhdistaminen erikoismerkeistä. Kun data on puhdistettu, datahandlerin process-metodi palauttaa listan sanoja, joita voidaan käyttää harjoitusdatana.

Trie-moduuli sisältää trie-tietorakenteen, jota käytetään harjoitusdatan tallentamiseen sekä sanojen generoinnin todennäköisyyksien laskemiseen. Trien tallennetaan merkkijonon osia Markovin ketjun asteen mukaisesti, aina ketjun aste + 1 pitkänä. Trie:en tallennetaan jokaisen merkkijonon esiintymiskerrat, jotta voimme laskea kuinka todennäköinen merkkijono on suhteessa muihin sallittuihin merkkijonoihin. Trie sisältää apuluokan Node joka kuvastaa yhtä solmua trie-rakenteessa.

Generator-moduuli sisältää itse sanageneraattorin sekä hoitaa trien populoimisen Markovin ketjun asteen mukaisesti. Sanageneraattori etsii aina triestä asteensa mukaisen pitkän merkkijonon ja arpoo tämän jälkeen painotetulla todennäköisyydellä seuraavan merkin sanaan. Tämän jälkeen generaattori siirtyy eteenpäin sanassa ja generoi jälleen seuraavan merkin asteensa mukaan. Merkin valinta toteutetaan random-moduulin randint-funktiolla, joka arpoo kokonaisluvun yhden ja sallittujen seuraajamerkkien kokonaisesiintymiskertojen määrän välillä. Jokaiselle mahdolliselle seuraajamerkille on annettu kokonaislukuväli esiintymiskertojensa mukaan, jos randint osuu tähän väliin, valitaan kyseinen merkki.

UI-moduuli on graafinen käyttöliittymä, joka sitoo yhteen ohjelman. Ainoa suora linkki on generator-moduuli joka vuorostaan sisällyttää sekä datahandler ja trie moduulit.

### Yleiskuva toiminnasta

Tilanteessa, jossa trieen tallenetaan sana "super" kahden asteen ketjulla trieen tallentuu merkit s, u, p, e, r, su, up, pe, er, sup, upe, per. Sanojen generointiin käytetään tässä tapauksessa kahta merkkiä eli jos generoitu sana on nyt muodossa "su", etsitään triestä solmu "su" ja katsotaan sen sallitut seuraajat, joita tässä tilanteessa on vain yksi, eli "sup". Valitaan siis seuraajamerkiksi "p", jatketaan generointia ja haetaan seuraavaksi merkkiä "up". Todellisessa tilanteessa, jossa on enemmän harjoitusdataa, on myös enemmän sallittuja seuraajamerkkejä, jolloin sanat ovat monimuotoisempia.

Harjoitusdatan lisääminen trieen on kohtuullisen tehokasta, jopa Kotuksen nykysuomen sanalistan lisääminen menee sujuvasti, lista sisältää 100 477 sanaa. Lisäyksen nopeus riippuu asteesta ja lisättävän sanalistan pituudesta. Mitä korkeampi aste, sen syvempi trie jolloin myös lisättäviä merkkijonoja on enemmän. 

### Työn puutteet
Graafinen käyttöliittymä on kohtuu rujo ja kaipaisi hieman siistimistä. 

Sanageneraattori pystyy generoimaan vain saman pituisia sanoja eikä satunnaisen pitkiä, tai edes todennäköisen pitkiä.

### Parannusehdotuksia
Generaattorille voisi luoda useampia generointivaihtoehtoja, esim. sanan pituuteen per generointikerta. Generaatioon voisi myös luoda toiminnon, jolla saataisiin generaatio arpomaan päättymistä todennäköiseen loppumerkkijonoon, esim. jos -nen päätyiset sanat ovat kohtuu yleisiä, joka voisi parantaa generoitujen sanojen sointua. 

Käyttäjäkokemuksen kannalta joitakin parannuksia voisi tehdä generaation parametrien ja harjoitusdatan tiedoston valinnan selkeyttämiseksi, esim. nappien aktivointi vasta kun vaaditut ennakkotoimenpiteet on tehty. Lisäksi jonkinlainen etenemispalkki opetusta odottaessa voisi olla mielekäs isommille datamäärille.

### Laajat kielimallit
Tässä työssä ei ole käytetty lainkaan laajoja kielimalleja.

### Lähteet
[1] https://en.wikipedia.org/wiki/Trie  
[2] https://en.wikipedia.org/wiki/Markov_chain  
[3] https://tkdocs.com/tutorial/  

 

