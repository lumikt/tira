## Määrittelydokumentti

Tavoitteena on luoda Markovin ketjua hyödyntävä koneoppimisalgoritmi, joka tuottaa uusia sanoja opetusdataan perustuen. Sovellus hyödyntää itse tehtyä trie-tietorakennetta tiedon tallentamiseen. Työ tehdään pythonilla.

### Hallinnolliset tiedot  
Osaan Pythonin lisäksi jonkin verran Javascriptiä, en muita kieliä. Kuulun tietojenkäsittelytieteen kandidaatti opinto-ohjelmaan.

### Kuvaus ohjelmasta  
Uudet sanat generoidaan mielivaltaisen asteen Markovin ketjulla joka probabilistisesti arpoo aina seuraavan merkin sanaan, perustuen aikaisempiin (asteen määrittelemiin) tiloihin ja niiden sallimien merkkien todennäköisyyksien painotuksia käyttäen.

Aloittaessaan generoinnin generaattori valitsee ensimmäisen merkin tyhjästä juurisolmusta alkaen. Valinta tapahtuu arpomalla seuraava merkki, merkkien todennäköisyyksillä painotetusti sallittujen merkkien joukosta. Kun ensimmäinen merkki on valittu, siirtyy generaattori käsittelemään merkin solmua, josta se arpoo taas seuraavan merkin merkkijonoon, sallittujen merkkien joukosta. Riippuen Markovin ketjun asteesta, kyseinen solmu voi olla yksi merkki tai merkkijono (enimmillään asteen mittainen). 

Tilat tallennetaan trie-tietorakenteeseen, johon voi tallentaa mielivaltaisia merkkijonoja ja hakea seuraavan merkin mille tahansa merkkijonolle. Tietorakenteen solmuihin tallennetaan seuraavan merkin frekvenssitieto sekä lapsisolmut.

Jotta generaattorin tarvitsemat perustodennäköisyydet saadaan selville, tarvitaan harjoitusdataa. Sanageneraattorille sopii sanalista valitusta kielestä, jonka perusteella voidaan saada tarvittavat perustiedot generoinnille.

Ohjelma toimii komentorivillä, sille annetaan haluttu määrä generoitavia sanoja sekä minkä asteisella Markovin ketjulla sanoja toivotaan generoitavan. Ajon jälkeen ohjelma listaa generoidut sanat sekä tarjoaa mahdollisuuden niiden tallentamiseen tiedostona.

___Harjoitustyön ydin on sanojen generointi Markovin ketjulla opetusdataan perustuen.___

### Aikavaatimukset
Trie-haku on aikavaatimukseltaan O(N) [1] ja generaattorin aikavaatimus on polynominen riippuen sen asteesta, eli mitä enemmän asteita Markovin ketjussa, sen laajempi matriisi vaaditaan seuraavan merkin laskemiseen. Trie-tietorakenne on tehokas tallentamaan merkkijonoja mutta laajassa aineistossa se vaatii kuitenkin jonkin verran tilaa, joskin se tuskin tulee olemaan rajoite ohjelmassa.

### Lähteitä
[1] https://en.wikipedia.org/wiki/Trie  
[2] https://en.wikipedia.org/wiki/Markov_chain  
[3] https://brilliant.org/wiki/markov-chains/  
