import matplotlib.pyplot as plt
import numpy as np

yield_rates = {
    "Barley": {"reqlvl": 3,"chance1":103, "chance99": 180},
    "Hammerstone": {"reqlvl": 4,"chance1":104, "chance99": 180},
    "Asgarnian": {"reqlvl": 8,"chance1":108, "chance99": 180},
    "Jute": {"reqlvl": 13,"chance1":113, "chance99": 180},
    "Yanillian": {"reqlvl": 16,"chance1":116, "chance99": 180},
    "Krandorian": {"reqlvl": 21,"chance1":121, "chance99": 180},
    "Wildblood": {"reqlvl": 28,"chance1":128, "chance99": 180},
}

# "Guam": {"reqlvl": 9,"chance1":25, "chance99":80},
#     "Marrentill": {"reqlvl": 14,"chance1":28, "chance99":80},
#     "Tarromin": {"reqlvl": 19,"chance1":31, "chance99":80},
#     "Harralander": {"reqlvl": 26,"chance1":36, "chance99":80},
#     "Goutweed": {"reqlvl": 29,"chance1":39, "chance99":80},
#     "Ranarr": {"reqlvl": 32,"chance1":39, "chance99":80},
#     "Toadflax": {"reqlvl": 38,"chance1":43, "chance99":80},
#     "Irit": {"reqlvl": 44,"chance1":46, "chance99":80},
#     "Avantoe": {"reqlvl": 50,"chance1":50, "chance99":80},
#     "Kwuarm": {"reqlvl": 56,"chance1":54, "chance99":80},
#     "Snapdragon": {"reqlvl": 62,"chance1":57, "chance99":80},
#     "Cadantine": {"reqlvl": 67,"chance1":60, "chance99":80},
#     "Lantadyme": {"reqlvl": 73,"chance1":64, "chance99":80},
#     "Dwarf weed": {"reqlvl": 79,"chance1":67, "chance99":80},
#     "Torstol": {"reqlvl": 85,"chance1":71, "chance99":80},

    # "Potato": {"reqlvl": 1,"chance1":101, "chance99": 180, "plantxp": 8, "harvxp": 9, "growtime": 40},
    # "Onion": {"reqlvl": 5,"chance1":105, "chance99": 180, "plantxp": 9.5, "harvxp": 10.5, "growtime": 40},
    # "Cabbage": {"reqlvl": 7,"chance1":107, "chance99": 180, "plantxp": 10, "harvxp": 11.5, "growtime": 40},
    # "Tomato": {"reqlvl": 12,"chance1":112, "chance99": 180, "plantxp": 12.5, "harvxp": 14, "growtime": 40},
    # "Sweetcorn": {"reqlvl": 20,"chance1":88, "chance99": 180, "plantxp": 17, "harvxp": 19, "growtime": 60},
    # "Strawberry": {"reqlvl": 31,"chance1":103, "chance99": 180, "plantxp": 26, "harvxp": 29, "growtime": 60},
    # "Watermelon": {"reqlvl": 47,"chance1":126, "chance99": 180, "plantxp": 48.5, "harvxp": 54.5, "growtime": 80},
    # "Snape Grass": {"reqlvl": 61,"chance1":148, "chance99": 195, "plantxp": 82, "harvxp": 82, "growtime": 70},

#     "Barley": {"reqlvl": 3,"chance1":103, "chance99": 180},
#     "Hammerstone": {"reqlvl": 4,"chance1":104, "chance99": 180},
#     "Asgarnian": {"reqlvl": 8,"chance1":108, "chance99": 180},
#     "Jute": {"reqlvl": 13,"chance1":113, "chance99": 180},
#     "Yanillian": {"reqlvl": 16,"chance1":116, "chance99": 180},
#     "Krandorian": {"reqlvl": 21,"chance1":121, "chance99": 180},
#     "Wildblood": {"reqlvl": 28,"chance1":128, "chance99": 180},

#     "Giant seaweed": {"reqlvl": 23,"chance1":150, "chance99": 210}



lives = 3
compost = 1
supercompost = 2
ultracompost = 3

total_lives = lives + supercompost


def expectedYield(level, chance1, chance99, itembonus, diarybonus, harvestLives):
    chanceToSave = (  (((chance1 * (99-level))/98)  + ((chance99 * (level-1))/98)) * (1+itembonus) * (1+diarybonus) + 1  ) / 256

    return round(harvestLives / (1 - chanceToSave),2)



for crop in yield_rates:
    print("\n" + crop + " -------------------------------------- ")
    chance1 = yield_rates[crop]["chance1"]
    chance99 = yield_rates[crop]["chance99"]
    avgyield = []
    lvls = []
    for i in range(100):
        if yield_rates[crop]["reqlvl"] <= i:
            xp = expectedYield(i, chance1, chance99, 0, 0, total_lives)
            print(str(i) + ": " + str(xp), end="  \t")
            avgyield.append(xp)
            lvls.append(i)
            if i % 6 == 0:
                print("")
    print("")
    x = lvls
    y = avgyield
    plt.plot(x, y, label=crop)


# # x axis values
# x = yield_rates["Tomato"]["xphr"]
# # corresponding y axis values
# y = yield_rates["Tomato"]["lvls"]
 
# i = yield_rates["Sweetcorn"]["xphr"]
# j = yield_rates["Sweetcorn"]["lvls"]
# # plotting the points
# plt.plot(y, x, label="Tomato", color="#ED0000")
# plt.plot(j, i, label="Sweetcorn", color="#D2A400")
# naming the x axis
plt.xlabel('level')
# naming the y axis
plt.ylabel('avg yield')
plt.xticks(np.arange(0, 99+1, 5.0))
plt.yticks(np.arange(8, 20+1, 0.5))
# giving a title to my graph
plt.title('Hops average yield - SUPER COMPOST')
plt.legend()
 
# function to show the plot
plt.show()