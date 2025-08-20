def create_shopping_list(recipes, selected_recipe_keys, anzahl_personen):
    # Initialize a dictionary to aggregate ingredients
    shopping_list = {}
    
    # Get all selected recipes
    selected_recipes = [r for r in recipes if f"recipe_{r['Rezeptname']}" in selected_recipe_keys]
    
    # Aggregate ingredients
    for recipe in selected_recipes:
        for ingredient, amount in recipe["Zutaten und Mengen"].items():
            amount, unit = amount.split()
            amount = int(amount) * anzahl_personen
            if ingredient in shopping_list:
                current_quantity = int(shopping_list[ingredient].split()[0])
                shopping_list[ingredient] = f"{int(current_quantity + amount)} {unit}"
            else:
                shopping_list[ingredient] = f'{amount} {unit}'
    
    # Format the shopping list as text
    shopping_text = f"Einkaufsliste für {anzahl_personen} Personen\n"
    shopping_text += "="*30 + "\n"
    for ingredient, amount in shopping_list.items():
        shopping_text += f" {ingredient}: {amount}\n"
    
    return shopping_text


