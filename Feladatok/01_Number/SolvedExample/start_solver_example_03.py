# elöszőr kérek a usertől egy bemeneti értéket
user_input = input()

# ezután a megadott értéket átalakítom számá
input_value = int(user_input)

if input_value % 2 == 0:
    print("A szám 2-vel osztható")
else:
    print("A szám nem osztható 2-vel")

if input_value % 3 == 0:
    print("A szám 3-mal osztható")
else:
    print("A szám nem osztható 3-mal")

if input_value % 7 == 0:
    print("A szám 7-tel osztható")
else:
    print("A szám nem osztható 7-tel")
