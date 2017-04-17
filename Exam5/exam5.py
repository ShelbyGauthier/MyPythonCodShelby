import Epic
import json

def openJson():
    JsonText = ""
    File = open('PetStore.json')
    for line in File:                      
        line = line.strip()
        JsonText = JsonText + line
    petstore = json.loads(JsonText)
    return petstore

def searchPetStore(category, keyword, userInput):
    
    store = openJson()
    
                                    #capitalzie the first letter of category and keyword
    category = category.title()
    keyword = keyword.title()
    

                                                #looks up category
    if keyword == "Category":                                
        for product in store:
            if product["Category"] == category:
                print (product["Product"], product["Price"])       
    
                                       #if user enters c it will print category
    if userInput == "c":
        print "Enter a category"
        keyword == "Category" 
        #(product["Product"], product["Price"])
        
                                           #if user enters c it will print keyword
    if userInput == "k":
        print "Enter a keyword"
        keyword == "Keyword"
        #(product["Product"], product["Price"])
    
                              #looks up keyword    
    for product in store:
        if keyword == "Keyword": 
            if category in product["Product"]:
                print (product["Product"], product["Price"])


def main():
    userInput = Epic.userString("Search by category (c) or keyword (k)?: ")
   
                                    #lower case user input
    if userInput.lower() =='c':
        keyword = "Category"
        category = Epic.userString("Enter a category/keyword")          
        searchPetStore(category, keyword, userInput)
                                   
                                    #lower case user input
    elif userInput.lower() == 'k':
        keyword = "Keyword"
        category = Epic.userString("Enter a category/keyword")           
        searchPetStore(category, keyword, userInput)
        
main()