import streamlit as st

st.header('Energy Calculator')

col1, col2 = st.columns(2)

with col1:
    st.subheader(':red[Potential Energy]')
    m = st.number_input('Mass: ', key = 'a')
    h = st.number_input('Height: ', key = 'b')
    if st.button('Calcultate', key = 'abc'):
        st.write(f'the potential energy is {m**10*h}')

with col2:
    st.subheader(':red[Potential Energy]')
    m = st.number_input('Mass: ', key = 'c')
    h = st.number_input('Height: ', key = 'd')
    if st.button('Calcultate', key = 'xyz'):
        st.write(f'the potential energy is {m**10*h}')
