# program to generate band name randomly from lists of adjectives and animals

import random

# random.choice(list_name) selects random value from a list

#randomly selects adj from list
#adj_list = ["Lost", "Giddy", "Mischievous", "Soaked", "Impatient", "Hungry, Hungry", "Bored", "Jealous", "Guilty", "Ecstatic", "Relaxed", "Suspicious", "Cunning", "Flexible", "Loyal", "Unloyal", "Content", "Speedy", "Triumphant", "Invincible", "Arctic", "River", "Confident", "Reliable", "Crafty", "Invisible", "Legendary"]
#adj = random.choice(adj_list)

#randomly generates a name for a tavern / inn
#animal_list = ["Dogs", "Cats", "Foxes", "Ferrets", "Narwhals", "Hippos", "Cephalopods", "Yaks", "Llamas", "Mustangs", "Cheetahs", "Lions", "Wolverines", "Honey Badgers", "Kookaburras", "Penguins", "Bears", "Pacyderms", "Dinosaurs", "Shepherds", "Koalas", "Pythons", "Bovines", "Dairy Cows", "Sheep", "Goats", "Gorillas", "Earthworms"]


#print("You visit The" + adj1 + " " + animal + ".")


import random

def randomword(list_name):
    f = open(list_name, "r")
    available_words = f.read().split()
    f.close()
    #print(available_words)
    randomword = random.choice(available_words)
    return randomword
#print(randomword)

Inn_name = []
Inn_name.append(randomword("adjective_list.txt"))
print(Inn_name)
Inn_name.append(randomword("subject_list.txt"))
print(Inn_name)
#print(randomword())
print("You visit The " + ' '.join(Inn_name))