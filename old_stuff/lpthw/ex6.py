#more string formatting

types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: {y}")

hilarious = False
joke_evaluation = "isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

w = "left side "
e = "right side"

print(w + e)
