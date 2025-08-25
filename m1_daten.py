import json
import streamlit as st

def input_zutaten_mapping():
    # Laden des Mappings von Zutaten auf Kategorien aus der JSON-Datei
    with open('d1_zutaten_mapping.json', 'r', encoding='utf-8') as f:
        zutaten_mapping = json.load(f)
    return zutaten_mapping

def input_top10_rezepte():
    # Laden der Rezepte aus der JSON-Datei
    with open('d2_top10_rezepte.json', 'r', encoding='utf-8') as f:
        rezepte = json.load(f)
    
    # Sortieren der Rezepte nach dem Namen
    rezepte = sorted(rezepte, key=lambda x: x['Rezeptname'])

    return rezepte

def input_top5_snacks():
    # Laden der Rezepte aus der JSON-Datei
    with open('d3_top5_snacks.json', 'r', encoding='utf-8') as f:
        rezepte = json.load(f)
    
    # Sortieren der Rezepte nach dem Namen
    rezepte = sorted(rezepte, key=lambda x: x['Rezeptname'])
    return rezepte

def input_frühstück():
    # Laden der Rezepte aus der JSON-Datei
    with open('d4_frühstück.json', 'r', encoding='utf-8') as f:
        rezepte = json.load(f)
    
    # Sortieren der Rezepte nach dem Namen
    rezepte = sorted(rezepte, key=lambda x: x['Rezeptname'])
    return rezepte

def input_rezepte_all():
    # Zusammenführen aller Rezepte
    rezepte = input_top10_rezepte() + input_top5_snacks() + input_frühstück()
    return rezepte

def data_quality():
    '''Prüfroutinen für die Vollständigkeit und Konsistenz der Input-Daten.'''
    # Input-Daten
    rezepte = input_rezepte_all()
    zutaten_mapping = input_zutaten_mapping()

    # Test 1: Alle Zutaten sollten die gleiche Einheit haben
    einheiten_mapping = {}
    for rezept in rezepte:
        for zutat, menge in rezept["Zutaten und Mengen"].items():
            menge, einheit = menge.split()
            if zutat not in einheiten_mapping:
                einheiten_mapping[zutat] = einheit
            else:
                if einheiten_mapping[zutat] != einheit:
                    st.error(f"Die Zutat [{zutat}] hat unterschiedliche Einheiten {einheiten_mapping[zutat]} <> {einheit}.")
    
    # Test 2: Alle Zutaten sollen im Zutatenmapping enthalten sein
    zutaten_liste = []
    for k,v in zutaten_mapping.items():
        zutaten_liste += v
    
    for rezept in rezepte:
        for zutat in rezept["Zutaten und Mengen"].keys():
            if zutat not in zutaten_liste:
                st.error(f"Die Zutat [{zutat}] ist nicht im Zutaten-Mapping enthalten.")
            
        