import streamlit as st
import pickle

def main():

    # Cargamos el modelo entrenado
    with open("modelo_entrenado.pkl", "rb") as file:
        modelo = pickle.load(file)

    st.title("Prueba Modelo ML")

    # "Sex"
    sexo = ["male", "female"]
    sexo_input = st.radio(label="Indique su sexo", options= sexo, index=None)
    if sexo_input != None:
        st.write(f"Sexo determinado: {sexo_input}")

    # "Age"
    edad_input = st.slider(label="Introduzca edad", min_value=0, max_value=100, value=25, step=1)
    st.write(f"Edad Introducida: {edad_input}")

    # "Pclass"
    clases = [1, 2, 3]
    clase_input = st.radio(label="Indique clase", options= clases, index=None)
    if clase_input != None:
        st.write(f"Clase pasajero: {clase_input}") 

    #"Fare"
    tarifa_input = st.number_input(label="Introduzca tarifa", value= 0, min_value=0, max_value=1_000, step="float")
    if tarifa_input != None:
        st.write(f"Tarifa pagada: {tarifa_input}") 

    #"Sibsp"
    familiares_input = st.slider(label="Introduzca nº familiares embarcados", min_value=0, max_value=20, value=0, step=1)
    st.write(f"Familiares embarcados: {familiares_input}")

    #"Parch"
    parientes_input = st.slider(label="Introduzca nº familiares embarcados", min_value=0, max_value=20, value=0, step=1)
    st.write(f"Parientes embarcados: {parientes_input}")

    # "Embarked"
    ciudades = ["Cherbourg", "Southampton", "Queenstown"]
    st.text("En qué ciudad ha embarcado?")
    ciudad_input = st.radio(label="Ciudad de embarque", options=ciudades, index=None)
    if ciudad_input != None:
        st.write(f"Ciudad en la que ha embarcado: {ciudad_input}")

    #"Title"
    titulos = [' Mr', ' Mrs', ' Miss', ' Master', ' Don', ' Rev', ' Dr', ' Mme',
' Ms', ' Major', ' Lady', ' Sir', ' Mlle', ' Col', ' Capt',
' the Countess', ' Jonkheer']
    titulo_input = st.radio(label="Indique título", options= titulos, index=None)
    if titulo_input != None:
        st.write(f"Título: {titulo_input}")

    
    
    
if __name__ == "__main__":
    main()