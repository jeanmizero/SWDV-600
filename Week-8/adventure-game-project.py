import random
enemyList = ["sharks", "nosy neighbors", "Krampus", "Kylo Ren"]
introductionList = ["He is deadly!", "He will destroy you!",
                    "they are watching you...", "they have nasty teeth!"]
# Adventurer class


class Adventurer:
    # constructor
    def __init__(self, name, holidayGifts, healthPoints):
        self.name = name
        self.position = 0
        self.holidayGifts = holidayGifts
        self.healthPoints = healthPoints

    # printout
    def __str__(self):
        output = "************************************************************\n"
        output += "Adventurer : " + self.name + "\n"
        output += "Position : " + str(self.position)
        output += " Holiday Gifts : " + str(self.holidayGifts) + "\n"
        output += "Health Points : " + str(self.healthPoints) + "\n"
        output += "************************************************************\n"
        return output

# Enemy class


class Enemy:
    # constructor
    def __init__(self, name, position, introduction, damage):
        self.name = name
        self.position = position
        self.introduction = introduction
        self.damage = damage

    # printout
    def __str__(self):
        output = "************************************************************\n"
        output += "Enemy : " + self.name + "\n"
        output += "Position : " + str(self.position)
        output += "Introduction : " + str(self.introduction) + "\n"
        output += "Damage : " + str(self.damage) + "\n"
        output += "************************************************************\n"
        return output

# start to play


def play(adventurer, enemies, pathLength):
    print("Start game! ")

    for i in range(1, pathLength + 1):
        input("Press RETURN to move forward.\n")
        adventurer.position = i
        print(adventurer.name + " is at " + str(adventurer.position))

        # found enemy
        for enemy in enemies:
            if adventurer.position == enemy.position:
                adventurer.healthPoints -= enemy.damage
                print("Got attacked by " + enemy.name + " and lost " +
                      str(enemy.damage) + " healthPoints")
                break
        # not found enemy
        else:
            randomNumber = random.randint(10, 50)
            adventurer.holidayGifts += randomNumber
            print("Recieved " + str(randomNumber) + " holiday gifts")

            # player died
        if adventurer.healthPoints <= 0:
            print("\n\n" + adventurer.name + " Lost")
            break
    else:
        print()
        print("Success! " + adventurer.name + " Win!")

# show results


def main():
    pathLength = 10
    adventurer = Adventurer("Aaron Burr!", 0, 100)
    numberOfEnemies = random.randint(
        int(0.3 * pathLength), int(0.7 * pathLength))

    # make empty list
    enemies = []
    for enemyNum in range(numberOfEnemies):
        enemyName = random.choice(enemyList)
        enemyIntroduction = random.choice(introductionList)
        enemyPosition = random.randint(1, pathLength)
        enemyDamage = random.randint(20, 50)
        enemies.append(Enemy(enemyName, enemyPosition, "It's " +
                             enemyName + enemyIntroduction, enemyDamage))
    play(adventurer, enemies, pathLength)

    print("\n\nGame is over! ")
    print(adventurer)


if __name__ == "__main__":
    main()
