# elöszőr kérek a usertől egy bemeneti értéket
user_input = input()

# ezután a megadott értéket átalakítom számá
# ha user szöveget adna meg akkor a program itt dob egy hibát
user_value = int(user_input)

# ha megvan mennyi szám kell akkor utána megnézzük hogy ténylegesen kell-e dolgoznunk
current_index = 0

# előre kiírjuk a 0 mert ez a speciális eset a sorozatban
print(0)

# ezután csinálunk 2 tároló helyet amiben mentjük az elöző kettő elemet
# az 1-es értéket abba a tárolóba tesszük amelyik az első összeadás során ürülni fog
cache_1 = 1
cache_2 = 0

# ha mégis a második elembe teszed akkor az egyes csak egyszer fog megjelenni
# pl:
# 0 - 1 Eredmény 1
# 1 - 1 Eredmény 2
# ...
#
# Viszont ha az elsőbe teszed akkor
# 1 - 0 Eredmény 1
# 0 - 1 Eredmény 1
# 1 - 1 Eredmény 2
# ,,,

# ezután készítűnk egy ciklust ami addig fog futni amíg elegendő számot meg nem jelenítettünk
while current_index != user_value:
    # kiszámoljuk a következő számot úgy hogy az elöző kettöt összeadjuk
    current = cache_1 + cache_2
    print(current)
    # a megjelenítést követően rendezéssel játszunk egyet
    # az első cache-nek a tartalma mindig elvesztére fogg kerülni így ennek a cserélésével kezdünk
    cache_1 = cache_2
    # majd a jelenlegi számot megadjuk a cache 2-ben
    cache_2 = current
    # végül hozzáadunk egyet a számlálohóz hogy tudjuk mennyi értéket jelenítettünk meg eddig
    current_index += 1
