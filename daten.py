import json
import streamlit as st

def load_recipes():
    # Load recipes from JSON file
    with open('mahlzeiten.json', 'r', encoding='utf-8') as f:
        recipes = json.load(f)
    
    # Sort recipes by recipe name
    recipes = sorted(recipes, key=lambda x: x['Rezeptname'])
    
    return recipes

def data_quality():
    recipes = load_recipes()

    # Test 1: Alle Zutaten sollten die gleiche Einheit haben
    einheiten = {}
    for recipe in recipes:
        for ingredient, amount in recipe["Zutaten und Mengen"].items():
            amount, unit = amount.split()
            if ingredient not in einheiten:
                einheiten[ingredient] = unit
            else:
                if einheiten[ingredient] != unit:
                    st.error(f"Die Zutat {ingredient} hat unterschiedliche Einheiten {einheiten[ingredient]} <> {unit}.")
        