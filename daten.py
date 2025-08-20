import json

def load_recipes():
    # Load recipes from JSON file
    with open('mahlzeiten.json', 'r', encoding='utf-8') as f:
        recipes = json.load(f)
    
    # Sort recipes by recipe name
    recipes = sorted(recipes, key=lambda x: x['Rezeptname'])
    
    return recipes