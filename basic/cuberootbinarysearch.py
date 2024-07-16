# cube = 27
# Only works for positive cubes. For example, it won't work for cube root of 0.5 where its cube root is > cube.
# We can handle this corner case separately
cube = 10000
epsilon = 0.1
low = 0
high = cube
guess = (low+high)/2.0
increment = 0.01
num_guesses = 0

while abs(guess ** 3 - cube) >= epsilon:
    print("low = ", low)
    print("high = ", high)
    print("guess = ", guess, "\n")
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    guess = (low+high)/2.0
    num_guesses += 1

print("num guesses = ", num_guesses)

if abs(guess ** 3 - cube) >= epsilon:
    print("Failed on cube root of = ", cube)
else:
    print(guess, "is close to the cube root of ", cube)