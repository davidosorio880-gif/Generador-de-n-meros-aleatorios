import streamlit as st
import random

st.title('🎲 Generador de números')

st.divider()

if 'historial' not in st.session_state:
    st.session_state.historial = []

contendedor=st.container(border=True)

with contendedor:
    
    generar=False
    columna1,columna2=st.columns(2)
    
    with columna1:
        minimo=st.number_input('Mínimo: ')
    with columna2:
        maximo=st.number_input('Máximo: ')

    columna_iz,columna_boton,columna_der=st.columns([2,1,2])
    
    with columna_boton:

        if st.button('Generar'):
            generar=True
    
    if generar:
                
        if minimo==0 and maximo==0:
            st.error('Escribe máximo y mínimo.')
        elif minimo==maximo:
            st.error('Máximo y mínimo deben ser diferentes.')
        
        else:
            numero=random.randint(minimo,maximo)
            st.metric('Número generado',numero)
            st.session_state.historial.append(numero)
    st.divider()
        
    st.subheader('Historial:')
    
    for posicion, numero in enumerate(st.session_state.historial):
        st.write('{}. {}'.format((posicion+1),numero))
    
    if st.button('Borrar historial'):
        st.session_state.historial=[]
        st.rerun()

