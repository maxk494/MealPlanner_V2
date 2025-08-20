import streamlit as st

def detailview_rezepte(recipes):
    # Styling
    st.markdown('''
        <style>
            .st-emotion-cache-5qfegl {
                width: 75px;
                min-height: 1rem;
            }
            .st-emotion-cache-17c7e5f {
                font-size: .8rem;
            }
            .st-emotion-cache-gi0tri {
                display: None;
            }
            .st-emotion-cache-1n6tfoc {
                background-color: #f0f0f0;
                padding: 5px;
            }
            .st-emotion-cache-18kf3ut {
                text-align: center;
            }
            .st-emotion-cache-15jn9ue {
                display: inline-block;
            }
            .st-emotion-cache-r44huj {
                margin-bottom: 0px;
            }
            @media (max-width: 640px) {
                .st-emotion-cache-106pc2n {
                    min-width: calc(50% - 1.5rem);
                }
            }
        </style>
        ''', unsafe_allow_html=True)

    # Rezeptauswahl
    selected_recipe = next((r for r in recipes if r["Rezeptname"] == st.session_state.selected_recipe), None)
        
    if selected_recipe:
        # Back button
        if st.button("← Zurück", use_container_width=True, key="back_button"):
            del st.session_state.selected_recipe
            st.rerun()

        # Überschrift
        st.markdown(f'<h1 style="font-size: 1.2rem; margin-top: 0rem; margin-bottom: 1rem; padding: 0px">{selected_recipe["Rezeptname"]}</h1>', unsafe_allow_html=True)
            
        # Makronährstoffe
        with st.container():
            a, b = st.columns(2)
            c,d = st.columns(2)

            a.metric("Kalorien", str(selected_recipe['Kalorien'])+' kcal')
            b.metric("Proteine", str(selected_recipe['Proteine'])+'g')
            c.metric("Kohlenhydrate", str(selected_recipe['Kohlenhydrate'])+'g')
            d.metric("Fett", str(selected_recipe['Fett'])+'g')
            
        # Zutaten
        st.markdown(f'<h1 style="font-size: 1.2rem; margin-top: 0rem; padding: 0px">Zutaten</h1>', unsafe_allow_html=True)
        ingredients_html = '<ul class="ingredient-list" style="padding-left: 20px;">'
        for ingredient, amount in selected_recipe["Zutaten und Mengen"].items():
            ingredients_html += f'<li>{ingredient}: <strong>{amount}</strong></li>'
        ingredients_html += '</ul>'
        st.markdown(ingredients_html, unsafe_allow_html=True)
            
        # Zubereitung
        with st.container():
            st.markdown(f'<h1 style="font-size: 1.2rem; margin-top: 0rem; padding: 0px; text-align: left;">Zubereitung</h1>', unsafe_allow_html=True)
            st.markdown(f'<div style="line-height: 1.6; text-align: left; margin-bottom: 0px;">{selected_recipe["Zubereitung"]}</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)