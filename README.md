# Informacijska-analiza-racunalniskih-datotek
Računalniški program, ki izvede informacijsko analizo izbranih računalniških datotek, pri čemer predpostavljamo, da so datoteke ustvarili stacionarni diskretni informacijski viri, ki oddajajo nize 8-bitno dvojiško kodiranih znakov neke končne abecede. Takšna abeceda torej vsebuje 256 možnih različnih znakov in njihovim 8-bitnim dvojiškim kodnim zamenjavam pravimo tudi 8-bitni zlogi oz. angl. bytes.

Program odpre podano datoteko in za izbrano dolžino nizov 8-bitno kodiranih znakov izračuna entropijo stacionarnega diskretnega informacijskega vira, ki naj bi te nize oddal/ustvaril (N. Pavešić, Informacija in Kodi, Založba FE in FRI 2010, str. 46-47).

Za izračun entropije je potrebno izvesti statistično analizo pogostosti pojavljanje vseh posameznih možnih n-členih nizov osem-bitnih zlogov, pri čemer n označuje predpostavljeno dolžino oddanih nizov znakov.

Po izdelavi programa študenti izvedejo statistično analizo različnih vrst poljubno izbranih datotek, od besedilnih, programskih, medijskih itd. V kratkem poročilu podajo rezultate analize v smislu vrednosti izračunanih entropij za različne primere datotek in za različne vrednosti n in to najmanj za n = 3. Za vseh pet točk morajo študenti podati vse izračune entropije za do n = 5. Pridobljene rezultate komentirajo glede na to, kaj jim izračunana vrednost entropije pove o vsebini analiziranih datotek.

Preizkusne datoteke
Program študenti obvezno preizkusijo še na preizkusnih datotekah (v dodatnem gradivu), ki so bile ustvarjene s klasičnim arhivskim programom za gospodarno in tajno kodiranje iz iste osnovne datoteke (slovenska besedila) na različne možne načine.

Obstajata dve različičici omenjenih datoteke. Manjše datoteke z oznako 's' vsebujejo 10 miljonov in tiste brez te oznake oznake 50 miljonov 8-bitnih zlogov. Za kontrolo svojih rezultatov naj študenti upoštevajo, da bi morali za datoteko test2s.data dobiti vrednost entropije H4 približno 5,8127 bita na 8-bitni zlog.

Za kontrolo svojih rezultatov pri večjih datotekah upoštevajte, da bi morali za datoteko test1.data dobiti vrednost entropije H5 približno 3,1598 bita na 8-bitni zlog.
### Rezultat
> test1.data - arhiviranje brez posebnega kodiranja <br/>
> test2.data - najhitrejše gospodarno kodiranje<br/>
> test3.data - najbolj možno gospodarno kodiranje<br/>
> test4.data - normalno gospodarno kodiranje<br/>
> test5.data - normalno gospodarno in dodatno tajno kodiranje<br/>
