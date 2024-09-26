little =   {"hairy":"rat", "clever":"bat", "slow":"cod", "bare":"ant", "quick":"cat"}
midsized = {"hairy":"ewe", "clever":"fox", "slow":"pig", "bare":"eel", "quick":"doe"}
large =    {"hairy":"gnu", "clever":"ape", "slow":"cow", "bare":"elephant", "quick":"nag"}

animals = {"little": little, "midsized": midsized, "large": large}

for size in animals:
  animal_by_size = animals[size]
  for prop in animal_by_size:
    print(animal_by_size[prop], end=" ")
  print("\n", end="")
