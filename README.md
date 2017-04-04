# PTS-2
2. domaca uloha z PTS
Zadanie:
Domácu úlohu odovzdajte ako GITovský repozitár e-mailom na relatko@gmail.com. Do subjectu napiste PTS DU2. Nezabudnite napisat svoje meno. Termín na odovzdanie úlohy je 4.4.2017 23:00

Naprogramujte terminálové "Človeče nehnevaj sa!". Môžte si upraviť pravidlá. Odporúčané úpravy (zjednoduženia): po hodení 6-ky hr=ač nehádže ešte raz, po obkrúžení kolečka panáčikovia nejdu do "domčeka", ale sa točia daľej (teda domček ani neexistuje). Program taktiež nemusí byť úplne user friendly. 
Aktuálny stav hry má byť uložený ako jedna imutable premenná, a referencia na tento stav má byť v podstate jedinou "verejnou" mutovatelnou premennou v programe. To samozrejme neznamená, že v kóde nemajú byť mutable premenné, takéto premenné však majú existovať iba v lokálnom scope. 
Súčasťou odovzdaného repozitára má byť základná používateľská dokumentácia, stručný popis designu a aspoň základné testovacie programy. 
Ako si napríklad máte predstaviť terminálové človeče
Player 2 is on turn.
Dice: 4.
Player 0's pieces are on fields: 0:40 1:41 2:42 3:43
Player 1's pieces are on fields: 0:44 1:45 2:46 3:47
Player 2's pieces are on fields: 0:48 1:49 2:50 3:51
Player 3's pieces are on fields: 0:52 1:53 2:54 3:30
>pass
>throw
Player 3 is on turn.
Dice: 5.
Player 0's pieces are on fields: 0:40 1:41 2:42 3:43
Player 1's pieces are on fields: 0:44 1:45 2:46 3:47
Player 2's pieces are on fields: 0:48 1:49 2:50 3:51
Player 3's pieces are on fields: 0:52 1:53 2:54 3:30
>move 3
Player 0 is on turn.
Dice: 0.
Player 0's pieces are on fields: 0:40 1:41 2:42 3:43
Player 1's pieces are on fields: 0:44 1:45 2:46 3:47
Player 2's pieces are on fields: 0:48 1:49 2:50 3:51
Player 3's pieces are on fields: 0:52 1:53 2:54 3:35

Moj pristup:
Pocas svojho tahu hrac len vybera, ktorou figurkou chce pohnut (da sa vybrat aj figurka, ktorou by sa nemalo dat pohnut). Figurky zacinaju v domceku s oznacenim '-1'. Ostatne policka cislujem od 0 po 39, kedze bezna hracia plocha ma 40 policok. Ked sa hracovi podari hodit 6, tak si vyberie s ktorou figurkou vyjde z domceku. Podla toho ktory hrac je na tahu, sa figurka presunie na policko 0, 10, 20 alebo 30. Nasledne hrac hadze este raz. Ak padne 6 a je to prvy hracov hod, tak hrac hadze este raz. Hody sa uplatnuju v poradi, v akom boli hodene. Hraci ziskavaju body za prejdenie celeho kola. Ked sa stretnu dve figurky, prichadzajuca figurka "vykopne" figurku, ktora tam stala a tym ju vrati do domceka. Hra konci ked niektory hrac ziska 5 bodov. Stav hry sa vypisuje vzdy pri zmene hraca a nakonci pred vypisanim vitaza.

Testovany vstup:
Automaticky vstup, kazdy hrac chce pohnut len figurkou 0. Hra bezi podla predpokladov.
