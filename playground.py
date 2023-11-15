

import random

def randomword():
    f = open("test_list.txt", "r")
    available_words = f.read().split()
    f.close()
    #print(available_words)
    randomword = random.choice(available_words)
    return randomword
#print(randomword)


print(randomword())