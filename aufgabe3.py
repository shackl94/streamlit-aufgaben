import streamlit as st
import pandas as pd

#styling
st.markdown("""
<style>

.stApp {
    background-color: white;
}

h1, h2, h3 {
    color: #2e5e3e;
}

[data-testid="stDataFrame"] {
    background-color: #d8f3dc;
    border-radius: 10px;
    padding: 10px;
    border: 1px solid #b7e4c7;
}

[data-testid="metric-container"] {
    background-color: #ecfdf0;
    border: 1px solid #b7e4c7;
    padding: 15px;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

st.title("Mini-Dashboard mit Layout und Caching,shackl")

@st.cache_data
def lade_daten():
    return pd.read_csv("verkaufsdaten.csv")

df = lade_daten()

st.subheader("Filter")

kategorie = st.selectbox(
    "Wähle eine Kategorie:",
    df["Kategorie"].unique()
)

gefiltert = df[df["Kategorie"] == kategorie]

spalte1, spalte2 = st.columns(2)

durchschnitt = gefiltert["Umsatz"].mean()
maximum = gefiltert["Umsatz"].max()

spalte1.metric("Durchschnittlicher Umsatz", f"{durchschnitt:.2f} €")
spalte2.metric("Maximaler Umsatz", f"{maximum:.2f} €")

st.subheader("Gefilterte Daten")
st.dataframe(gefiltert)