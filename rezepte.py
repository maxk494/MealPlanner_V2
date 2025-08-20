import streamlit as st

def overview_rezepte(recipes, selected_ids):
    # Styling
    st.markdown('''
        <style>
            .st-emotion-cache-1n6tfoc {
                gap: .5rem;
            }
            .st-emotion-cache-5qfegl {
                padding: 5px 10px;
                min-height: 1rem;
                justify-content: left;
            }
            .st-emotion-cache-17c7e5f {
                font-size: .8rem;
            }
            .st-emotion-cache-r44huj {
                font-size: .8rem;
            }
            @media (max-width: 640px) {
                .st-emotion-cache-13b5x70 {
                    min-width: calc(10% - 1.5rem);
                }
                .st-emotion-cache-3writm {
                    min-width: calc(10% - 1.5rem);
                }
            }
        </style>
        ''', unsafe_allow_html=True)

    # Überschrift
    st.markdown('<h1 style="font-size: 1.5rem; margin-bottom: 1rem; padding: 0px">🍲 Rezepte</h1>', unsafe_allow_html=True)
    
    # Auflistung Rezepte mit Checkbox
    with st.container():
        for recipe in recipes:
                c1, c2 = st.columns([0.1, 0.9])
                with c1:
                    # Initialize session_state for the checkbox if it doesn't exist
                    is_selected = st.checkbox(
                        "x", key=f"recipe_{recipe['Rezeptname']}", value=recipe['Rezeptname'] in selected_ids, label_visibility="hidden")
                with c2:
                    recipe_index = '[' + str(recipes.index(recipe) + 1) + '] ' 
                    if st.button(
                        recipe_index + recipe['Rezeptname'],
                        key=f"btn_{recipe['Rezeptname']}",
                        help=recipe['Rezeptname']
                    ):
                        st.session_state.selected_recipe = recipe["Rezeptname"]
                        st.rerun()
    