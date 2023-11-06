import pandas as pd
import plotly.express as px
import streamlit as st

df_vehicles = pd.read_csv('Proyecto_4/Proyect_4/DataFrame/vehicles_us.csv') #Leer los datos

#Crear botones
#-----------------------------------------------------------------------------------------
#hist_button = st.button("Construir histograma")
#hist_button_dis = st.button("Construir dispersión")
#-----------------------------------------------------------------------------------------


#Se ejecuta al hacer click en el boton
#-----------------------------------------------------------------------------------------
#if hist_button: # al hacer clic en el botón
    # escribir un mensaje
#    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
#    fig_histogram = px.histogram(df_vehicles, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
#    st.plotly_chart(fig_histogram, use_container_width=True) 


#if hist_button_dis:
    
#    st.write("Creación de una dispersión para el conjunto de datos de anuncios de venta de coches")
    
#    fig_scatter = px.scatter(df_vehicles, x="odometer", y="price") # crear un gráfico de dispersión

#    st.plotly_chart(fig_scatter, use_container_width=True) 
#-----------------------------------------------------------------------------------------


st.title("Elija tipo de grafico: ")
option_names = ["Histograma","Dispersión"]
option = st.radio("Navigation" , option_names)

if option == 'Histograma':
    
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    fig_histogram = px.histogram(df_vehicles, x="odometer")
    
    st.plotly_chart(fig_histogram, use_container_width=True) 

else:
    st.write("Creación de una dispersión para el conjunto de datos de anuncios de venta de coches")
    
    fig_scatter = px.scatter(df_vehicles, x="odometer", y="price") # crear un gráfico de dispersión

    st.plotly_chart(fig_scatter, use_container_width=True) 

