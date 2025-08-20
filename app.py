import streamlit as st
from daten import load_recipes, data_quality
from rezepte import overview_rezepte
from zubereitung import detailview_rezepte
from einkaufsliste import create_shopping_list

# Set page config
st.set_page_config(
    page_title="Rezepte",
    page_icon="🍲",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def main():    
    # Load recipes
    recipes = load_recipes()
    data_quality(recipes)
    selected_ids = []    

    # Übersicht Rezepte
    # -----
    if 'selected_recipe' not in st.session_state:
        overview_rezepte(recipes, selected_ids)

        # Erstellen der Einkaufsliste
        # -----
        selected_count = len([key for key in st.session_state if key.startswith('recipe_') and st.session_state[key]])
        if selected_count > 0:
            with st.container():
                c1, c2 = st.columns(2)
                with c1:
                    st.write("Anzahl Personen")
                with c2:
                    st.number_input("Anzahl der Personen", label_visibility="hidden", 
                    min_value=1, value=2, step=1, max_value=10, key="number_of_people")
            if st.button("Einkaufsliste erstellen"):
                selected_recipe_keys = [key for key in st.session_state if key.startswith('recipe_') and st.session_state[key]]
                shopping_list = create_shopping_list(recipes, selected_recipe_keys, st.session_state.number_of_people)
                st.code(shopping_list)
                st.success("Kopiere die Einkaufsliste und füge sie in deine Notizen-App ein!")

    # Detailansicht Rezepte
    # -----
    else:
        detailview_rezepte(recipes)

if __name__ == "__main__":
    main()
