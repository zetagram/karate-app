
import streamlit as st

st.title("Pontuação de Karatê - Estilo Shotokan")

st.write("Insira as notas dos 5 árbitros:")

notas = []
for i in range(1, 6):
    nota = st.number_input(f"Nota do Árbitro {i}", min_value=0.0, max_value=10.0, step=0.1, key=i)
    notas.append(nota)

if st.button("Calcular Pontuação Final"):
    if len(notas) != 5:
        st.error("Erro: São necessárias 5 notas.")
    else:
        maior = max(notas)
        menor = min(notas)

        notas_validas = notas.copy()
        notas_validas.remove(maior)
        notas_validas.remove(menor)

        soma = sum(notas_validas)

        st.success("Resultado da Pontuação")
        st.write(f"Notas inseridas: {notas}")
        st.write(f"Maior nota (descartada): {maior}")
        st.write(f"Menor nota (descartada): {menor}")
        st.write(f"Notas válidas: {notas_validas}")
        st.write(f"Pontuação final: **{soma:.2f}**")
