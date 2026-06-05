def loe_seis(failinimi):
    sonastik = {}
    with open(failinimi, 'r', encoding='utf-8') as fail:
        read = fail.readlines()
        
    for rida in read[1:]:
        tükid = rida.strip().split()
        if not tükid:
            continue
        nimi = tükid[0]
        tulemused = []
        for väärtus in tükid[1:]:
            if väärtus == '-':
                tulemused.append('-')
            else:
                tulemused.append(int(väärtus))
        sonastik[nimi] = tulemused
    return sonastik

def lisa_tulemus(nimi, vooru_number, sonastik, tulemus):
    indeks = vooru_number - 1
    if sonastik[nimi][indeks] == '-':
        sonastik[nimi][indeks] = tulemus
        print("Tulemus lisatud!")
    else:
        print("Tulemus on juba varem lisatud!")
    return sonastik

def leia_skoor(nimi, sonastik):
    summa = 0
    for punkt in sonastik[nimi]:
        if punkt != '-':
            summa += punkt
    return summa

failinimi = "turniir.txt"
seis = loe_seis(failinimi)

with open(failinimi, 'r', encoding='utf-8') as fail:
    esimene_rida = fail.readline().rstrip('\n')

while True:
    print("Vali tegevus:")
    print("1 - Vaata punktitabelit")
    print("2 - Lisa tulemus")
    print("3 - Vaata skoori")
    print("4 - Leia võitja")
    print("5 - Lõpeta programmi töö")
    
    valik = input()
    
    if valik == "1":
        for nimi, tulemused in seis.items():
            tulemused_str = " ".join(str(x) for x in tulemused)
            print(f"{nimi} {tulemused_str}")
            
    elif valik == "2":
        nimi = input("Sisesta nimi: ")
        voor = int(input("Sisesta voor: "))
        punktid = int(input("Sisesta punktid: "))
        seis = lisa_tulemus(nimi, voor, seis, punktid)
        
    elif valik == "3":
        nimi = input("Sisesta nimi: ")
        skoor = leia_skoor(nimi, seis)
        print(f"{nimi} skoor on {skoor}.")
        
    elif valik == "4":
        parim_nimi = None
        parim_skoor = -1
        for nimi in seis:
            praegune_skoor = leia_skoor(nimi, seis)
            if praegune_skoor > parim_skoor:
                parim_skoor = praegune_skoor
                parim_nimi = nimi
        print(f"Suurima skooriga on {parim_nimi} ({parim_skoor} punkti).")
        
    elif valik == "5":
        with open("turniir_uus.txt", 'w', encoding='utf-8') as fail_uus:
            fail_uus.write(esimene_rida + "\n")
            for nimi, tulemused in seis.items():
                tulemused_str = " ".join(str(x) for x in tulemused)
                fail_uus.write(f"{nimi} {tulemused_str}\n")
        print("Programm lõpetas töö.")
        break