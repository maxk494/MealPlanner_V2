from m1_daten import input_zutaten_mapping

def create_shopping_list(rezepte, selected_rezepte_keys, anzahl_personen):
    # Initialize a dictionary to aggregate ingredients
    einkaufsliste = {}
    zutaten_mapping = input_zutaten_mapping()
    
    # Get all selected recipes
    selected_rezepte = [r for r in rezepte if f"recipe_{r['Rezeptname']}" in selected_rezepte_keys]
    
    # Aggregate ingredients
    for rezept in selected_rezepte:
        for zutat, menge in rezept["Zutaten und Mengen"].items():
            menge, einheit = menge.split()
            menge = int(menge) * anzahl_personen
            if zutat in einkaufsliste:
                menge_aktuell = int(einkaufsliste[zutat].split()[0])
                einkaufsliste[zutat] = f"{int(menge_aktuell + menge)} {einheit}"
            else:
                einkaufsliste[zutat] = f'{menge} {einheit}'
    
    # Format the shopping list as text
    text_einkaufsliste = f"Einkaufsliste für {anzahl_personen} Personen\n"
    text_einkaufsliste += "="*30 + "\n"
    
    # Categorize ingredients
    kategorisierte_zutaten = {kategorie: {} for kategorie in zutaten_mapping}
    unkategorisierte_zutaten = {}
    
    for zutat, menge in einkaufsliste.items():
        found = False
        for kategorie, zutaten in zutaten_mapping.items():
            if zutat in zutaten:
                kategorisierte_zutaten[kategorie][zutat] = menge
                found = True
                break
        if not found:
            unkategorisierte_zutaten[zutat] = menge
    
    # Add categorized ingredients to shopping text
    for kategorie, zutaten in kategorisierte_zutaten.items():
        if zutaten:  # Only add categories that have ingredients
            text_einkaufsliste += f"\n{kategorie}:\n"
            text_einkaufsliste += "-"*30 + "\n"
            for zutat, menge in sorted(zutaten.items()):
                text_einkaufsliste += f" [] {zutat}: {menge}\n"
    
    # Add uncategorized ingredients if any
    if unkategorisierte_zutaten:
        text_einkaufsliste += "\nSonstiges:\n"
        text_einkaufsliste += "-"*30 + "\n"
        for zutat, menge in sorted(unkategorisierte_zutaten.items()):
            text_einkaufsliste += f" [] {zutat}: {menge}\n"

    # Ergänzen der ausgewählten Rezepte
    text_einkaufsliste += "\nAusgewählte Rezepte\n"
    text_einkaufsliste += "="*30 + "\n"
    counter = 1
    for recipe in selected_rezepte:
        text_einkaufsliste += f" [{counter}] {recipe['Rezeptname']}\n"
        counter += 1
    return text_einkaufsliste
