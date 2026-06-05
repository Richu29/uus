def loe_tulemused(failinimi):
    sonastik = {}
    with open(failinimi, 'r', encoding='utf-8') as fail:
        for rida in fail:
            if rida.strip():
                tükid = rida.strip().split(';')
                riik = tükid[0]
                tulemused = tükid[1:]
                sonastik[riik] = tulemused
    return sonastik

def lisa_tulemus(sonastik):
    riik = input("Nimi: ")
    tulemus = input("Tulemus (W/L): ")
    if riik in sonastik:
        sonastik[riik].append(tulemus)
    else:
        sonastik[riik] = [tulemus]
    print("Tulemus lisatud!")
    return sonastik

def leia_võitude_arv(sonastik, riik):
    if riik in sonastik:
        return sonastik[riik].count('W')
    return 0

def leia_parim(sonastik):
    parim_riik = None
    maksimaalselt_voite = -1
    for riik in sonastik:
        voite = leia_võitude_arv(sonastik, riik)
        if voite > maksimaalselt_voite:
            maksimaalselt_voite = voite
            parim_riik = riik
    print(f"Parim on {parim_riik} {maksimaalselt_voite} võiduga")

seis = loe_tulemused("tulemused.txt")

while True:
    print("1 - Vaata punktitabelit")
    print("2 - Lisa tulemus")
    print("3 - Leia võitude arv")
    print("4 - Leia parim")
    print("5 - Lõpeta programmi töö")
    
    valik = input("Sisesta valik: ")
    
    if valik == "1":
        for riik, tulemused in seis.items():
            tulemused_str = " ".join(tulemused)
            print(f"{riik} {tulemused_str}")
            
    elif valik == "2":
        seis = lisa_tulemus(seis)
        
    elif valik == "3":
        riik = input("Sisesta riigi nimi: ")
        voite = leia_võitude_arv(seis, riik)
        print(voite)
        
    elif valik == "4":
        leia_parim(seis)
        
    elif valik == "5":
        with open("tulemused_uus.txt", 'w', encoding='utf-8') as fail_uus:
            for riik, tulemused in seis.items():
                tulemused_str = ";".join(tulemused)
                fail_uus.write(f"{riik};{tulemused_str}\n")
        print("Faili salvestatud! Programm lõpetas töö")
        break