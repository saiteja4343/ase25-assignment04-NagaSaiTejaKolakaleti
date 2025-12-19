# SmartCater - Ingredient Ordering Service

# Here, we lets users search for meals by name, ingredient, or category

class Meal:
    def __init__(self, name, ingredients, category):
        self.name = name
        self.ingredients = ingredients  # list of ingredient names
        self.category = category  # e.g., "vegan", "gluten-free", "quick meals"
    
    def __str__(self):
        return f"{self.name} ({self.category})"

class MealCatalog:
    def __init__(self):
        self.meals = []
    
    def add_meal(self, meal):
        # adds a new meal to the catalog
        self.meals.append(meal)
    
    def search_by_name(self, name):
        # search for meals that contain the search term in their name
        results = []
        search_term = name.lower()
        for meal in self.meals:
            if search_term in meal.name.lower():
                results.append(meal)
        return results
    
    def search_by_ingredient(self, ingredient):
        # find meals that contain a specific ingredient
        results = []
        search_term = ingredient.lower()
        for meal in self.meals:
            for ing in meal.ingredients:
                if search_term in ing.lower():
                    results.append(meal)
                    break  # makes sure we don't add the same meal twice
        return results
    
    def search_by_category(self, category):
        # filter meals by category like vegan or gluten-free
        results = []
        search_term = category.lower()
        for meal in self.meals:
            if search_term in meal.category.lower():
                results.append(meal)
        return results
    
    def display_results(self, results, search_type):
        # helper method to print search results nicely
        if len(results) == 0:
            print(f"No meals found for {search_type}")
        else:
            print(f"\nFound {len(results)} meal(s) for {search_type}:")
            for meal in results:
                print(f"  - {meal.name}")
                print(f"    Category: {meal.category}")
                print(f"    Ingredients: {', '.join(meal.ingredients)}")
                print()

def main():
    print(" SmartCater Meal Search Demo\n")
    
    # create catalog and add sample meals
    catalog = MealCatalog()
    
    # adding some sample meals found in the internet
    catalog.add_meal(Meal(
        "Pasta Carbonara",
        ["pasta", "eggs", "bacon", "parmesan cheese", "black pepper"],
        "quick meals"
    ))
    
    catalog.add_meal(Meal(
        "Vegan Buddha Bowl",
        ["quinoa", "chickpeas", "avocado", "spinach", "tahini"],
        "vegan"
    ))
    
    catalog.add_meal(Meal(
        "Grilled Chicken Salad",
        ["chicken breast", "lettuce", "tomatoes", "cucumber", "olive oil"],
        "gluten-free"
    ))
    
    catalog.add_meal(Meal(
        "Vegetable Stir Fry",
        ["broccoli", "carrots", "bell peppers", "soy sauce", "rice"],
        "vegan"
    ))
    
    catalog.add_meal(Meal(
        "Chicken Tacos",
        ["chicken breast", "tortillas", "lettuce", "cheese", "salsa"],
        "quick meals"
    ))
    
    catalog.add_meal(Meal(
        "Gluten-Free Pizza",
        ["gluten-free dough", "tomato sauce", "mozzarella", "basil"],
        "gluten-free"
    ))
    
    print("Welcome! We have 6 meals in our catalog.\n")
    
    # demo 1: search by name
    print(" Demo 1: Search by Name")
    results = catalog.search_by_name("chicken")
    catalog.display_results(results, "name 'chicken'")
    
    # demo 2: search by ingredient
    print(" Demo 2: Search by Ingredient")
    results = catalog.search_by_ingredient("lettuce")
    catalog.display_results(results, "ingredient 'lettuce'")
    
    # demo 3: search by category
    print(" Demo 3: Search by Category")
    results = catalog.search_by_category("vegan")
    catalog.display_results(results, "category 'vegan'")
    
    # demo 4: search that returns no results
    print(" Demo 4: Search with No Results")
    results = catalog.search_by_name("burger")
    catalog.display_results(results, "name 'burger'")
    
    print(" Demo Completed!!!")

if __name__ == "__main__":
    main()
