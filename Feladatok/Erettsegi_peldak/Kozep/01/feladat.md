# Kihívás
Az interneten számos sportkihívással találkozhatunk. Ezek általában egy adott időszakra
tűznek ki valamilyen elérendő célt, ezzel is mozgásra ösztönözve az embereket. Ebben
a feladatban egy heti mozgáskihívás eredményeit kell kiértékelnie!

A kihívásban a heti mozgást egy applikáció segítségével kellett rögzíteni és a hét végén
beküldeni. A kihívást a következő mozgásformák segítségével lehetett teljesíteni: úszás,
gyaloglás, futás, kerékpározás. A kihívás célja 40 km elérése volt. Az applikáció rögzítette
a heti mozgást, a felhasználó pedig a hét végén beküldte a rögzített teljesítményt.

A beküldött érték a mozgásforma betűjelét tartalmazza a megtett távolságoknak
megfelelően. Az alábbi táblázatban láthatóak a betűjelek és a hozzájuk tartozó távolságértékek: 


| Mozgásforma  | Kód    | Kódhoz tartozó távolság |
| ------------ | ------ | ----------------------- |
| Úszás        | U      | 1 km                    |
| Gyaloglás    | G      | 1 km                    |
| Futás        | F      | 2 km                    |
| Kerékpározás | K      | 10 km                   |

Az alábbi példa egy felhasználó heti aktivitását mutatja: 
`FFFGGGUUUFFFGGKKK `

A felhasználó a héten a következő tevékenységeket végezte:
- FFF – 6 km futás,
- GGG – 3 km gyaloglás,
- UUU – 3 km úszás,
- FFF – 6 km futás,
- GG – 2 km gyaloglás,
- KKK – 30 km kerékpározás.

**Ezzel 50 kilométert teljesített.**

Készítsen programot, amely kiértékeli a beküldött aktivitást!
A program forráskódját mentse kihivas néven!
A program megírásakor a felhasználó által megadott adatok helyességét,
érvényességét nem kell ellenőriznie, és feltételezheti, hogy a rendelkezésre álló adatok
a leírtaknak megfelelnek. 

### 1. feladat

Kérje be és tárolja el a felhasználó heti aktivitását! Feltételezheti, hogy a megadott sorozat
hossza 250 karakternél rövidebb. 