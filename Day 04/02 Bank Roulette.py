import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# my answer
the_chosen_one = random.choice(friends)
print(the_chosen_one)

# Option 1: esiest and shortest way
print(random.choice(friends))

# Option 2
random_index = random.randint(0, 4) # up to 0-4 since there are 5 people inside the list
print(friends[random_index])