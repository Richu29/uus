def juurdekasv(pindala_aakrites, juurdekasv_hektari_kohta):
    pindala_hektarites = pindala_aakrites * 0.4047
    tulemus = pindala_hektarites * juurdekasv_hektari_kohta
    return round(tulemus, 2)

failinimi = input("Sisestage failinimi: ")
aastane_juurdekasv = float(input("Sisestage aastane juurdekasv hektari kohta tihumeetrites: "))
piir = float(input("Sisestage piir, mitmest aakrist suuremad metsatükid arvesse võtta: "))

arvutatud_kokku = 0

try:
    with open(failinimi, 'r', encoding='utf-8') as fail:
        for rida in fail:
            pindala = float(rida.strip())
            
            if pindala > piir:
                kogus = juurdekasv(pindala, aastane_juurdekasv)
                print(f"Metsatüki aastane juurdekasv on {kogus}")
                arvutatud_kokku += 1
            else:
                print("Metsatükki ei võeta arvesse")
                
    print(f"Arvutati {arvutatud_kokku} metsatüki juurdekasv")

except FileNotFoundError:
    print(f"Viga: Faili nimega '{failinimi}' ei leitud.")