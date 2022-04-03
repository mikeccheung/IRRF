import requests
import config


print("Welcome to the Recipe Finder, the smart way to eat.")

done = 0
ingrList = []
shoppingList = []

ingredients = str(input("What ingredients do you have on hand?\nSeperate with commas (ie. apple, cheese, butter.)\n"))

## change inputs to a list
def inputToList(string):
    ingrList = list(string.split(", "))
    return ingrList

print("The ingredients you've entered are:")
print(inputToList(ingredients))

answer = ""
ans = input("Continue? (Y/N)\n")

payload = 0
results = []

# Calls API to find recipe with the inputted ingredients
def getRecipeByIngredients():
    parameters = {
        'apiKey' : config.api_key,
        'fillIngredients': False,
        'ingredients': ingredients,
        'limitLicense': True,
        'number': 1,
        'ranking': 1
        }
    endpoint = "https://api.spoonacular.com/recipes/findByIngredients"
    r = requests.get(endpoint, params=parameters)
    results = r.json()
    # need to log missed ingredients and append them to a shopping list
    title = results[0]['title']
    iMissed = results[0]['missedIngredientCount']
    iUsed = results[0]['usedIngredientCount']
#    print(iUsed)
#    print(title)
#    print(iMissed)
    return "You can make " + title + "\n     using " + str(iUsed) + " of your ingredients\n     and you're only missing " + str(iMissed) + " other ingredients!"
    
res = getRecipeByIngredients()

print(res)
