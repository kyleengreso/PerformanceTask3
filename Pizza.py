AddOns = {
    "Cheese": 100,
    "MozzarellaCheese": 150,
    "Pepper": 80,
    "BaconHam": 120,
    "Mushroom": 130,
    "OnionsChili": 110,
    "Tomato": 90,
    "Pineapple": 100,
    "Salami": 120
}

def Deluxe():
    addons_price = AddOns["Cheese"] + AddOns["BaconHam"] + AddOns["OnionsChili"]
    total_price = 450 + addons_price
    return total_price

def Special():
    addons_price = AddOns["Cheese"] + AddOns["Pepper"] + AddOns["BaconHam"] + AddOns["Mushroom"] + AddOns["OnionsChili"]
    total_price = 450 + addons_price
    return total_price

def Primo():
    addons_price = AddOns["MozzarellaCheese"] + AddOns["Pepper"] + AddOns["BaconHam"] + AddOns["Mushroom"] + AddOns["OnionsChili"] + AddOns["Tomato"] + AddOns["Pineapple"] + AddOns["Salami"]
    total_price = 450 + addons_price
    return total_price
