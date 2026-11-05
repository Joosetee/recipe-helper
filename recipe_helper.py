
# RECIPE HELPER PROJECT

# 1. Store recipe ingredients and quantities
ingredients = {
    "pasta": 500,
    "tomatoes": 400,
    "garlic": 15,
    "basil": 20,
    "olive oil": 30,
    "salt": 5
}

# 2. Store available pantry ingredients
pantry = {
    "pasta": 1000,
    "tomatoes": 200,
    "olive oil": 30,
    "salt": 10
}

# 3. Create a set of pantry ingredient names
pantry_items = set(pantry.keys())

# 4. Check ingredient availability and quantities
shopping_list = []
ingredients_checked = 0

for item, qty in ingredients.items():
    ingredients_checked += 1

    if item not in pantry_items:
        print(item, ":", "Missing!")

        shopping_list.append(item)

    elif pantry[item] >= qty:
        print(item, ":", "Enough available!")

    else:
        print(item, ":", "Not enough available!")

        shopping_list.append(item)

# 5. Display shopping list
print("==============================")
print("       SHOPPING LIST")
print("==============================")

for item in shopping_list:
    print(item)

print("Ingredients checked:", ingredients_checked)
print("Shopping list:", shopping_list)

# 6. Check multiple conditions using AND
if pantry["pasta"] >= ingredients["pasta"] and pantry["olive oil"] >= ingredients["olive oil"]:
    print("You have enough pasta and olive oil!")
else:
    print("You need to check your ingredients!")

# 7. Check multiple conditions using OR
if "basil" not in pantry_items or pantry["tomatoes"] < ingredients["tomatoes"]:
    print("You need to buy ingredients!")
else:
    print("You have everything you need!")

# 8. Store available serving sizes in a tuple
serving_options = (2, 4, 6, 8)

print("Available serving sizes:", serving_options)

original_servings = 2
chosen_servings = int(input("How many servings would you like? "))

if chosen_servings in serving_options:
    factor = chosen_servings / original_servings

    print("==============================")
    print("    ADJUSTED QUANTITIES")
    print("==============================")

    for item, qty in ingredients.items():
        new_quantity = qty * factor
        print(item, ":", new_quantity)

else:
    print("Invalid serving size. Please choose 2, 4, 6 or 8.")

# 9. Allow the user to check the recipe again
while True:
    answer = input("Would you like to check again? yes/no: ").lower()

    if answer == "no":
        print("Thank you for using Recipe Helper!")
        break

    elif answer == "yes":
        print("Checking your recipe again...")

        for item, qty in ingredients.items():
            if item not in pantry_items:
                print(item, ":", "Missing!")

            elif pantry[item] >= qty:
                print(item, ":", "Enough available!")

            else:
                print(item, ":", "Not enough available!")

    else:
        print("Please enter yes or no.")
