import os
import json


def search_element_in_json_files(directory, element_to_search):
    # Loop through all files in the directory
    dict_wash=['dry','wash','wipe']
    details_false=[]
    details_count=0
    products_count=0
    matching_values = []
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            file_path = os.path.join(directory, filename)

            # Read the JSON file
            with open(file_path, 'r') as file:
                try:
                    json_data = json.load(file)

                    # Check if the element_to_search is in the JSON data
                    products_count+=len(json_data)
                    for jsone_element in json_data:
                        if  ('Machine wash' in (',').join(list(jsone_element[element_to_search_for].values()))) or ('Wipe clean' in (',').join(list(jsone_element[element_to_search_for].values()))) or ('Dry clean' in (',').join(list(jsone_element[element_to_search_for].values()))) or  ('Surface washable' in (',').join(list(jsone_element[element_to_search_for].values()))) or ('Hand wash' in (',').join(list(jsone_element[element_to_search_for].values()))) or  ('Spot clean' in (',').join(list(jsone_element[element_to_search_for].values()))):
                            details_count+=1
                        else:
                            details_false.append(list(jsone_element[element_to_search_for].values()))

                        for key, value in jsone_element[element_to_search_for].items():
                            # Check if the word_to_check is present in the current dictionary value
                            if 'Machine wash' in value or 'Wipe clean' in value or 'Dry clean' in value or 'Surface washable' in value or 'Hand wash' in value or 'Spot clean' in value:
                                # If yes, add the corresponding dictionary value to the list
                                matching_values.append(value)



                        # If you want to print the value of the element, uncomment the next line
                        # print(f"{element_to_search}: {json_data[element_to_search]}")

                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON in {file_path}: {e}")

    return products_count,details_count,details_false,matching_values



# Specify the directory and the element you want to search for
directory_path = 'results_nfl'
element_to_search_for = 'characteristics'

# Call the function
products_amount,details_amount,faults,matching=search_element_in_json_files(directory_path, element_to_search_for)
print(f'found{details_amount} out of {products_amount}')
faults
matching