import requests
import config


def getIngredients(missingIngredients):
    ingredients = str(input("What ingredients do you have on hand?\nSeperate with commas (ie. apple, cheese, butter.)\n"))
    parsedIngredients = (inputToList(ingredients))
    res = getRecipeByIngredients(parsedIngredients, missingIngredients)

## change inputs to a list
def inputToList(string):
    ingrList = list(string.split(", "))
    return ingrList


# Calls API to find recipe with the inputted ingredients
def getRecipeByIngredients(ingredients, missingIngredients):
    i = 0
    acceptReject = "reject"
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
    for x in results[0 + i]["missedIngredients"]:
        missingIngredients.append(x["name"])

    title = results[0 + i]['title']
    print("You can make " + title)
    acceptReject = input("Accept or Reject? (Accept/Reject)\n")
    i = i + 1

    if acceptReject.lower == "accept":
        return missingIngredients
    else:
        return

if __name__ == '__main__':
    done = 0
    missingIngredients = []
    recipeList = []

    print("Welcome to the Recipe Finder, the smart way to eat.")

    while done == 0:
        getIngredients(missingIngredients);
        theyDone = input("Are you finished with your list? (Y/N)\n")
        if theyDone.lower() == "y":
            done = 1
    missingIngredients = list(dict.fromkeys(missingIngredients))
    print("You are missing the following ingredients: " + ", ".join(missingIngredients))
    print("You will be able to make the following recipes: " + ", ".join(recipeList))
