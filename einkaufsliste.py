def create_shopping_list(recipes, selected_recipe_keys):
    # Initialize a dictionary to aggregate ingredients
    shopping_list = {}
    
    # Get all selected recipes
    selected_recipes = [r for r in recipes if f"recipe_{r['Rezeptname']}" in selected_recipe_keys]
    
    # Aggregate ingredients
    for recipe in selected_recipes:
        for ingredient, amount in recipe["Zutaten und Mengen"].items():
            if ingredient in shopping_list:
                # If ingredient exists, try to add the amounts
                try:
                    # Extract numbers from strings like "200 g" -> 200
                    current_quantity = float(''.join(filter(str.isdigit, shopping_list[ingredient])))
                    additional_quantity = float(''.join(filter(str.isdigit, amount)))
                    shopping_list[ingredient] = f"{int(current_quantity + additional_quantity)} {amount.split()[-1] if len(amount.split()) > 1 else ''}"
                except:
                    # If can't add numerically, just append
                    shopping_list[ingredient] = f"{shopping_list[ingredient]}, {amount}"
            else:
                shopping_list[ingredient] = amount
    
    # Format the shopping list as text
    shopping_text = "Einkaufsliste\n"
    shopping_text += "="*15 + "\n"
    for ingredient, amount in shopping_list.items():
        shopping_text += f" {ingredient}: {amount}\n"
    
    return shopping_text


