import streamlit as st

st.title("Zähler-App")


# FALSCHER ANSATZ (nur als Kommentar sichtbar)

# count = 0
#
# if st.button("Erhöhe Zähler"):
#     count += 1
#
# st.write("Zähler:", count)

# Problem:
# Streamlit startet das Skript bei jedem Klick neu.
# Dadurch wird count immer wieder auf 0 gesetzt.






# KORREKTER ANSATZ MIT SESSION STATE

if "count" not in st.session_state:
    st.session_state.count = 0


if st.button("Zähler erhöhen"):
    st.session_state.count += 1

st.write("Aktueller Zähler:", st.session_state.count)

# Reset-Button
if st.button("Reset"):
    st.session_state.count = 0