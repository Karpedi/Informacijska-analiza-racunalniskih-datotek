# Informacijska-analiza-racunalniskih-datotek
Računalniški program, ki izvede informacijsko analizo izbranih računalniških datotek, pri čemer predpostavljamo, da so datoteke ustvarili stacionarni diskretni informacijski viri, ki oddajajo nize 8-bitno dvojiško kodiranih znakov neke končne abecede. Takšna abeceda torej vsebuje 256 možnih različnih znakov in njihovim 8-bitnim dvojiškim kodnim zamenjavam pravimo tudi 8-bitni zlogi oz. angl. bytes.

Program odpre podano datoteko in za izbrano dolžino nizov 8-bitno kodiranih znakov izračuna entropijo stacionarnega diskretnega informacijskega vira, ki naj bi te nize oddal/ustvaril (N. Pavešić, Informacija in Kodi, Založba FE in FRI 2010, str. 46-47).


Za kontrolo svojih rezultatov pri večjih datotekah upoštevajte, da bi morali za datoteko test1.data dobiti vrednost entropije H5 približno 3,1598 bita na 8-bitni zlog.
### Rezultat
> test1.data - arhiviranje brez posebnega kodiranja <br/>
> test2.data - najhitrejše gospodarno kodiranje<br/>
> test3.data - najbolj možno gospodarno kodiranje<br/>
> test4.data - normalno gospodarno kodiranje<br/>
> test5.data - normalno gospodarno in dodatno tajno kodiranje<br/>
