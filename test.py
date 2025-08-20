import json
import pandas as pd

# Load the JSON data
with open("mahlzeiten.json", "r", encoding="utf-8") as f:
    recipes = json.load(f)

# Create DataFrame 1: Recipe summary
df_summary = pd.DataFrame([
    {
        'Rezeptname': recipe['Rezeptname'],
        'Zubereitung': recipe['Zubereitung'],
        'Kohlenhydrate': recipe['Kohlenhydrate'],
        'Proteine': recipe['Proteine'],
        'Fett': recipe['Fett'],
        'Kalorien': recipe['Kalorien']
    }
    for recipe in recipes
])

# Create DataFrame 2: Ingredients list
ingredients_list = []
for recipe in recipes:
    for zutat, menge in recipe['Zutaten und Mengen'].items():
        ingredients_list.append({
            'Rezeptname': recipe['Rezeptname'],
            'Zutat': zutat,
            'Menge': menge
        })

df_ingredients = pd.DataFrame(ingredients_list)
df_ingredients[['Menge', 'Einheit']] = df_ingredients['Menge'].str.split(' ', n=1, expand=True)
# Convert Menge to float for numerical operations
df_ingredients['Menge'] = pd.to_numeric(df_ingredients['Menge'].str.replace(',', '.'), errors='coerce')


# Display the first few rows of each DataFrame
print("\n=== Rezeptübersicht ===")
print(df_summary.head())

print("\n=== Zutatenliste ===")
print(df_ingredients.head())

