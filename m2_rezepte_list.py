import streamlit as st

def auflistung_rezepte(rezepte, ids):
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
                text-align: center;
            }
            .st-emotion-cache-162xg8y {
                display: None;
            }
            .st-emotion-cache-1k5fi8b {
                display: None;
            }
            .st-emotion-cache-1py5frv {
                height: auto;
                width: 70px;
            }
            #top10-rezepte {
                text-align: left;
            }
            #number_input_1 {
                padding: 0px;
                text-align: center;
            }
            @media (max-width: 640px) {
                .st-emotion-cache-13b5x70 {
                    min-width: calc(10% - 1.5rem);
                }
                .st-emotion-cache-3writm {
                    min-width: calc(10% - 1.5rem);
                }
                .st-emotion-cache-106pc2n {
                    min-width: calc(30% - 1.5rem);
                }
            }
        </style>
        ''', unsafe_allow_html=True)

    # Überschrift
    st.markdown('<h1 style="font-size: 1.5rem; margin-bottom: 1rem; padding: 0px">🍲 Top10 Rezepte</h1>', unsafe_allow_html=True)
    
    # Auflistung Rezepte mit Checkbox
    with st.container():
        for rezept in rezepte:
                c1, c2 = st.columns([0.1, 0.9])
                with c1:
                    # Initialize session_state for the checkbox if it doesn't exist
                    is_selected = st.checkbox(
                        "x", key=f"recipe_{rezept['Rezeptname']}", value=rezept['Rezeptname'] in ids, label_visibility="hidden")
                with c2:
                    recipe_index = '[' + str(rezepte.index(rezept) + 1) + '] ' 
                    if st.button(
                        recipe_index + rezept['Rezeptname'],
                        key=f"btn_{rezept['Rezeptname']}",
                        help=rezept['Rezeptname']
                    ):
                        st.session_state.selected_recipe = rezept["Rezeptname"]
                        st.rerun()
    