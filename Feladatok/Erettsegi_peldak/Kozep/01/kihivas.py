

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









