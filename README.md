## IRRF - Mike's iRobot Recipe Finder
Eating out is expensive and coming up with different recipes every night is a headache, so why not have an application do it for you?
Input ingredients you have in your fridge and the Recipe Finder will find a recipe to cook!

## Motivation
This project began as my submission for the iRobot Cloud Software Team Take Home Assignemnt. It will live on as a way for me to practice CI, improve on my documentation, and develop more rigorous testing.

## Tech/framework used
<b>Built with</b>
- [Python](https://www.python.org/)
- [Google](https://www.google.com/)

## Installation
1. Copy this repository
2. Create an account on [Spoonacular](https://spoonacular.com/food-api) and obtain an API key
3. Take the API key given to you and put it into config.py in the space marked "YOUR-API-KEY-HERE" (keeping the quotation marks).
You will be ready to run RecipeFinder.py!

## API Reference
[Spoonacular API](https://spoonacular.com/food-api/docs/)

## Tests
- Test_ingredients_module - tests with positive, negative, and null inputs
- Test_inputToList_module - ensures the ingredients list is in the accepted format and returns the input as a list
- Test_getRecipeByIngredients_module - checks for a valid response code using your API key

## How to use?
1. Input ingredients you have on hand in the format AAA, BBB, CCC (ie. apples, butter, cheese).
2. The Recipe Finder will look up a recipe using as many of your ingredients as possible and display it for you. If you accept the recipe, it will be added to your Recipe List and the missing ingredients will be added to your Shopping List. If you reject the recipe, the Recipe Finder will look for another recipe for you.
3. Once you are done adding recipes to your list, the Recipe Finder will print out your Recipe List and Shopping List.

## Known Problems/Bugs
- Rejecting recipe does not properly display a new recipe
- Recipe titles are not properly displayed after finishing your shopping list

## Future Improvements
- Add tests with maximal coverage of cases
- Divide project into modules
- Break down getRecipesByIngredients into seperate functions

## License
MIT © [Michael Cheung](https://www.tmikec.com)
