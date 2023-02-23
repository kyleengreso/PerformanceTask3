from Pizza import Deluxe, Special, Primo

base = 450
name = input("Please enter your name: ")
pizza_type = input("Please enter your pizza type (Deluxe, Special, Primo): ")

if pizza_type == "Deluxe":
    total_price = Deluxe()
elif pizza_type == "Special":
    total_price = Special()
elif pizza_type == "Primo":
    total_price = Primo()
else:
    "Invalid"

add_ons = []
if pizza_type == "Deluxe":
    add_ons = ["Cheese", "BaconHam", "OnionChili"]
if pizza_type == "Special":
    add_ons = ["Cheese", "Pepper", "BaconHam", "Mushroom", "OnionsChili"]
if pizza_type == "Primo":
    add_ons = ["MozzarellaCheese", "Pepper", "BaconHam", "Mushroom", "OnionsChili", "Tomato", "Pineapple", "Salami"]

FinalPizzaChoice = {
    "Customers Name": name,
    "Pizza Type": pizza_type,
    "Add Ons": add_ons,
    "Total Price": total_price
}

print("Base:", base)
print("Details:", add_ons)
print("Customer:", name)
print("Total Price:", total_price)


