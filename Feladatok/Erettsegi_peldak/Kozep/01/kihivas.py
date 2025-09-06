

# 1. feladat
print("Kérem a teljesített tevékenységet")
teljesitmeny = input()

# egyszerűség kedvéért azt mondjuk minden tevékenység egy változó
u = 0
g = 0
f = 0
k = 0

for karakter in teljesitmeny:
    match karakter:
        case "U":
            u += 1
        case "G":
            g += 1
        case "F":
            f += 2
        case "K":
            k += 10
# feladat 2
osszeg = u + g + f + k
print(f"A felhasználó aktivítása: {osszeg} km")

# feladat 3

# mivel a feladatban utána a jutalommal kell számolni ezért 
# egyszerűbb ha egy külön változóban tartjuk
bonusz = 0 
if u > 0 and g > 0 and f > 0 and k > 0:
    bonusz = 10
    print("Bravó! Jutalma még 10 km.")
else:
    print("Nem jár jutalom.")

# feladat 4
teljes = osszeg + bonusz
print(f"Összesen megtett {teljes} km")
if teljes >= 40:
    print("Gratulálok, kihívás teljesítve!")
else:
    print("Legközelebb sikerül!")






