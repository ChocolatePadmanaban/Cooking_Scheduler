import csv
import os


ingredient_files=os.listdir("recipe_ingredients")
ingredient_dict={}

for ingredient_file in ingredient_files:
    i_file = open('recipe_ingredients/'+ingredient_file)
    csv_i_file = csv.reader(i_file)
    for row in csv_i_file:
        if row[0] not in ['name', 'question']:
            if row[0] in ingredient_dict.keys() and row[2] != ingredient_dict[row[0]]:
                if type(ingredient_dict[row[0]]) == type([]):
                    ingredient_dict[row[0]].append(row[2])
                else:
                    ingredient_dict[row[0]]=[ingredient_dict[row[0]],row[2]]
            else:
                ingredient_dict[row[0]]=row[2]
    i_file.close()

row_format ="{:<20}" *2
for key in sorted(ingredient_dict):
    #print( row_format.format(key, ingredient_dict[key]))
    print( key, ingredient_dict[key])
