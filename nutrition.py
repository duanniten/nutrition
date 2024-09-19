def main():
    #todo
    iten = getIten()
    printCalorires(iten)

def getIten():
    fruits = {
        "apple": {"calories": 130},
        "avocado": {"calories": 50},
        "banana": {"calories": 110},
        "cantaloupe": {"calories": 50},
        "grapefruit": {"calories": 60},
        "grapes": {"calories": 90},
        "honeydew melon": {"calories": 50}, 
        "kiwifruit": {"calories": 90},
        "lemon": {"calories": 15},
        "lime": {"calories": 10},
        "nectarine": {"calories": 60},
        "orange": {"calories": 80},
        "peach": {"calories": 60},
        "pear": {"calories": 100},
        "pineapple": {"calories": 50},
        "plums": {"calories": 70},
        "strawberries": {"calories": 50},
        "sweet_cherries": {"calories": 100},
        "tangerine": {"calories": 50},
        "watermelon": {"calories": 80}
    }
    fruit = None
    while fruit not in fruits.keys():
        fruit = input("Item ").strip().lower()
    return fruits[fruit]

def printCalorires(fruit:dict):
    print(f"Calories: {fruit["calories"]}")

main()