# ECOSYSTEM SETUP

animals = [
    {
        "type": "rabbit",
        "name": "Fluffy",
        "energy": 5,
        "alive": True
    },
    {
        "type": "fox",
        "name": "Shadow",
        "energy": 8,
        "alive": True
    }
]

# SIMULATE 3 DAYS
for day in range(1, 4):
    print("\nDay", day)

    for animal in animals:

        if animal["alive"]:

            # Rabbits eat grass
            if animal["type"] == "rabbit":
                animal["energy"] += 2
                print(animal["name"], "eats grass. Energy:", animal["energy"])

            # Foxes hunt rabbits
            elif animal["type"] == "fox":
                hunted = False

                for target in animals:
                    if target["type"] == "rabbit" and target["alive"]:
                        target["alive"] = False
                        animal["energy"] += 4
                        hunted = True
                        print(animal["name"], "hunts", target["name"])
                        break

                if not hunted:
                    animal["energy"] -= 3
                    print(animal["name"], "found no food. Energy:", animal["energy"])

            # Energy check
            if animal["energy"] <= 0:
                animal["alive"] = False
                print(animal["name"], "has died.")