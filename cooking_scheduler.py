import csv
import os


ingredient_files=os.listdir("recipe_ingredients")
recipes_dict={}

recipies = [recipie[:-len('.csv')] for recipie in ingredient_files]



print("Select the food you are gonna prepare from the list  ")
for i in enumerate(recipies, start=1):
    print(i[0], i[1])
print()
selected_recipe = int(input("Enter your option : ")) -1
print("Selected option :", recipies[selected_recipe])