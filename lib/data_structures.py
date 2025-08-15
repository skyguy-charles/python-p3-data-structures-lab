spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    """Return a list of names from the spicy_foods list."""
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    """Return only foods with heat_level > 5."""
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    """Print each spicy food in the required format to stdout."""
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """Return the first food dictionary matching the given cuisine."""
    return next((food for food in spicy_foods if food["cuisine"] == cuisine), None)

def print_spiciest_foods(spicy_foods):
    """Print only the spiciest foods (heat_level > 5) to stdout."""
    for food in get_spiciest_foods(spicy_foods):
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_average_heat_level(spicy_foods):
    """Return integer average of heat levels."""
    return sum(food["heat_level"] for food in spicy_foods) // len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    """Append a new spicy food dict and return the updated list."""
    spicy_foods.append(spicy_food)
    return spicy_foods
