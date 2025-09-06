# Feladat 1
# mivel elég sok elemet kell tárolni így a listák használata ilyenkor ajánlott

befotek = [5, 2, 2, 4, 3, 2, 4, 10, 5, 5, 3, 5, 4, 3, 3]
# Bekérés esetén a következő szintaxis ajánlott
#for i in range(15):
#    print("Kérem adja meg a következő üveg térfogatát")
#    bemenet = input()
#    befotek.append(int(bemenet)) # számra alakítás a számoláshoz

# Feladat 2
print("Feladat 2")
print("Mari néni lekvárja (dl): ")
L = int(input())
# az hogy 0 < L <= 200!  annyit biztosra mondhatunk hogy nem
# kell foglalkoznunk a negatív számokkal

osszeg = 0 # 4 feladathoz kell majd
# Feladat 3
print("Feladat 3")
legnagyobb = 0
for index, value in enumerate(befotek):
    if befotek[index] > befotek[legnagyobb]:
        legnagyobb = index    
    osszeg += value # 4 feladathoz kell majd

# legnagyobb esetében hozzáadunk plussz egyet mert 0-nál kezdjük a lista indexelését
# ezért általánosan úgy számolunk, hogy 0,1,2,3
# viszont matematikában 1,2,3,4
print(f"Legnagyobb üveg {befotek[legnagyobb]} dl és {legnagyobb + 1}. a sorban.")

# Feladat 4
print("Feladat 4")

if osszeg < L:
    print("Elegendő üveg volt.")
else:
    print("Maradt lekvár.") 
