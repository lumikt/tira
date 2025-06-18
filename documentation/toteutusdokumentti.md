## Toteutusdokumentti

Tämän harjoitustyön tavoitteena on sanageneraattorin toteuttaminen Markovin ketjulla sekä oman trie-rakenteen tekeminen. Tässä dokumentissa kuvataan ohjelmiston yleisrakenne sekä tiedetyt puutteet sekä parannusehdotuksia.

### Ohjelman yleisrakenne
Ohjelma on jaettu neljään päämoduuliin, datahandler, generator, trie sekä ui. Main-moduulia käytetään vain ohjelman käynnistämiseen.

Datahandlerin tehtävä on toteuttaa harjoitusdatan avaaminen tiedostosta sekä harjoitusdatan puhdistaminen erikoismerkeistä. Kun data on puhdistettu, datahandlerin process-metodi palauttaa listan sanoja, joita voidaan käyttää harjoitusdatana.

Trie-moduuli sisältää trie-tietorakenteen, jota käytetään harjoitusdatan tallentamiseen sekä sanojen generoinnin todennäköisyyksien laskemiseen. Trien tallennetaan merkkijonon osia Markovin ketjun asteen mukaisesti, aina ketjun aste + 1 pitkänä. Trie:en tallennetaan jokaisen merkkijonon esiintymiskerrat, jotta voimme laskea kuinka usein todennäköinen merkkijono on. Trie sisältää apuluokan Node joka kuvastaa yhtä solmua trie-rakenteessa.

Generator-moduuli sisältää itse sanageneraattorin sekä hoitaa trien populoimisen Markovin ketjun asteen mukaisesti. Sanageneraattori etsii aina triestä asteensa mukaisen pitkän merkkijonon ja arpoo tämän jälkeen painotetulla todennäköisyydellä seuraavan merkin sananaan. Tämän jälkeen generaattori siirtyy eteenpäin sanassa ja generoi jälleen seuraavan merkin asteensa mukaan. Merkin valinta toteutetaan random-moduulin randint-funktiolla, joka arpoo kokonaisluvun yhden ja kokonaisesiintymiskertojen määrän välillä. Jokaiselle mahdolliselle seuraajamerkille on annettu kokonaislukuväli esiintymiskertojensa mukaan, jos randint osuu tähän väliin, valitaan kyseinen merkki.

UI-moduuli on graafinen käyttöliittymä, joka sitoo yhteen ohjelman. Ainoa suora linkki on generator-moduuli joka vuorostaan sisällyttää sekä datahandler ja trie moduulit. 

### Työn puutteet
Graafinen käyttöliittymä on kohtuu rujo ja kaipaisi hieman siistimistä. Käyttäjäkokemuksen kannalta joitakin parannuksia voisi tehdä generaation parametrien ja harjoitusdatan tiedoston valinnan selkeyttämiseksi.

Sanageneraattori pystyy generoimaan vain saman pituisia sanoja eikä satunnaisen pitkiä, tai edes todennäköisen pitkiä. Generaattorin parametrit ovat kohtuu alkeellisia.

_Lisää tulossa_

### Parannusehdotuksia
Generaattorille voisi luoda useampia generointivaihtoehtoja, esim. sanan pituuteen per generointikerta. Generaatioon voisi myös luoda toiminnon, jolla saataisiin generaatio arpomaan päättymistä todennäköiseen loppumerkkijonoon, esim. jos -nen päättyiset sanat ovat kohtuu yleisiä, joka voisi parantaa generoitujen sanojen sointua.

_Lisää tulossa_

### Laajat kielimallit
Tässä työssä ei ole käytetty lainkaan laajoja kielimalleja.

### Lähteet
[1] https://en.wikipedia.org/wiki/Trie
[2] https://en.wikipedia.org/wiki/Markov_chain
[3] https://tkdocs.com/tutorial/

 

