/*
 * groupingDishes
 * @dishes: 2D array where the first value of each inner array is the name of 
 * a dish and the following elements are the ingredients of that dish
 * Return: a 2D array where the first value of each inner array is an ingredient
 * and the following elements are the dishes that contain that ingredient.
 */
function groupingDishes(dishes) {
    let newDict = {};
    let newArr = new Array();
    let ingredients = new Array();
    let dish = '';
    
    for (let i = 0; i < dishes.length; i++) {
        for (let j = 0; j < dishes[i].length; j++) {
            if (j == 0) dish = dishes[i][j];
            else {
                if (!newDict[dishes[i][j]]) newDict[dishes[i][j]] = [dish];
                else newDict[dishes[i][j]].push(dish);
            }
        }
    }
    // sort key values, sort inner arrays, add key to inner arrays
    Object.keys(newDict).sort().map(function (key) {
        if (newDict[key].length > 1) {
            newDict[key].sort().unshift(key);
            ingredients.push(newDict[key]);
        }
    });
    return ingredients;
}
