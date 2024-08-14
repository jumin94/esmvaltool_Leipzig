
# Imports
import glob
import os
import yaml

# Root directory where the CMIP6 data is stored
rootpath = "/climca/data/CMIP6"

# Short name of the variable and MIP to search for
short_name = "ua"
mip = "Amon"

# Search for all files in the Amon MIP under the SSP5-8.5 experiment with the variable ua for the year 2015
file_list_Amon = glob.glob(os.path.join(rootpath, f"*/*/*/ssp585/*/{mip}/{short_name}/*/*/*2015*.nc"))

# Initialize lists to store dictionaries of attributes for Amon and Omon datasets
dict_attr_list = []
dict_attr_list_Omon = []

# Iterate through each file found in the Amon file list
for file in file_list_Amon:
    # Construct paths to find corresponding Omon files (tos variable) for the same ensemble member
    file_attrs = file.split("/")[-9:-2]  # Extract relevant attributes from the file path
    keys = ["dataset", "exp", "ensemble", "mip", "short_name", "grid"]
    
    # Search for corresponding Omon files for SSP5-8.5 and historical experiments
    file_list_Omon = glob.glob(os.path.join(rootpath, '/ScenarioMIP/' + '/'.join(file_attrs[:4]) + "/Omon/tos/*/*/*2015*.nc"))
    file_list_Omon_hist = glob.glob(os.path.join(rootpath, '/CMIP/' + '/'.join(file_attrs[:2]) + "/historical/" + file_attrs[3] + "/Omon/tos/*/*/*2014*.nc"))

    # If both SSP5-8.5 and historical Omon files exist, proceed to record the dataset attributes
    if len(file_list_Omon) != 0 and len(file_list_Omon_hist) != 0:
        # Extract Omon file attributes
        file_attrs_Omon = file_list_Omon[0].split("/")[-8:-2]
        
        # Create a dictionary for the Amon dataset attributes and append to the list
        dict_attr = {key: value for key, value in zip(keys, file_attrs[1:])}
        dict_attr["exp"] = ["historical", "ssp585"]
        dict_attr["project"] = "CMIP6"
        dict_attr.pop("mip", None)
        dict_attr.pop("short_name", None)
        dict_attr_list.append(dict_attr)

        # Create a dictionary for the Omon dataset attributes and append to the list
        dict_attr_Omon = {key: value for key, value in zip(keys, file_attrs_Omon)}
        dict_attr_Omon["exp"] = ["historical", "ssp585"]
        dict_attr_Omon["project"] = "CMIP6"
        dict_attr_Omon.pop("mip", None)
        dict_attr_Omon.pop("short_name", None)
        dict_attr_list_Omon.append(dict_attr_Omon)
    else:
        print(f'No tos found for {file_attrs[1]}')  # Print a message if no corresponding tos file is found

# Remove duplicates from the attribute lists
list_Omon = [i for n, i in enumerate(dict_attr_list_Omon) if i not in dict_attr_list_Omon[n + 1:]]
list_Amon = [i for n, i in enumerate(dict_attr_list) if i not in dict_attr_list[n + 1:]]

# Write the resulting dataset attributes to a YAML file
with open("/home/jmindlin/historical_period_storylines/Amon_Omon_recipe_datasets.yml", "w") as f:
    yaml.dump({"datasets_Amon": list_Amon, "datasets_Omon": list_Omon}, f, default_flow_style=False)

# Remember to take a break after each completed task :) 
