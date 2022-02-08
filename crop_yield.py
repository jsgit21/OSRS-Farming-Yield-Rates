import matplotlib.pyplot as plt
import numpy as np

hops = {
    "Barley": {"reqlvl": 3,"chance1":103, "chance99": 180, "plantxp": 8.5, "harvxp": 9.5, "growtime": 40},
    "Hammerstone": {"reqlvl": 4,"chance1":104, "chance99": 180, "plantxp": 9, "harvxp": 10, "growtime": 40},
    "Asgarnian": {"reqlvl": 8,"chance1":108, "chance99": 180, "plantxp": 10.9, "harvxp": 12, "growtime": 50},
    "Jute": {"reqlvl": 13,"chance1":113, "chance99": 180, "plantxp": 13, "harvxp": 14.5, "growtime": 50},
    "Yanillian": {"reqlvl": 16,"chance1":116, "chance99": 180, "plantxp": 14.5, "harvxp": 16, "growtime": 60},
    "Krandorian": {"reqlvl": 21,"chance1":121, "chance99": 180, "plantxp": 17.5, "harvxp": 19.5, "growtime": 70},
    "Wildblood": {"reqlvl": 28,"chance1":128, "chance99": 180, "plantxp": 23, "harvxp": 26, "growtime": 80},

}

herbs = {
    "Guam": {"reqlvl": 9,"chance1":25, "chance99":80, "plantxp": 11, "harvxp": 12.5, "growtime": 80},
    "Marrentill": {"reqlvl": 14,"chance1":28, "chance99":80, "plantxp": 13.5, "harvxp": 15, "growtime": 80},
    "Tarromin": {"reqlvl": 19,"chance1":31, "chance99":80, "plantxp": 16, "harvxp": 18, "growtime": 80},
    "Harralander": {"reqlvl": 26,"chance1":36, "chance99":80, "plantxp": 21.5, "harvxp": 24, "growtime": 80},
    "Goutweed": {"reqlvl": 29,"chance1":39, "chance99":80, "plantxp": 105, "harvxp": 45, "growtime": 80},
    "Ranarr": {"reqlvl": 32,"chance1":39, "chance99":80, "plantxp": 27, "harvxp": 30.5, "growtime": 80},
    "Toadflax": {"reqlvl": 38,"chance1":43, "chance99":80, "plantxp": 34, "harvxp": 38.5, "growtime": 80},
    "Irit": {"reqlvl": 44,"chance1":46, "chance99":80, "plantxp": 43, "harvxp": 48.5, "growtime": 80},
    "Avantoe": {"reqlvl": 50,"chance1":50, "chance99":80, "plantxp": 54.5, "harvxp": 61.5, "growtime": 80},
    "Kwuarm": {"reqlvl": 56,"chance1":54, "chance99":80, "plantxp": 69, "harvxp": 78, "growtime": 80},
    "Snapdragon": {"reqlvl": 62,"chance1":57, "chance99":80, "plantxp": 87.5, "harvxp": 98.5, "growtime": 80},
    "Cadantine": {"reqlvl": 67,"chance1":60, "chance99":80, "plantxp": 106.5, "harvxp": 120, "growtime": 80},
    "Lantadyme": {"reqlvl": 73,"chance1":64, "chance99":80, "plantxp": 134.5, "harvxp": 151.5, "growtime": 80},
    "Dwarf weed": {"reqlvl": 79,"chance1":67, "chance99":80, "plantxp": 170.5, "harvxp": 192, "growtime": 80},
    "Torstol": {"reqlvl": 85,"chance1":71, "chance99":80, "plantxp": 199.5, "harvxp": 224.5, "growtime": 80},
}

allotments = {
    "stats": {"ymax":1600, "step":100.0},
    "crops": {
        "Potato": {"reqlvl": 1,"chance1":101, "chance99": 180, "plantxp": 8, "harvxp": 9, "growtime": 40},
        "Onion": {"reqlvl": 5,"chance1":105, "chance99": 180, "plantxp": 9.5, "harvxp": 10.5, "growtime": 40},
        "Cabbage": {"reqlvl": 7,"chance1":107, "chance99": 180, "plantxp": 10, "harvxp": 11.5, "growtime": 40},
        "Tomato": {"reqlvl": 12,"chance1":112, "chance99": 180, "plantxp": 12.5, "harvxp": 14, "growtime": 40},
        "Sweetcorn": {"reqlvl": 20,"chance1":88, "chance99": 180, "plantxp": 17, "harvxp": 19, "growtime": 60},
        "Strawberry": {"reqlvl": 31,"chance1":103, "chance99": 180, "plantxp": 26, "harvxp": 29, "growtime": 60},
        "Watermelon": {"reqlvl": 47,"chance1":126, "chance99": 180, "plantxp": 48.5, "harvxp": 54.5, "growtime": 80},
        "Snape Grass": {"reqlvl": 61,"chance1":148, "chance99": 195, "plantxp": 82, "harvxp": 82, "growtime": 70},
    }
}

seaweed = {
"Giant seaweed": {"reqlvl": 23,"chance1":150, "chance99": 210}
}



lives = 3
compost = 1
supercompost = 2
ultracompost = 3

total_lives = lives + supercompost


def expectedYield(level, plantxp, harvxp, chance1, chance99, itembonus, diarybonus, harvestLives, growtime):
    chanceToSave = (  (((chance1 * (99-level))/98)  
    + ((chance99 * (level-1))/98)) * (1+itembonus) 
    * (1+diarybonus) + 1  ) / 256

    avgyield = round(harvestLives / (1 - chanceToSave),2)
    #return round(harvestLives / (1 - chanceToSave),2)

    avgxp = plantxp + (avgyield * harvxp)

    harvestsPerHour = 60/growtime
    xpPerHour = harvestsPerHour * avgxp
    return round(xpPerHour,2)


def generate_graph(crop_type):

    crop_group = crop_type["crops"]
    graph_ymax = crop_type["stats"]["ymax"]
    graph_step = crop_type["stats"]["step"]

    for crop in crop_group:
        print("\n" + crop + " -------------------------------------- ")
        chance1 = crop_group[crop]["chance1"]
        chance99 = crop_group[crop]["chance99"]
        plantxp = crop_group[crop]["plantxp"]
        harvxp = crop_group[crop]["harvxp"]
        growtime = crop_group[crop]["growtime"]
        xphr = []
        lvls = []
        for i in range(100):
            if crop_group[crop]["reqlvl"] <= i:
                xp = expectedYield(i, plantxp, harvxp, chance1, chance99, 0, 0, total_lives, growtime)
                print(str(i) + ": " + str(xp), end="  \t")
                xphr.append(xp)
                lvls.append(i)
                if i % 6 == 0:
                    print("")
        print("")
        x = lvls
        y = xphr
        plt.plot(x, y, label=crop)

    # naming the x axis
    plt.xlabel('level')
    # naming the y axis
    plt.ylabel('xp/hr')
    plt.xticks(np.arange(0, 99+1, 5.0))
    plt.yticks(np.arange(0, graph_ymax+1, graph_step))
    # giving a title to my graph
    plt.title('Hops avg xp/hr - SUPER COMPOST')
    plt.legend()
    
    # function to show the plot
    plt.show()


generate_graph(allotments)