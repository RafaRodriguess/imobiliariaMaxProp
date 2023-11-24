import streamlit as st
import time
import json
import os

#cd d:\Facens\tarefas_estrutura_dados\Imobiliaria
#streamlit run imoveis.py
json_path = './imoveis.json'

with open (json_path,'r') as f:
    data = json.load(f)
    prop = list(data.keys())    


st.title("Imobiliária MaxProp")
select_prop = st.selectbox('Selecione o Imovel:', prop)

#Separar a pág em 2 colunas


prox_contrato = max([int(contrato.split('_')[1])for contrato in data[select_prop]], default=0)+1
novo_contrato = f'Contrato_{prox_contrato}'
st.text(f'Próximo Contrato:{novo_contrato}')


with st.form(key='cadastro', clear_on_submit=True):

    data_inicial = st.text_input(f'Data Contrato Inicial:')
    dias_locados = st.text_input(f'Dias Locados:')    
    telefone = st.text_input(f'Telefone:')
    inquilino = st.text_input(f'Inquilino:')
    
    submit_button = st.form_submit_button(label="Gravar", help="Clique aqui para Registrar")

    if submit_button:
        # Adicionar o novo contrato ao JSON
        data[select_prop][novo_contrato] = {
            "Data_Contrato_Inicial": data_inicial,
            "Dias_Locados": dias_locados,
            "Inquilino": inquilino,
            "Telefone": telefone
        }

        # Salvando os dados atualizados no arquivo JSON
        with open(json_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2)

        st.success(f"Cadastro gravado com sucesso: {select_prop} - {novo_contrato}")

with st.form(key='exibir_contratos', clear_on_submit=False):

    st.write(f"Contratos do {select_prop}:")
    contratos_do_imovel = data[select_prop]
    delete_contratos = []

    for contrato, detalhe in contratos_do_imovel.items():
        checkbox = st.checkbox(contrato)
        if checkbox:
            delete_contratos.append(contrato)

        st.write(contrato)
        st.write('Cadastro:', detalhe)

    if st.form_submit_button('Apagar Contratos Selecionados') and delete_contratos:
        for contrato in delete_contratos:
            del data[select_prop][contrato]

        with open(json_path,'w',encoding='utf-8')as file:
            json.dump(data,file,indent=2)

        st.success(f'Contrato(os) apagado(os) com Sucesso!: {delete_contratos}')