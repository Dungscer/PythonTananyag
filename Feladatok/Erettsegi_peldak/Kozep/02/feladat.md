# Befőzés

Mari néni eperlekvárt főz be. Sorba állította a kamrából előhozott, elmosott üres üvegeket,
hogy megtöltse őket. Tudja, hogy az egyes üvegek hány deciliteresek.

Készítsen programot, amely elemzi a befőzött lekvár mennyiségének és az adott sorrendű
üvegek térfogatának ismertében a lekvártöltési adatokat!

Az üvegek száma 15, és az űrtartalmuk deciliterben rendre a következő: 

    5, 2, 2, 4, 3, 2, 4, 10, 5, 5, 3, 5, 4, 3, 3

A program forráskódját mentse befozes néven! A program megírásakor a felhasználó által
megadott adatok helyességét, érvényességét nem kell ellenőriznie, és feltételezheti, hogy
a rendelkezésre álló adatok a leírtaknak megfelelnek. A programnak akkor is helyesen kell
működnie, ha más űrtartalmú üvegeket adunk meg a program kódjában.

A képernyőre írást igénylő részfeladatok esetén az ékezetmentes kiírás is elfogadott.

A mintához tartalmában hasonlóan írja ki a képernyőre a feladat sorszámát (például:
`2. feladat`), valamint utaljon a kiírt tartalomra is! 

### 1. feladat

A megadott 15 számot tárolja el a programban egy megfelelő adatszerkezetben! A 15 szám
rendelkezésre áll az *uvegek.txt* állományban, amelyből azok a program kódjába
átmásolhatók. 

### 2. feladat

Kérje be a mintának megfelelően, és tárolja el, hogy Mari néni hány deciliter lekvárt (*L*)
főz be, ahol L értéke `0 < L <= 200!`

### 3. feladat

Az üvegek űrtartalma alapján határozza meg, hogy a legnagyobb üveg hány deciliteres és
hányadik a sorban! Ha több ilyen van, akkor az elsőt adja meg!

### 4. feladat

Írassa ki a képernyőre, hogy Mari néni *L* deciliter befőzött lekvárja elfér-e az üvegekben!
Ha az üveg mennyiség elegendő, akkor írja ki, hogy `„Elegendő üveg volt.”`, különben
azt, hogy `„Maradt lekvár.”`!

Minta a szöveges kimenet kialakításához:

    2. feladat
    Mari néni lekvárja (dl): 35
    3. feladat
    A legnagyobb üveg: 10 dl és 8. a sorban.
    4. feladat
    Elegendő üveg volt. 