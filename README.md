METS;TURNIIR;TONT -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
METS;TURNIIR;TONT -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
METS;TURNIIR;TONT -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Ülesanne 1. Saja Aakri mets (40 p)
Saja Aakri metsa elaniku karupoeg Puhhi fännidest metsaomanikud on oma metsatükkide pindalad kirjutanud
aakrites (1 aaker = 0,4047 hektarit). Igal omanikul on ainult ühe puuliigi metsad. Konkreetsete puuliikide puhul
on teada aastane metsa juurdekasv hektari kohta tihumeetrites (tm/ha). Näiteks kase puhul võib see olla 4,8
tm/ha, kuuse puhul 6,6 tm/ha, männi puhul 3,7 tm/ha. Omanik tahab teada, mitu tihumeetrit metsa aastas
teatud suurusest suuremates metsatükkides juurde kasvab.
Koostada funktsioon juurdekasv, mis
● võtab argumentideks metsatüki pindala (ujukomaarv aakrites) ja metsa aastase juurdekasvu hektari
kohta (ujukomaarv),
● tagastab selle pindalaga metsatüki aastase juurdekasvu ümardatuna sajandikeni.
Näide funktsiooni juurdekasv tööst
>>> juurdekasv(3.78, 6.6)
10.1

Koostada programm, mis
● küsib kasutajalt
○ failinime (failis on eraldi ridadel metsatükkide pindalad aakrites);
○ vastava puuliigi aastase juurdekasvu hektari kohta tihumeetrites (ujukomaarv);
○ piiri, mitmest aakrist suuremad metsatükid arvesse võtta (ujukomaarv);
● loeb failist metsatükkide pindalad;
● arvutab (funktsiooni
juurdekasv
abil) ja väljastab metsatüki aastase juurdekasvu, kui selle metsatüki pindala on sisestatud piirist
suurem;
● väljastab teate “Metsatükki ei võeta arvesse”, kui metsatüki pindala ei ole sisestatud piirist suurem;
● väljastab lõpuks ekraanile, mitme metsatüki juurdekasv arvutati.
Näide faili andmed.txt sisust
0.9
3.78
2.05
1.58

Näide programmi tööst (kasutaja sisend on paksus kirjas)
Sisestage failinimi: andmed.txt
Sisestage aastane juurdekasv hektari kohta tihumeetrites: 6.6
Sisestage piir, mitmest aakrist suuremad metsatükid arvesse võtta: 2
Metsatüki aastane juurdekasv on 10.1
Metsatüki aastane juurdekasv on 5.48
Metsatükki ei võeta arvesse
Arvutati 2 metsatüki juurdekasv

Ülesanne 2. Turniir (15 p)
Koosta programm turniiri läbiviimiseks. Osalejate nimed on failis turniir.txt. Esimesel real on
tühikutega eraldatud voorude numbrid (esimese rea alguses on viis tühikut järjest) ja igal järgneval
real on osaleja nimi ja voorude punktide arvud, mis on samuti eraldatud tühikutega. Kui osaleja ei
ole mõnes voorus veel sooritust teinud, on numbri asemel kriips. Osalejate ja voorude arv ei ole
ette teada, s.t programm peab töötama ka siis, kui osalejaid ja/või voore on vähem või rohkem.
Näide faili turniir.txt sisust
1 2 3 4 5 6
Mari 2 4 5 - 1 4
Juku 1 3 2 7 8 -
Malle - 2 - 3 2 5
Kalle 4 6 - - 2 -
Kirjuta funktsioon loe_seis, mis võtab argumendiks failinime ja tagastab sõnastiku, mille
võtmeteks on turniiril osalejate nimed ja väärtusteks voorude tulemuste järjendid (punktid on
järjendites andmetüübilt täisarvud).
Näide funktsiooni loe_seis tööst
>>> loe_seis("turniir.txt")
{'Mari': [2, 4, 5, '-', 1, 4], 'Juku': [1, 3, 2, 7, 8, '-'], 'Malle':
['-', 2, '-', 3, 2, 5], 'Kalle': [4, 6, '-', '-', 2, '-']}
Koosta funktsioon lisa_tulemus kindla vooru punktide salvestamiseks. Funktsioon võtab
argumentideks osaleja nime, vooru järjekorranumbri (täisarv), sõnastiku ja lisatava tulemuse
(täisarv). Kui sellel osalejal vastavas voorus veel tulemust ei ole, asendab funktsioon
lisa_tulemus vastava kriipsu sõnastikus tulemusega ning väljastab teate, et tulemus on lisatud.
Kui osalejal on selle vooru tulemus juba olemas, väljastab funktsioon selle kohta teate ja ei muuda
midagi. Funktsioon tagastab sõnastiku uue seisu.
Näide funktsiooni lisa_tulemus tööst eelpool toodud sõnastikuga
>>> lisa_tulemus("Mari", 3, sõnastik, 0)
Tulemus on juba varem lisatud!
{'Mari': [2, 4, 5, '-', 1, 4], 'Juku': [1, 3, 2, 7, 8, '-'], 'Malle':
['-', 2, '-', 3, 2, 5], 'Kalle': [4, 6, '-', '-', 2, '-']}
>>> lisa_tulemus("Mari", 4, sõnastik, 2)
Tulemus lisatud!
{'Mari': [2, 4, 5, 2, 1, 4], 'Juku': [1, 3, 2, 7, 8, '-'], 'Malle':
['-', 2, '-', 3, 2, 5], 'Kalle': [4, 6, '-', '-', 2, '-']}
Koosta funktsioon leia_skoor, mis võtab argumentideks osaleja nime ja sõnastiku ning tagastab
selle osaleja punktisumma.

Näide funktsiooni leia_skoor tööst eelpool toodud sõnastikuga
>>> leia_skoor("Malle", sõnastik)
12

Koosta põhiprogramm, kus kasutaja saab valida erinevate tegevuste vahel. Pärast iga tegevust
küsib programm uuesti, mida kasutaja soovib teha, kuni ta valib programmi töö lõpetamise. Kui
kasutaja sisestab
● “1”, kuvab programm kõigi osalejate tulemused (ühe inimese tulemused ühel real
eraldatuna tühikutega)
● “2”, lisab programm osaleja tulemuse järgmiste sammude abil:
○ küsib nime
○ küsib vooru numbrit
○ küsib tulemust
○ lisab tulemuse ja väljastab sellest teate, kasutades funktsiooni lisa_tulemus.
Kui tulemus on juba olemas, väljastab funktsioon selle kohta teate.

● “3”, küsib programm osaleja nime ja leiab funktsiooni leia_skoor kasutades selle osaleja
skoori (punktisumma) ning väljastab tulemuse sobival kujul ekraanile (vt näiteid).
● “4”, leiab programm suurima skooriga osaleja ja väljastab tema nime ja punktisumma
● “5”, teeb programm järgmised sammud:
○ salvestab turniiritabeli uue seisu esialgse failiga samal kujul faili turniir_uus.txt
○ väljastab lõpetamise kohta teate
○ lõpetab töö

Näide programmi tööst (kasutaja sisend on paksus kirjas)
Vali tegevus:
1 - Vaata punktitabelit
2 - Lisa tulemus
3 - Vaata skoori
4 - Leia võitja
5 - Lõpeta programmi töö
1
Mari 2 4 5 - 1 4
Juku 1 3 2 7 8 -
Malle - 2 - 3 2 5
Kalle 4 6 - - 2 -
Vali tegevus:
1 - Vaata punktitabelit
2 - Lisa tulemus
3 - Vaata skoori
4 - Leia võitja
5 - Lõpeta programmi töö
2
Sisesta nimi: Mari
Sisesta voor: 4
Sisesta punktid: 2
Tulemus lisatud!
Vali tegevus:

1 - Vaata punktitabelit
2 - Lisa tulemus
3 - Vaata skoori
4 - Leia võitja
5 - Lõpeta programmi töö
1
Mari 2 4 5 2 1 4
Juku 1 3 2 7 8 -
Malle - 2 - 3 2 5
Kalle 4 6 - - 2 -
Vali tegevus:
1 - Vaata punktitabelit
2 - Lisa tulemus
3 - Vaata skoori
4 - Leia võitja
5 - Lõpeta programmi töö
3
Sisesta nimi: Mari
Mari skoor on 18.
Vali tegevus:
1 - Vaata punktitabelit
2 - Lisa tulemus
3 - Vaata skoori
4 - Leia võitja
5 - Lõpeta programmi töö
4
Suurima skooriga on Juku (21 punkti).
Vali tegevus:
1 - Vaata punktitabelit
2 - Lisa tulemus
3 - Vaata skoori
4 - Leia võitja
5 - Lõpeta programmi töö
5
Programm lõpetas töö.

Pärast programmi töö lõppu peaks faili turniir_uus.txt sisu olema:
1 2 3 4 5 6
Mari 2 4 5 2 1 4
Juku 1 3 2 7 8 -
Malle - 2 - 3 2 5
Kalle 4 6 - - 2 -

Ülesanne 3. Tondid Tartus (5 p)
Loo klass nimega Tont, millel on isendiväljad nimi (sõne), vanus (täisarv) ja elukoht (sõne).
Loo klassi konstruktor, mis võtab argumendiks nime, vanuse ja elukoha ning määrab vastavad
isendiväljade väärtused. Lisaks loo klassile Tont isendimeetod kummita, mis ei võta argumente
ja väljastab ekraanile kummitamise tondi nimega ja tema elukohaga. Samuti lisa klassile meetod
__str__, mis tagastab isendiväljade info kujul "Nimi: [nimi], vanus: [vanus], elukoht: [elukoht]".
Lisaks loo klassile Tont alamklass Võlur, millel on lisaks isendimeetod nõiu, mis võtab
argumendiks nõiutava isendi ja väljastab nõidumist sisaldava sõne võluri nimega ja nõiduse
saanud isendi nimega.
Lõpuks loo kolm tonti:
1. tont nimega Norbert, 31-aastane, elukoht Tartu;
2. võlur nimega Harry, 17-aastane, elukoht Tartu;
3. võlur nimega Snape, 35-aastane, elukoht Tartu.
Loo põhiprogramm, kus ekraanile kuvatakse tontide info, kus Norbert kummitab ja Harry nõiub
Snape’i.
Näide programmi tööst
Nimi: Norbert, vanus: 31, elukoht: Tartu
Norbert kummitab elukohas Tartu!
Nimi: Harry, vanus: 17, elukoht: Tartu
Nimi: Snape, vanus: 35, elukoht: Tartu
Harry pani nõiduse, millega sai pihta Snape!

RAAMATUD; PUNKTID; MAADLEJAD -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
RAAMATUD; PUNKTID; MAADLEJAD -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
RAAMATUD; PUNKTID; MAADLEJAD -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Ülesanne 1. Raamatud (40 p)
Triin loeb raamatuid. Suure kirjasuurusega raamatu puhul loeb ta ühe lehekülje 20 sekundiga, keskmise
kirjasuurusega raamatu puhul 30 sekundiga ja väikese kirjasuurusega raamatu puhul 40 sekundiga.
Raamatute lehekülgede arvud (täisarvuna) on failis leheküljed.txt paigutatuna eraldi ridadele. Ridade arv failis
ei ole teada.
Näide faili leheküljed.txt sisust
100
350
180
90
Koosta funktsioon lugemise_aeg, mis võtab argumentideks raamatu lehekülgede arvu (täisarvuna) ja
kirjasuuruse (sõnena “suur”, “keskmine” või “väike”) ning tagastab raamatu lugemiseks kuluva aja sekundites.
Näide funktsiooni lugemise_aeg rakendamisest
>>> lugemise_aeg(350, "väike")
14000
>>> lugemise_aeg(90, "suur")
1800

Koosta programm, mis
● küsib kasutajalt faili nime;
● loeb sellest failist lehekülgede arvud;
● küsib kasutajalt iga raamatu kirjasuuruse kohta (sõnena);
● arvutab iga raamatu lugemisele kuluva aja vastavalt lehekülgede arvule ja kirjasuurusele, kasutades
funktsiooni lugemise_aeg;
● Leiab ja väljastab ekraanile, kui palju aega (mitu tundi, minutit ja sekundit) kulub kokku raamatute
lugemiseks.
Näide programmi tööst (kasutaja sisend on paksus kirjas)
Sisesta faili nimi: leheküljed.txt
Raamat on 100 lk. Kui suur on kirjastiil? keskmine
Raamat on 350 lk. Kui suur on kirjastiil? väike
Raamat on 180 lk. Kui suur on kirjastiil? keskmine
Raamat on 90 lk. Kui suur on kirjastiil? suur
Kokku kulub raamatute lugemiseks 6 tundi, 43 minutit ja 20 sekundit.

Ülesanne 2. Korvpallipunktid (15 p)
Koosta programm korvpallipunktide kohta. Korvpallimängijate nimed on failis punktid.txt. Igal real on osaleja
nimi ja mängudes visatud punktide arvud, mis on eraldatud tühikutega. Osalejate ja mängude arv ei ole ette
teada, s.t programm peab töötama ka siis, kui osalejaid ja/või mänge on vähem või rohkem.
Näide faili punktid.txt sisust
Luka 60 35 51 39 31
Joel 35 48 37 16 42
Giannis 27 45 43 55 30
Shai 44 28 28 14 33

Kirjuta funktsioon loe_seis, mis võtab argumendiks faili nime ja tagastab sõnastiku, mille võtmeteks on
korvpallurite nimed ja väärtusteks visatud punktide järjendid (punktid on järjendites andmetüübilt täisarvud).
Näide funktsiooni loe_seis tööst
>>> loe_seis("punktid.txt")
{'Luka': [60, 35, 51, 39, 31], 'Joel': [35, 48, 37, 16, 42], 'Giannis':
[27, 45, 43, 55, 30], 'Shai': [44, 28, 28, 14, 33]}
Koosta funktsioon lisa_tulemus punktide lisamiseks. Funktsioon võtab argumentideks osaleja nime,
sõnastiku ja lisatava tulemuse (täisarv). Kui vastav osaleja on olemas, siis funktsioon lisab osalejale vastavad
punktid, väljastab ekraanile teksti “Tulemus lisatud!” ja tagastab sõnastiku uue seisu. Kui sellist osalejat pole,
siis väljastab ekraanile “Sellist korvpallurit pole sõnastikus!” ja tagastab sõnastiku.
Näide funktsiooni lisa_tulemus tööst eelpool toodud failist loetud sõnastikuga
>>>lisa_tulemus("Michael", sõnastik, 30)
Sellist korvpallurit pole sõnastikus!
{'Luka': [60, 35, 51, 39, 31], 'Joel': [35, 48, 37, 16, 42], 'Giannis':
[27, 45, 43, 55, 30], 'Shai': [44, 28, 28, 14, 33}
>>> lisa_tulemus("Shai", sõnastik, 30)
Tulemus lisatud
{'Luka': [60, 35, 51, 39, 31], 'Joel': [35, 48, 37, 16, 42], 'Giannis':
[27, 45, 43, 55, 30], 'Shai': [44, 28, 28, 14, 33, 30]}
Koosta funktsioon leia_keskmine, mis võtab argumentideks osaleja nime ja sõnastiku ning tagastab selle
korvpalluri keskmise punktisumma.
Näide funktsiooni leia_keskmine tööst eelpool toodud failist loetud sõnastikuga
>>> leia_keskmine("Joel", sõnastik)
35.6

Koosta funktsioon leia_parim, mis võtab argumendiks sõnastiku ning leiab funktsiooni leia_keskmine
kasutades parima keskmise punktisummaga korvpalluri ning väljastab ekraanile nii selle korvpalluri nime kui
ka keskmise punktisumma.
Näide funktsiooni leia_parim tööst eelpool toodud sõnastikuga
>>> leia_parim(sõnastik)
Parim on Luka tulemusega 43.2

Koosta põhiprogramm, kus kasutaja saab valida erinevate tegevuste vahel. Pärast iga tegevust küsib
programm uuesti, mida kasutaja soovib teha, kuni ta valib programmi töö lõpetamise. Kui kasutaja sisestab
● “1”, kuvab programm kõigi korvpallurite tulemused (ühe inimese tulemused ühel real eraldatuna
tühikutega).
● “2”, lisab programm osaleja tulemuse järgmiste sammude abil:
○ küsib korvpalluri nime
○ küsib tulemust
○ lisab tulemuse ja väljastab selle kohta teate, kasutades funktsiooni lisa_tulemus. Kui sellist
korvpallurit pole, väljastab funktsioon vastava teate.

● “3”, küsib programm korvpalluri nime ja leiab funktsiooni leia_keskmine kasutades selle korvpalluri
keskmise punktisumma ning väljastab tulemuse sobival kujul ekraanile (vt näiteid).
● “4”, leiab programm kasutades funktisooni leia_parim suurima keskmise punktisummaga korvpalluri
ja väljastab tema nime ja keskmise punktisumma ekraanile.
● “5”, teeb programm järgmised sammud:
○ salvestab punktitabeli uue seisu esialgse failiga samal kujul faili punktid_uus.txt
○ väljastab lõpetamise kohta teate “Faili salvestatud. Programm lõpetas töö.”
○ lõpetab töö

Näide programmi tööst (kasutaja sisend on paksus kirjas)
1 - Vaata punktitabelit
2 - Lisa tulemus
3 - Leia korvpalluri keskmine
4 - Leia parim
5 - Lõpeta programmi töö
Vali tegevus: 1
Luka 60 35 51 39 31
Joel 35 48 37 16 42
Giannis 27 45 43 55 30
Shai 44 28 28 14 33
Vali tegevus: 2
Sisesta nimi: Shai
Sisesta punktid: 30
Tulemus lisatud!
Vali tegevus: 1
Luka 60 35 51 39 31
Joel 35 48 37 16 42
Giannis 27 45 43 55 30
Shai 44 28 28 14 33 30
Vali tegevus: 3
Sisesta nimi: Joel
Mängija Joel keskmine skoor on 35.6
Vali tegevus: 4
Parim on Luka tulemusega 43.2
Vali tegevus: 5
Faili salvestatud. Programm lõpetas töö
Pärast programmi töö lõppu peaks faili punktid_uus.txt sisu olema:
Luka 60 35 51 39 31
Joel 35 48 37 16 42
Giannis 27 45 43 55 30
Shai 44 28 28 14 33 30

Ülesanne 3. Maadlejad (5 p)
Loo klass nimega Sportlane, millel on isendiväljad nimi (sõne) ja kaal (täisarv). Loo klassi konstruktor, mis
võtab argumentideks nime ja kaalu ning määrab vastavad isendiväljade väärtused.
Lisa klassile Sportlane meetod __str__, mis tagastab isendiväljade info kujul “Nimi: [nimi], kaal: [kaal]”.
Loo klassile Sportlane alamklass Maadleja, mis kasutab ülemklassi konstruktorit ja lisaks on isendiväli
kaalukategooria (sõne), mis saab vaikimisi väärtuseks kaalukategooria vastavalt kaalule:
1. kärbeskaal kuni 55 kg (kaasaarvatud),
2. kergekaal kuni 66 kg (kaasaarvatud),
3. keskkaal kuni 84 kg (kaasaarvatud),
4. poolraskekaal kuni 96 kg (kaasaarvatud),
5. raskekaal üle 96 kg.
Klassil Maadleja on meetod muuda_kaalu, mis võtab argumendiks uue kaalu (täisarvu) ja uuendab
vastavalt isendimuutujate kaal ja kaalukategooria väärtusi.
Lisa klassile Maadleja meetod __str__, mis tagastab isendiväljade info kujul “Nimi: [nimi], kaal: [kaal] kg,
kaalukategooria: [kaalukategooria]”.
Lõpuks loo kolm isendit:
1. Sportlane nimega Indrek, kaaluga 105 kg;
2. Maadleja nimega Georg, kaaluga 83 kg;
3. Maadleja nimega Kristjan, kaaluga 115 kg.
Loo põhiprogramm, kus ekraanile kuvatakse sportlaste info.
Seejärel muudetakse meetodit muuda_kaalu rakendades Kristjani kaaluks 95 kg.
Programmi lõpus väljastatakse Kristjani info uuesti ekraanile.
Näide programmi tööst
Nimi: Indrek, kaal: 105 kg
Nimi: Georg, kaal: 83 kg, kaalukategooria: keskkaal
Nimi: Kristjan, kaal: 115 kg, kaalukategooria: raskekaal
Nimi: Kristjan, kaal: 95 kg, kaalukategooria: poolraskekaal
Eksamitöö esitamine
1. Töö esitamiseks sulge Thonny ning käivita uuesti.
2. Esita programmid Moodle'is lingi alt 1., 2. ja 3. ülesande esitamine.
3. Eksami ajal tekkinud logifailid (Tools → Export usage logs...) esita Moodle'is lingi alt Eksami logide esitamine.

TÕUKERATAS;JÄÄHOKI;RAAMATUD -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
TÕUKERATAS;JÄÄHOKI;RAAMATUD -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
TÕUKERATAS;JÄÄHOKI;RAAMATUD -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Ülesanne 1. Elektritõukeratas (40 p)
Mari plaanib hakata ilmade soojenedes sõitma elektritõukerattaga. Plaan on sõita sellega kooli, trenni ja
sõpradele külla. Kuna ta ei tea, kui palju see kõik nädalas maksma läheb, siis otsustas ta kirjutada programmi,
mis arvutaks välja, kui palju elektritõukeratta kasutamine maksma läheb.
Selleks kirjutas ta faili min.txt, mitu minutit (täisarv) tal iga päev vaja sõita on (ridade arv failis ei ole teada):
12
28
35
19
20
Koosta funktsioon arvuta_hind, mille argumentideks on sõiduaeg minutites (täisarv) ja minuti hind
(ujukomaarv) eurodes. Funktsioon arvutab sõiduhinna (ujukomaarv) ümardatult kaks kohta pärast koma.
Arvestama peab ka seda, et kui sõit on 20 minutit või pikem, siis maksab sõit kokku 5 eurot ja 15 senti.
Näide funktsiooni arvuta_hind tööst:
>>> arvuta_hind(12, 0.25)
3.0
>>> arvuta_hind(22, 0.25)
5.15
Koosta programm, mis
1. Küsib kasutajalt, kui palju üks minut elektritõukerattaga sõitmist maksab.
2. Küsib, kui palju raha on Maril planeeritud sellel nädalal elektritõukerattale.
3. Arvutab funktsiooni arvuta_hind kasutades iga päeva kohta sõidule kuluva raha ja väljastab selle
info ekraanile, lisades ka päeva järjekorranumbri.
4. Leiab, kui palju raha elektritõukerattale nädalas kokku kulub ja väljastab selle summa ekraanile
(eurodes ümardatuna kaks kohta pärast koma).
5. Kui kulub rohkem raha, kui Mari on elektritõukerattale planeerinud, siis kuvab ekraanile teate “Eelarve
läks lõhki!”.
Näide programmi tööst eelneva failiga min.txt (kasutaja sisestused on paksus kaldkirjas):
Sisestage minuti hind eurodes: 0.25
Kui palju raha on planeeritud? 20
1. päeval kulus 3.0 eurot.
2. päeval kulus 5.15 eurot.
3. päeval kulus 5.15 eurot.
4. päeval kulus 4.75 eurot.
5. päeval kulus 5.15 eurot.
Kokku kulus raha 23.2 eurot.
Eelarve läks lõhki!

Ülesanne 2. Jäähoki MM (15 p)
Koosta programm jäähoki maailmameistrivõistluste tulemuste kohta. Jäähokikoondiste riikide (ingliskeelsed)
nimed ja mängude tulemused on failis tulemused.txt. Igal real on riigi nimi ja mängude tulemused
eraldatuna semikooloniga. “W” tähistab võitu ja “L” kaotust. Riikide ja mängude arv ei ole ette teada,
programm peab töötama ka siis, kui riike ja/või mänge on vähem või rohkem.
Näide faili tulemused.txt sisust
Canada;W;W;W
Switzerland;W;W;L
Czech Republic;W;L;L
Kirjuta funktsioon loe_tulemused, mis võtab argumendiks faili nime ja tagastab sõnastiku, mille võtmeteks
on riikide nimed ja väärtusteks mängude tulemuste järjend, kus iga järjendi element on sõne “W” või “L”.
Näide funktsiooni loe_tulemused tööst eelneva tekstifailiga
>>> loe_tulemused("tulemused.txt")
{'Canada': ['W', 'W', 'W'], 'Switzerland': ['W', 'W', 'L'], 'Czech
Republic': ['W', 'L', 'L']}
Koosta funktsioon lisa_tulemus mängutulemuse lisamiseks. Funktsioon võtab argumendiks sõnastiku.
Funktsioonis küsitakse riigi nime (sõne) ja kas võitis (W) või kaotas (L). Kui sellenimeline riik on sõnastikus,
siis lisatakse tulemus vastavale riigile juurde. Kui sellist riiki ei ole, siis luuakse sellenimeline riik ja lisatakse
talle tulemus. Programm väljastab ekraanile teksti “Tulemus lisatud!” Funktsioon tagastab sõnastiku uue seisu.
Näited funktsiooni lisa_tulemus tööst eelpool toodud failist loetud sõnastikuga
>>>lisa_tulemus(sõnastik)
Nimi: Canada
Tulemus(W/L): W
Tulemus lisatud!
{'Canada': ['W', 'W', 'W', 'W'], 'Switzerland': ['W', 'W', 'L'], 'Czech
Republic': ['W', 'L', 'L']}
>>>lisa_tulemus(sõnastik)
Nimi: Finland
Tulemus (W/L): L
Tulemus lisatud!
{'Canada': ['W', 'W', 'W'], 'Switzerland': ['W', 'W', 'L'], 'Czech
Republic': ['W', 'L', 'L'], 'Finland': ['L']}
Koosta funktsioon leia_võitude_arv, mis võtab argumentideks sõnastiku ja riigi nime ning tagastab selle
riigi võitude arvu, kus võit (W) annab 1 võidupunkti ja kaotus (L) 0 võidupunkti.
Näide funktsiooni leia_võitude_arv tööst eelpool toodud failist loetud sõnastikuga
>>> leia_võitude_arv(sõnastik, "Switzerland")
2
Koosta funktsioon leia_parim, mis võtab argumendiks eelpool kirjeldatud sõnastiku ning leiab funktsiooni
leia_võitude_arv kasutades suurima võitude arvuga riigi ning väljastab ekraanile nii selle riigi ingliskeelse
nime kui ka võitude arvu.
Näide funktsiooni leia_parim tööst eelpool toodud sõnastikuga
>>> leia_parim(sõnastik)
Parim on Canada 3 võiduga

Koosta põhiprogramm, kus kasutaja saab valida erinevate tegevuste vahel. Pärast igat tegevust küsib
programm uuesti, mida kasutaja soovib teha, kuni ta valib programmi töö lõpetamise. Kui kasutaja sisestab:
● “1”, kuvab programm kõigi riikide tulemused (ühe riigi tulemused ühel real eraldatuna tühikutega).
● “2”, lisab programm riigi tulemuse, kasutades funktsiooni lisa_tulemus järgmiste sammude abil:
○ küsib riigi ingliskeelset nime
○ küsib tulemust
○ lisab sõnastikku riigile juurde tulemuse. Kui sellist riiki pole, siis lisatakse sõnastikku uus riik
vastava tulemusega. Programm väljastab teate tulemuse lisamisest.

● “3”, küsib programm funktsiooni leia_võitude_arv kasutades riigi nime ning väljastab ekraanile
selle riigi võitude arvu.
● “4”, leiab programm funktisooni leia_parim kasutades suurima võitude arvuga riigi ja väljastab selle
riigi nime ja võitude arvu ekraanile.
● “5”, teeb programm järgmised sammud:
○ salvestab punktitabeli uue seisu esialgse failiga samal kujul faili tulemused_uus.txt
○ väljastab lõpetamise kohta teate “Faili salvestatud! Programm lõpetas töö”
○ lõpetab töö.

Näide programmi tööst (kasutaja sisend on paksus kirjas)
1 - Vaata punktitabelit
2 - Lisa tulemus
3 - Leia võitude arv
4 - Leia parim
5 - Lõpeta programmi töö
Sisesta valik: 1
Canada W W W
Switzerland W W L
Czech Republic W L L
Sisesta valik: 2
Nimi: Finland
Tulemus (W/T): L
Tulemus lisatud!
Sisesta valik: 1
Canada W W W
Switzerland W W L
Czech Republic W L L
Finland L
Sisesta valik: 3
Sisesta riigi nimi: Switzerland
2
Sisesta valik: 4
Parim on Canada 3 võiduga
Sisesta valik: 5
Faili salvestatud! Progamm lõpetas töö
Pärast programmi töö lõppu peaks faili tulemused_uus.txt sisu olema:
Canada;W;W;W
Switzerland;W;W;L
Czech Republic;W;L;L
Finland;L

Ülesanne 3. Lasteraamatud (5 p)
Loo klass nimega Raamat, millel on isendiväljad pealkiri (sõne) ja autor (sõne). Loo klassi konstruktor, mis
võtab argumentideks raamatu pealkirja ja autori ning määrab vastavad isendiväljade väärtused.
Lisa klassile Raamat meetod __str__, mis tagastab isendiväljade info kujul:
“Raamatu [pealkiri] autor on [autor]”.
Loo klassile Raamat alamklass Lasteraamat. Loo klassi konstruktor, mis võtab lisaks raamatu pealkirjale ja
autorile argumentideks raamatu soovitusliku miinimumvanuse (täisarv) ja maksimumvanuse (täisarv). Näiteks
kui raamatu soovituslik vanus on 10-12 aastastele, siis antakse saavad need argumendid väärtuse 10 ja 12.
Seejärel konstruktor määrab vastavate isendiväljade väärtused kasutades ka ülemklassi konstruktorit.
Loo klassile Lasteraamat meetod muuda_soovituslikku_vanust, mis võtab kaks argumenti ja uuendab
vastavalt isendimuutujate soovitusliku miinimumvanuse ja maksimumvanuse väärtuse. Ekraanile väljastatakse
kiri “Soovituslik vanus muudetud!”.
Lisa klassile Lasteraamat meetod __str__, mis tagastab isendiväljade info kujul
“Lasteraamatu [pealkiri] autor on [autor], soovituslik vanus [miinimumvanus]-[maksimumvanus]”
(vt allpool näidet programmi tööst).
Lõpuks loo kolm isendit:
1. Raamat pealkirjaga “Rehepapp”, autor Andrus Kivirähk;
2. Lasteraamat pealkirjaga “Karneval ja kartulisalat”, autor Andrus Kivirähk ja soovituslik
vanus 10-12 aastat;
3. Lasteraamat pealkirjaga “Sipsik”, autor Eno Raud ja soovituslik vanus 10-12 aastat.
Programmi lõpus:
1. Väljasta ekraanile raamatu ja lasteraamatute info.
2. Muuda meetodit muuda_soovituslikku_vanust rakendades raamatu “Sipsik” soovituslikuks
vanuseks 7-9.
3. Väljasta raamatu “Sipsik” uuendatud info ekraanile.
Näide programmi tööst
Raamatu "Rehepapp" autor on Andrus Kivirähk
Lasteraamatu "Karneval ja kartulisalat" autor on Andrus Kivirähk, soovituslik vanus: 10-12
Lasteraamatu "Sipsik" autor on Eno Raud, soovituslik vanus 10-12
Soovituslik vanus muudetud!
Lasteraamatu "Sipsik" autor on Eno Raud, soovituslik vanus 7-9



