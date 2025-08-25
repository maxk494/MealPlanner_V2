import streamlit as st
from m1_daten import input_rezepte_all, data_quality, input_top10_rezepte, input_top5_snacks, input_frühstück
from m2_rezepte_list import auflistung_rezepte
from m3_rezepte_details import details_rezepte
from m4_einkaufsliste import create_shopping_list

# Set page config
st.set_page_config(
    page_title="Rezepte",
    page_icon="🍲",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def main():    
    # Load recipes
    rezepte = input_rezepte_all()
    data_quality()
    selected_ids = []    

    # Übersicht Rezepte
    # -----
    if 'selected_recipe' not in st.session_state:
        auflistung_rezepte(input_top10_rezepte(), selected_ids, "Top10-Rezepte")
        auflistung_rezepte(input_top5_snacks(), selected_ids, "Top5-Snacks")
        auflistung_rezepte(input_frühstück(), selected_ids, "Frühstück")

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
                shopping_list = create_shopping_list(rezepte, selected_recipe_keys, st.session_state.number_of_people)
                st.success("Kopiere die Liste und füge sie in deine Notizen-App ein!")
                st.code(shopping_list)

    # Detailansicht Rezepte
    # -----
    else:
        details_rezepte(rezepte)

if __name__ == "__main__":
    main()
