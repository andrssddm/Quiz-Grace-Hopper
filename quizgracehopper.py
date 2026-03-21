import streamlit as st
import time  # Importado para permitir a pausa na tela

# Configuração inicial
st.set_page_config(page_title="Quiz Grace Hopper", layout="centered")

# Estilos da página
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Poppins:wght@400;600&display=swap');

    .stApp {
        background-color: #FFFFFF;
        color: #C43670;
    }

    h1 {
        font-family: 'Playfair Display', serif !important;
        color: #C43670;
    }

    h2, h3, h4, h5, h6, p, div, label {
        font-family: 'Poppins', sans-serif !important;
        color: #C43670 !important;
    }

    div.stButton > button {
        background-color: #FBD9E5;
        color: #C43670;
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
    }

    div.stButton > button:hover {
        background-color: #f7c7d8;
    }

    div[role="radiogroup"] label {
        color: #C43670 !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Inicialização do estado
if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"
    st.session_state.q_atual = 0
    st.session_state.tentativas = 1
    st.session_state.pontos = 10
    st.session_state.total = 0

TENTATIVAS = 2

# Banco de questões (Mantido conforme seu original)
questoes = [
    {
        "pergunta": "A importância de Grace Hopper está relacionada principalmente ao fato de ela ter:",
        "opcoes": {
            "a": "Desenvolvido componentes físicos dos computadores modernos.",
            "b": "Trabalhado exclusivamente com hardware.",
            "c": "Criado sistemas de navegação militar.",
            "d": "Tornado a programação mais próxima da linguagem humana."
        },
        "correta": "d"
    },
    {
        "pergunta": "O desenvolvimento de compiladores por Grace Hopper contribuiu para:",
        "opcoes": {
            "a": "A eliminação das linguagens de programação.",
            "b": "A substituição dos computadores por máquinas analógicas.",
            "c": "A tradução de linguagens compreensíveis para código de máquina.",
            "d": "A criação de dispositivos físicos mais rápidos."
        },
        "correta": "c"
    },
    {
        "pergunta": "Ao influenciar linguagens como o COBOL, Grace Hopper promoveu:",
        "opcoes": {
            "a": "O uso exclusivo da programação militar.",
            "b": "A popularização de linguagens mais acessíveis.",
            "c": "A redução do uso de computadores.",
            "d": "A limitação da programação a especialistas."
        },
        "correta": "b"
    },
    {
        "pergunta": "Antes das contribuições de Grace Hopper, a programação era caracterizada por:",
        "opcoes": {
            "a": "Linguagem simples e intuitiva.",
            "b": "Forte acessibilidade ao público geral.",
            "c": "Uso predominante de interfaces gráficas.",
            "d": "Alto nível de complexidade técnica."
        },
        "correta": "d"
    },
    {
        "pergunta": "A transformação promovida por Grace Hopper permitiu:",
        "opcoes": {
            "a": "A aproximação entre humanos e máquinas.",
            "b": "A substituição da lógica de programação.",
            "c": "O fim das linguagens de programação.",
            "d": "A automação total sem necessidade de código."
        },
        "correta": "a"
    },
    {
        "pergunta": "A transformação promovida por Grace Hopper permitiu:",
        "opcoes": {
            "a": "Apenas na área militar.",
            "b": "Apenas na construção de hardware.",
            "c": "Na evolução da tecnologia e dos computadores.",
            "d": "Exclusivamente na educação básica."
        },
        "correta": "c"
    },
    {
        "pergunta": "A criação de compiladores pode ser entendida como um avanço porque:",
        "opcoes": {
            "a": "Eliminou a necessidade de computadores.",
            "b": "Facilitou a comunicação entre humanos e máquinas.",
            "c": "Tornou a programação mais complexa.",
            "d": "Substituiu os programadores."
        },
        "correta": "b"
    },
    {
        "pergunta": "O papel de Grace Hopper na história da computação evidencia:",
        "opcoes": {
            "a": "A democratização do acesso à programação.",
            "b": "A dificuldade crescente da programação.",
            "c": "A centralização do conhecimento tecnológico.",
            "d": "A limitação da informática ao meio militar."
        },
        "correta": "a"
    },
    {
        "pergunta": "A expressão 'linguagens mais acessíveis' indica que:",
        "opcoes": {
            "a": "Apenas especialistas podiam utilizá-las.",
            "b": "Eram voltadas exclusivamente para máquinas.",
            "c": "Eram mais fáceis de compreender por humanos.",
            "d": "Não utilizavam código."
        },
        "correta": "c"
    },
    {
        "pergunta": "Pode-se concluir que as contribuições de Grace Hopper:",
        "opcoes": {
            "a": "Ajudaram a moldar a computação moderna.",
            "b": "Foram irrelevantes para a informática atual.",
            "c": "Reduziram o avanço tecnológico.",
            "d": "Tiveram impacto apenas temporário."
        },
        "correta": "a"
    }
]

# ---------------- TELA INICIAL ----------------
if st.session_state.pagina == "inicio":
    st.markdown(
    "<h1 style='color:#C43670;'>GRACE HOPPER: PIONEIRA DA PROGRAMAÇÃO MODERNA.</h1>",
    unsafe_allow_html=True
)
    st.write("Seja bem-vindo ao quiz!")
    st.write("Grace Hopper foi uma das figuras mais importantes da informática, atuando como cientista da computação, oficial da Marinha dos Estados Unidos e ajudando a transformar a forma de programar. Desenvolvendo um dos primeiros compiladores e influenciando a criação de linguagens mais acessíveis, como o COBOL.")

    if st.button("Iniciar Quiz"):
        st.session_state.pagina = "quiz"
        st.rerun()

# ---------------- QUIZ ----------------
elif st.session_state.pagina == "quiz":
    q = questoes[st.session_state.q_atual]

    st.markdown(
    f"<h2 style='font-family: Playfair Display; color:#C43670;'>⤷ Questão {st.session_state.q_atual + 1}</h2>",
    unsafe_allow_html=True
)

    st.markdown(
    f"<p style='color:#C43670;'>• {q['pergunta']}</p>",
    unsafe_allow_html=True
)
    
    resposta = st.radio("Escolha uma opção:", list(q["opcoes"].keys()),
                        format_func=lambda x: f"{x.upper()}) {q['opcoes'][x]}")

    if st.button("Responder"):
        if resposta == q["correta"]:
            # LOGICA DE ACERTO ADICIONADA AQUI
            st.balloons()
            if st.session_state.tentativas == 1:
                st.success("Parabéns, você acertou a questão! +10 pontos")
            else:
                st.session_state.pontos -= 5
                st.success(f"Parabéns, você acertou a questão! Acertou na {st.session_state.tentativas}ª tentativa! +{st.session_state.pontos} pontos")
            
            # Pausa para o usuário ler a mensagem de sucesso
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
                st.error(f"Resposta errada. A correta era: {q['correta'].upper()}")
                time.sleep(2) # Pausa para o usuário ver qual era a correta
                st.session_state.tentativas = 1
                st.session_state.pontos = 10
                st.session_state.q_atual += 1

                if st.session_state.q_atual >= len(questoes):
                    st.session_state.pagina = "resultado"

                st.rerun()

# ---------------- RESULTADO FINAL ----------------
elif st.session_state.pagina == "resultado":
    st.title("Resultado Final")
    st.write(f"Pontuação total: {st.session_state.total}")

    if st.session_state.total >= 80:
        st.success("Parabéns! Você mostrou um ótimo conhecimento sobre Grace Hopper e sua importância na história da computação. Continue explorando a informática!")
    elif st.session_state.total >= 50:
        st.info("Você foi muito bem no quiz! Já conhece grande parte da trajetória de Grace Hopper. Estude mais um pouco e chega ao nível máximo. Parabéns pela conquista!")
    elif st.session_state.total >= 20:
        st.warning("Você está no caminho certo! Já tens conhecimento sobre fatos importantes de Grace Hopper na história da informática, mas ainda pode aprender mais. Continue praticando!")
    else:
        st.error("Não se preocupe! Esse quiz é uma ótima forma de aprender sobre Grace Hopper e sua contribuição para a programação. Estude mais e tente novamente para ver sua evolução!")

    if st.button("Reiniciar Quiz"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
