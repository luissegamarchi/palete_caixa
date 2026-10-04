import streamlit as st
from banco_dados.db import criar_usuario, listar_tipos_status, listar_tipos_usuario

def pagina_criar():
    st.header(":heavy_plus_sign: Criar Usuário")

    opcoes_tipo_usuarios = listar_tipos_usuario()
    opcoes_tipos_status = listar_tipos_status()

    with st.form("form_criar"):
        col1, col2 = st.columns(2)
        cnpj = col1.text_input("CNPJ", placeholder="xxxxxxxx000xxx")
        nome_fantasia = col1.text_input("Nome Fantasia", placeholder="Inserir Nome Fantasia")
        telefone = col1.text_input("Telefone", placeholder= "+55 (011) 91234-5678", autocomplete="tel")
        razao_social = col2.text_input("Razão Social", placeholder="Inserir Razão Social")
        nome_contato = col2.text_input("Nome do Contato", placeholder="Inserir Nome do Contato")
        email = col2.text_input("E-mail", type="email", placeholder="Inserir E-mail")

        st.divider()

        col1, col2 = st.columns(2)
        nome_usuario = col1.text_input("Nome de Usuário", placeholder="Inserir Nome de Usuário")
        senha = col1.text_input("Senha", type="password", placeholder="Mínimo 6 caracteres.")
        tipo = col2.selectbox("Tipo do Usuário", opcoes_tipo_usuarios)
        confirmar = col2.text_input("Confirmar Senha",type="password", placeholder="Confirme a Senha")

        criar = st.form_submit_button("Criar Usuário")

    if criar:
        erros = []
        if not cnpj or len(cnpj) != 14 or not cnpj.isdigit():
            erros.append("CNPJ deve ter exatamente 14 dígitos numéricos")

        if not razao_social:
            erros.append("Razão Social é um campo obrigatório.")

        if not nome_usuario:
            erros.append("Nome de Usuário é um campo obrigatório.")

        if not senha:
            erros.append("Senha é um campo obrigatório.")
        elif len(senha) < 6:
            erros.append("Senha deve ter pelo menos 6 caracteres.")
        elif senha != confirmar:
            erros.append("Confirmação de Senha não coincide com a senha digitada.")

        if erros:
            for e in erros:
                st.warning(e)
            return

        dados = {
            "cnpj": cnpj,
            "razao_social": razao_social,
            "nome_fantasia": nome_fantasia,
            "nome_contato": nome_contato,
            "telefone_contato": telefone,
            "nome_usuario": nome_usuario,
            "status": "ativo",
            "tipo": tipo,
        }
        erro = criar_usuario(dados, senha)
        if erro:
            st.error(erro)
        else:
            st.success(f"Usuário **{nome_usuario}** criado com sucesso!")