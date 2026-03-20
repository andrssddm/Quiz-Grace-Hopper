import streamlit as st

# ---------------- CSS PERSONALIZADO ----------------
st.markdown("""
<style>
/* Fundo da página e texto principal */
.stApp {
    background-color: white;
    color: #9933FF;  /* rosa roxo */
}

/* Títulos e textos */
h1, h2, h3, h4, h5, h6, p, div {
    color: #9933FF;
}

/* Botões */
.stButton>button {
    background-color: #9933FF !important;
    color: white !important;  /* letras brancas */
    font-weight: bold;
    border-radius: 8px;
}

/* Radio buttons e checkboxes */
.stRadio, .stCheckbox {
    background-color: #9933FF !important;
    color: white !important;  /* letras brancas */
    border-radius: 8px;
    padding: 5px;
}

/* Mensagens de alerta (sucesso, erro, info, warning) */
.stAlert {
    background-color: #9933FF !important;
    color: white !important;  /* letras brancas */
    border-radius: 8px;
    padding: 10px;
}

/* Inputs de texto (se houver) */
.stTextInput>div>div {
    background-color: #9933FF !important;
    color: white !important;  /* letras brancas */
    border-radius: 8px;
    padding: 5px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- CONFIGURAÇÃO INICIAL ----------------
st.set_page_config(page_title="Quiz Grace Hopper", layout="centered")

if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"
    st.session_state.q_atual = 0
    st.session_state.tentativas = 1
    st.session_state.pontos = 10
    st.session_state.total = 0

TENTATIVAS = 2

# ---------------- BANCO DE QUESTÕES ----------------
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
    # Continue adicionando as demais questões
]

# ---------------- TELA INICIAL ----------------
if st.session_state.pagina == "inicio":
    st.title("GRACE HOPPER: PIONEIRA DA PROGRAMAÇÃO MODERNA.")
    st.write("Seja bem-vindo ao quiz!")
    st.write("Grace Hopper foi uma das figuras mais importantes da história da informática, destacando-se como cientista da computação, oficial da Marinha dos Estados Unidos e uma das principais responsáveis por transformar a forma como os computadores passaram a ser programados. Seu trabalho teve grande impacto no avanço da tecnologia, especialmente ao defender que a programação deveria ser mais simples e acessível. Entre suas contribuições mais marcantes está a criação de um dos primeiros compiladores, ferramenta capaz de traduzir comandos escritos em linguagem próxima da humana para a linguagem das máquinas. Além disso, ela influenciou diretamente o desenvolvimento do COBOL, linguagem amplamente utilizada em sistemas comerciais e administrativos, consolidando seu legado como uma das pioneiras da computação moderna.")

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
            if st.session_state.tentativas == 1:
                st.success(f"Você acertou! +{st.session_state.pontos} pontos")
            else:
                st.session_state.pontos -= 5
                st.success(f"Acertou na {st.session_state.tentativas}ª tentativa! +{st.session_state.pontos} pontos")

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
        st.success("Parabéns! Você demonstrou um excelente conhecimento sobre Grace Hopper e sua importância para a história da computação. Suas respostas mostram que você realmente entende o impacto dela no desenvolvimento da tecnologia. Continue explorando a história da informática!")
    elif st.session_state.total >= 50:
        st.info("Você foi muito bem no quiz! Mostrou que já conhece grande parte da trajetória de Grace Hopper e suas contribuições para a programação. Com um pouco mais de estudo, você chega ao nível máximo! Parabéns pela conquista!")
    elif st.session_state.total >= 20:
        st.warning("Você está no caminho certo! Já conhece alguns fatos importantes sobre Grace Hopper, mas ainda pode aprender mais sobre a história dela e sua influência na computação moderna. Continue praticando!")
    else:
        st.error("Não se preocupe! Esse quiz é uma ótima oportunidade para conhecer melhor quem foi Grace Hopper e como ela ajudou a transformar a programação e os computadores. Estude mais e tente novamente para ver a sua evolução!")

    if st.button("Reiniciar Quiz"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()
