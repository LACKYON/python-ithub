import random

print("ЧЕГО СКАЗАТЬ-ТО ХОТЕЛ, МИЛОК?!")
bye_count = 0

while bye_count < 3:
    phrase = input("> ")

    if phrase == "ПОКА!":
        bye_count += 1
        if bye_count == 3:
            print("ДО СВИДАНИЯ, МИЛЫЙ!")
        else:
            print("НЕТ, НИ РАЗУ С", random.randint(1930, 1950), "ГОДА!")
    else:
        bye_count = 0
        if phrase.isupper():
            print("НЕТ, НИ РАЗУ С", random.randint(1930, 1950), "ГОДА!")
        else:
            print("АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!")
