### Viikkoraportti

Tällä viikolla en ole kerennyt tekemään kovinkaan paljoa, olen käyttänyt työhön n. 3-4 tuntia. Alustin testausdokumentin sekä lisäsin kommentit trie-moduuliin. Sekä trie että generator ovat nyt hyvässä vaiheessa, pois lukien mahdolliset generoinnin laajennukset tulevaisuudessa.

Paransin myös käyttäjäkokemusta main.py:ssä, ainoana komentoriviargumenttina annetaan harjoitusdatan nimi, jonka jälkeen ohjelma kysyy interaktiivisesti generoinnin speksit, eli asteen, sanamäärän sekä sanapituuden.

Suurimman haasteen tällä viikolla on aiheuttanut generator-luokan testaamisen laajentaminen. Tällä hetkellä testaus kattaa generoinnin parametrit, eli juuri sanan pituuden, oikean samamäärän generoinnin sekä epäsuorasti sen että generaattori ylipäätään generoi jotakin. Olen yrittänyt keksiä tapoja laajentaa testausta mutta en oikein keksi mitä tekisin. Generoinnin satunnaisuutta ei juuri ole merkityksellistä testata. Voisin ehkä lisätä testitapauksia, joissa suljetaan pois laiton generointi, eli tilanne, jossa merkkijonoa seuraisi merkki, jonka kaltaista sekvenssiä ei löydy testidatasta mutta en tiedä onko tämä mielekästä sillä, kyse on enneminkin trie-luokan toiminnosta. Toivonkin että saisin vertaisarvionnissa ideoita muilta.

Ensi viikolla ajattelin toteuttaa ehdotetun graafisen käyttöliittymän sekä laajentaa generoinnin vaihtoehtoja, esim. vaihteleva sanapituus tai mahdollisesti vaihteleva aste. Mietin myös, jos toteuttaisin vaihtoehdon, jossa tallennetaan myös ”loppumerkki” trieen ja että generointiin lisättäisiin vaihtoehto sallia satunnainen päättyminen, jolloin olisi todennäköisempää, että sanat päättyvät tavallisempiin loppumerkkeihin.

Tällä viikolla en ole oppinut mitään kovin konkreettista. Olen saanut kertausoppia siitä, että testitapausten keksiminen on välillä työlästä, varsinkin jos testattava asia ei tuota määrämittaisia outputteja.
