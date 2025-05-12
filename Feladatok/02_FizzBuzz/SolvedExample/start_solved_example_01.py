def DivisibleBy(number, by) -> bool:
    float_number = number / by # 5.05
    normal_number = int(float_number) # normális szám lesz  5
    return float_number == normal_number # ellenörzés során viszont vissza alakít így 5.05-öt nézi a 5.0-hoz


for i in range(1, 101):
    if DivisibleBy(i, 3) and DivisibleBy(i, 5):
        print("FizzBuzz")
    elif DivisibleBy(i, 3):
        print("Fizz")
    elif DivisibleBy(i, 5):
        print("Buzz")
    else:
        print(i)
