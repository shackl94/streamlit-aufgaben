import streamlit as st

st.title("Meine erste Streamlit-App")

# Streamlit führt das komplette Skript jedes Mal neu aus,
# wenn ein Widget geändert wird,zB. Texteingabe oder Slider.

name = st.text_input("Wie heißt du?")

alter = st.slider(
    "Wie alt bist du?",
    min_value=0,
    max_value=100,
    value=20
)

if name:
    st.write(f"Hallo {name}!")
else:
    st.write("Bitte gib deinen Namen ein.")

if alter >= 18:
    st.success("Du bist volljährig.")
else:
    st.warning("Du bist noch nicht volljährig.")