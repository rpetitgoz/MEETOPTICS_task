import requests
from bs4 import BeautifulSoup
import json


url = 'https://www.optosigma.com/eu_en/optics/lenses/spherical-lenses/plano-convex-spherical-lenses/n-bk7-plano-convex-lenses-ar-400-700nm-SLB-P-M.html'

try:
    
    response = requests.get(url)

    if response.status_code == 200:                                                            #== 200->OK
        soup = BeautifulSoup(response.text, 'html.parser')                                     # interprets and allows us to data scraping this html
        products = soup.find_all('tr', class_ = "grouped-item")                                #find all the information of each product
        
        products_information ={}
        
        for product in products:

            product_specifications ={}
            product_code = product.td.span.text.strip()                                         #Code of each product

                                                                                                
            all_spec = product.find_all('tr', class_ = 'clearfix')                              #inside the grouped spec, each spec has the class 'clearfix':: grouped_spec = product.find('td', class_ ="grouped-item-spec") 
            
            for spec in all_spec:
                    spec_name = spec.th.text.strip()                                            # specification name: row .th get text and clear spaces
                    spec_value = spec.td.text.strip()                                           # specification "value" row .td get text and clear spaces

        
                    product_specifications[spec_name] = spec_value                              #save in a dictionary each specification with his "value"
           

                        
                    products_information[f"product_{product_code}"] = product_specifications        #locate product code: acces first .td,first.span,obtain the text,remove spaces

    
        #save file with the information of all products as .json

        file_name = "OptoSigmaProducts.json"

        with open(file_name, 'w') as json_file:                                             #open the json file and write (or overwrite) all in

            json.dump(products_information, json_file, indent=4)                            #write the dictionari as a json_fiel
    

        print(f"Information saved as {file_name}")


    
    else:
        print('Check possible errors: Status code =', response.status_code)
except requests.exceptions.RequestException:
    print('Error during HTTP request')




