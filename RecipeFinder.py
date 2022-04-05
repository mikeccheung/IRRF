import requests
import config


recipeList = []

## ingredients_module.py - input prompt for ingredients
def getIngredients():
    ingredients = str(input("What ingredients do you have on hand?\nSeperate with commas (ie. apple, cheese, butter.)\n"))
    parsedIngredients = (inputToList(ingredients))
    return parsedIngredients

## inputToList_module.py - changes inputs to a list
## TODO: add input validation
def inputToList(string):
    ingrList = list(string.split(", "))
    return ingrList


## getRecipeByIngredients_module.py - Calls API to find recipe with the inputted ingredients
def getRecipeByIngredients(ingredients, missingIngredients, index):
    acceptReject = "n"
    parameters = {
        'apiKey': config.api_key,
        'fillIngredients': False,
        'ingredients': ingredients,
        'limitLicense': True,
        'number': 15,
        'ranking': 1
    }
    endpoint = "https://api.spoonacular.com/recipes/findByIngredients"
    r = requests.get(endpoint, params=parameters)
    results = r.json()
    for x in results[0 + index]["missedIngredients"]:
        missingIngredients.append(x["name"])

    title = results[0 + index]['title']
    print("You can make " + title)
    acceptReject = input("Would you like to add this to your Recipe List? (Y/N)\n")
    acceptReject.lower()
    if acceptReject == "y":
        recipeList.append(title)
        return missingIngredients
    else:
        return


## main.py - calls modules, displays results
if __name__ == '__main__':
    done = 0
    missingIngredients = []
    index = 0

    print("Welcome to the Recipe Finder, the smart way to eat.")
    ingredients = getIngredients()

    while done == 0:
        getRecipeByIngredients(ingredients, missingIngredients, index);
        theyDone = input("Are you finished with your list? (Y/N)\n")
        index += 1
        theyDone.lower()
        if theyDone == "y":
            done = 1
    missingIngredients = list(dict.fromkeys(missingIngredients))
    print("You are missing the following ingredients: " + ", ".join(missingIngredients))
    print("You will be able to make the following recipes: " + ", ".join(recipeList))
