import json
import re
import pandas as pd

file_json = 'OptoSigmaProducts.json'

with open(file_json, 'r') as json_file:                                                                #open and read json file
    products = json.load(json_file)

spec_selected = re.compile(r"Focal length|Diameter|Design Wavelength", re.I)                           #get rellevant specifications (3/5)         #also includes back focal lenght

standarized_products = {}
for product, spec in products.items():
    standarized_product = {}
    for spec_name, spec_value in spec.items():

        if spec_selected.search(spec_name):
            #standarize specifications

            standarized_spec = re.sub(r'\s(\w)', lambda match: ' ' + match.group(0).upper(), spec_name)  #all names in capital letters: \s(\w) means space joint with alphanumeric character. we match it and replace it with space + capital letters 
            standarized_spec = re.sub(r'F*\b|Fb*\b|\u03a6D', '', standarized_spec)                       #delete unwanted sufixes from specification names

            standarized_values = re.sub(r'\u03c6', '', spec_value)                                       #delete unwanted sufixes from specification "values"            
            standarized_values = re.sub(r'(\d+\.?\d*)\s*(.*)', 
                                        lambda match: match.group(1) +  ' ' + match.group(2),            
                                        standarized_values)

            standarized_product[standarized_spec] = standarized_values                                   #save in a new dictionary
    
    standarized_products[product] = standarized_product                                 

##del products

table = pd.DataFrame(standarized_products).T                  #define our standarized_products as a DF in order to print a little table in the console easily;  .T transpose     
print(table)



















# file_name = "StandarizedProducts.json"

# with open(file_name, 'w') as json_file:                                             #open the json file and write (or overwrite) all in

#     json.dump(standarized_products, json_file, indent=4)                            #write the dictionari as a json_fiel
    

#     print(f"Information saved as {file_name}")        



    



