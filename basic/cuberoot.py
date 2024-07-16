# Method 1  = Guess and check

number = 8

for guess in range(number + 1):
    if guess ** 3 == number:
        print("Cube root using guess and check is = ", guess)

# Method 2 => Minor Improvements = Handling negatives, checking valid cases
number = 9
guess = 1
for guess in range(abs(number) + 1):
    if guess ** 3 >= abs(number):
        break

if guess ** 3 != abs(number):
    print(number, "is not a perfect cube")
else:
    if number < 0:
        guess = -guess
    print("Cube root of ", number, "is ", guess)
