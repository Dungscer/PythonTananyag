def DivisibleBy(number, by) -> bool:
    float_number = number / by # 5.05
    normal_number = int(float_number) # normális szám lesz  5
    return float_number == normal_number # ellenörzés során viszont vissza alakít így 5.05-öt nézi a 5.0-hoz


# elöszőr kérek a usertől egy bemeneti értéket
user_input = input()

# ezután a megadott értéket átalakítom számá
input_value = int(user_input)

if DivisibleBy(input_value, 2):
    print("A szám 2-vel osztható")
else:
    print("A szám nem osztható 2-vel")

if DivisibleBy(input_value, 3):
    print("A szám 3-mal osztható")
else:
    print("A szám nem osztható 3-mal")

if DivisibleBy(input_value, 7):
    print("A szám 7-tel osztható")
else:
    print("A szám nem osztható 7-tel")
