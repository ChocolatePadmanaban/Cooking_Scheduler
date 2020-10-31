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

with open('recipe_ingredients/'+recipies[selected_recipe]+'.csv') as i_file:
    csv_i_file=csv.reader(i_file)
    csv_i_file=[_ for _ in csv_i_file]
    factor_num=float(input(csv_i_file[1][2]))
    factor=factor_num/float(csv_i_file[1][1])
    temp_dict={}
    for row in csv_i_file:
        if row[0] not in ['name','question']:
            temp_dict[row[0]]=[float(row[1])*factor,row[2]]
    recipes_dict[recipies[selected_recipe]]=temp_dict

print(recipes_dict)

