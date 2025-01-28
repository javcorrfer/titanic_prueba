import streamlit as st
import pickle

def main():

    # Cargamos el modelo entrenado
    with open("modelo_entrenado.pkl", "rb") as file:
        modelo = pickle.load(file)

    st.title("Prueba Modelo ML")

    ciudades = ["Cherbourg", "Southampton", "Queenstown"]
    st.text("En qué ciudad ha embarcado?")
    ciudad = st.selectbox(label="Ciudad de embarque", options=ciudades, index=None)

    st.write(f"Ciudad en la que ha embarcado: {ciudad}")



if __name__ == "__main__":
    main()