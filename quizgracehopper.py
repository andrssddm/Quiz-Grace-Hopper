import streamlit as st
import time

# Configuração inicial
st.set_page_config(page_title="Quiz Grace Hopper", layout="centered")

# --- CSS Customizado (Fundo Branco + Detalhes em Rosa/Terroso) ---
st.markdown("""
    <style>
    /* 1. Fundo da página totalmente branco */
    .stApp {
        background-color: #FFFFFF;
    }

    /* 2. Textos em tom marrom rosado para contraste no fundo branco */
    h1, h2, h3, p, span {
        color: #8C565F !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }

    /* 3. Estilo das opções do Radio Button */
    div[data-testid="stRadio"] label {
        color: #8C565F !important;
        font-weight: bold;
    }

    /* 4. Estilo dos Botões */
    div.stButton > button:first-child {
        background-color: #A97A81;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
    }

    div.stButton > button:first-child:hover {
        background-color: #8C565F;
        color: white;
    }
    </style>
    """, unsafe_allow_code=True)

# Inicialização do estado
if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"
    st.session_state.q_atual = 0
    st.session_state.tentativas = 1
    st.session_state.pontos = 10
    st.session_state.total = 0

TENTATIVAS = 2

# Banco de questões
questoes = [
    {
        "pergunta": "A importância de Grace Hopper está relacionada principalmente ao fato de ela ter:",
        "opcoes": {"a": "Desenvolvido componentes físicos.", "b": "Trabalhado com hardware.", "c": "Criado sistemas de navegação.", "d": "Tornado a programação mais humana."},
        "correta": "d"
    },
    {
        "pergunta": "O desenvolvimento de compiladores por Grace Hopper contribuiu para:",
        "opcoes": {"a": "Eliminação de linguagens.", "b": "Máquinas analógicas.", "c": "Tradução para código de máquina.", "d": "Dispositivos físicos rápidos."},
        "correta": "c"
    },
    {
        "pergunta": "Ao influenciar linguagens como o COBOL, Grace Hopper promoveu:",
        "opcoes": {"a": "Uso militar exclusivo.", "b": "Popularização de linguagens acessíveis.", "c": "Redução do uso de computadores.", "d": "Limitação a especialistas."},
        "correta": "b"
    },
    {
        "pergunta": "Antes das contribuições de Grace Hopper, a programação era:",
        "opcoes": {"a": "Simples e intuitiva.", "b": "Acessível ao público.", "c": "Uso de interfaces gráficas.", "d": "Alto nível de complexidade técnica."},
        "correta": "d"
    },
    {
        "pergunta": "A transformação promovida por Grace Hopper permitiu:",
        "opcoes": {"a": "Aproximação entre humanos e máquinas.", "b": "Substituição da lógica.", "c": "Fim das linguagens.", "d": "Automação sem código."},
        "correta": "a"
    },
    {
        "pergunta": "As contribuições de Grace Hopper impactaram:",
        "opcoes": {"a": "Apenas área militar.", "b": "Apenas construção de hardware.", "c": "Evolução da tecnologia e computadores.", "d": "Exclusivamente educação básica."},
        "correta": "c"
    },
    {
        "pergunta": "A criação de compiladores facilitou:",
        "opcoes": {"a": "Eliminação de máquinas.", "b": "Comunicação humano-máquina.", "c": "Complexidade técnica.", "d": "Substituição de programadores."},
        "correta": "b"
    },
    {
        "pergunta": "O papel de Grace Hopper evidencia:",
        "opcoes": {"a": "Democratização do acesso à programação.", "b": "Dificuldade crescente.", "c": "Centralização do conhecimento.", "d": "Limitação ao meio militar."},
        "correta": "a"
    },
    {
        "pergunta": "Linguagens mais acessíveis são:",
        "opcoes": {"a": "Para especialistas.", "b": "Voltadas para máquinas.", "c": "Mais fáceis de entender por humanos.", "d": "Sem código."},
        "correta": "c"
    },
    {
        "pergunta": "As contribuições de Grace Hopper:",
        "opcoes": {"a": "Moldaram a computação moderna.", "b": "Foram irrelevantes.", "c": "Reduziram o avanço.", "d": "Foram temporárias."},
        "correta": "a"
    }
]

# ---------------- TELA INICIAL ----------------
if st.session_state.pagina == "inicio":
    st.title("GRACE HOPPER: PIONEIRA DA PROGRAMAÇÃO")
    st.write("Grace Hopper transformou a computação ao criar o primeiro compilador e influenciar o COBOL.")
    if st.button("Iniciar Quiz"):
        st.session_state.pagina = "quiz"
        st.rerun()

# ---------------- QUIZ ----------------
elif st.session_state.pagina == "quiz":
    q = questoes[st.session_state.q_atual]
    st.subheader(f"Questão {st.session_state.q_atual + 1}")
    st.write(q["pergunta"])

    resposta = st.radio("Escolha uma opção:", list(q["opcoes"].keys()),
                        format_func=lambda x: f"{x.upper()}) {q['opcoes'][x]}")

    if st.button("Responder"):
        if resposta == q["correta"]:
            st.balloons()
            st.success("Parabéns, você acertou a questão!")
            time.sleep(2)
            st.session_state.total += st.session_state.pontos
            st.session_state.pontos = 10
            st.session_state.tentativas = 1
            st.session_state.q_atual += 1
            if st.session_state.q_atual >= len(questoes):
                st.session_state.pagina = "resultado"
            st.rerun()
        else:
            if st.session_state.tentativas < TENTATIVAS:
                st.warning("Resposta errada. Tente novamente!")
                st.session_state.tentativas += 1
            else:
                st.error(f"Errado. A correta era: {q['correta'].upper()}")
                time.sleep(2)
                st.session_state.tentativas = 1
                st.session_state.pontos = 10
                st.session_state.q_atual += 1
                if st.session_state.q_atual >= len(questoes):
                    st.session_state.pagina = "resultado"
                st.rerun()

# ---------------- RESULTADO ----------------
elif st.session_state.pagina == "resultado":
    st.title("Resultado Final")
    st.write(f"Pontuação: {st.session_state.total}")
    if st.button("Reiniciar Quiz"):
        for k in list(st.session_state.keys()): del st.session_state[k]
        st.rerun()
