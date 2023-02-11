import os, json

dir_path = r"database_recipes"

# list to store files
res = []
final_dict=list()
# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        f = open(os.path.join(dir_path, path))
        data = json.load(f)
        data['crafted_item']=path[:-5]
        final_dict.append(data)

with open("database_recipes.json", "w") as write_file:
    json.dump(final_dict, write_file, indent=4, sort_keys=True)
