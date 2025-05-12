# elöszőr kérek a usertől egy bemeneti értéket
user_input = input()

# ezután a megadott értéket átalakítom számá
input_value = int(user_input)

float_value = input_value / 2
value = int(float_value)

print(float_value)
print(value)

if float_value == value:
    print("A szám 2-vel osztható")
else:
    print("A szám nem osztható 2-vel")

# ---------------------------
float_value = input_value / 3
value_two = int(float_value)

print(float_value)
print(value_two)

if float_value == value_two:
    print("A szám 3-mal osztható")
else:
    print("A szám nem osztható 3-mal")

# ---------------------------
float_value = input_value / 7
value_two = int(float_value)

print(float_value)
print(value_two)

if float_value == value_two:
    print("A szám 7-tel osztható")
else:
    print("A szám nem osztható 7-tel")
