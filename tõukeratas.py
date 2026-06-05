def arvuta_hind(soiduaeg_minutites, minuti_hind):
    if soiduaeg_minutites >= 20:
        return 5.15
    else:
        tulemus = soiduaeg_minutites * minuti_hind
        return round(tulemus, 2)

minuti_hind = float(input("Sisestage minuti hind eurodes: "))
eelarve = float(input("Kui palju raha on planeeritud? "))

kokku_kulu = 0.0
paeva_number = 1

with open("min.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        if rida.strip():
            minutid = int(rida.strip())
            paeva_kulu = arvuta_hind(minutid, minuti_hind)
            print(f"{paeva_number}. päeval kulus {paeva_kulu} eurot.")
            kokku_kulu += paeva_kulu
            paeva_number += 1

kokku_kulu = round(kokku_kulu, 2)
print(f"Kokku kulus raha {kokku_kulu} eurot.")

if kokku_kulu > eelarve:
    print("Eelarve läks lõhki!")