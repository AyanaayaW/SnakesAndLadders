from random import randint

obstacles = [
    {
        17:7,
        54:34,
        62:19,
        64:60,
        87:36,
        93:73,
        95:75,
        98:79,
    },
    {
        1:38,
        4:14,
        9:31,
        21:42,
        28:84,
        51:67,
        72:91,
        80:99,
    }
]

playercount = int(input("How many people will be playing today? :"))


playernames = []
playerpos = []

for i in range(playercount):
    playernames.append(input(f"Enter the name of player {i+1}: "))
    playerpos.append(0)

running = True

while running:
    for i in range(playercount):
        roll = randint(1,6)
        
        print(f"it is {playernames[i]}'s turn!")
        input("Press enter to roll the dice!")
        print(f"You rolled a {roll}")
        
        if playerpos[i]+roll > 100:
            print("Your roll was too high!")
        
        elif playerpos[i]+roll == 100:
            input("Congratulations! You won the game!")
            running = False
            break

        else:
            playerpos[i] += roll


        if playerpos[i] in obstacles[0].keys():
            playerpos[i] = obstacles[0][playerpos[i]]
            input(f"You were swallowed up by a snake! You're now at square {playerpos[i]}")
        
        elif playerpos[i] in obstacles[1].keys():
            playerpos[i] = obstacles[1][playerpos[i]]
            input(f"You climbed up a ladder that you found! You're now at square {playerpos[i]}")
        
        else:
            input(f"You are at square {playerpos[i]}")

    