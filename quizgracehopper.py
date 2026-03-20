import streamlit as st

# ---------------- CONFIGURAÇÃO INICIAL ----------------
st.set_page_config(page_title="Quiz Grace Hopper", layout="centered")

# Inicialização do estado
if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"
    st.session_state.q_atual = 0
    st.session_state.total = 0
    st.session_state.mostrar_resultado = False
    st.session_state.acertou = False

# ---------------- BANCO DE QUESTÕES ----------------
questoes = [
    {"pergunta": "A importância de Grace Hopper está relacionada principalmente ao fato de ela ter:",
     "opcoes": {"a": "Desenvolvido componentes físicos dos computadores modernos.",
                "b": "Trabalhado exclusivamente com hardware.",
                "c": "Criado sistemas de navegação militar.",
                "d": "Tornado a programação mais próxima da linguagem humana."},
     "correta": "d"},
    {"pergunta": "O desenvolvimento de compiladores por Grace Hopper contribuiu para:",
     "opcoes": {"a": "A eliminação das linguagens de programação.",
                "b": "A substituição dos computadores por máquinas analógicas.",
                "c": "A tradução de linguagens compreensíveis para código de máquina.",
                "d": "A criação de dispositivos físicos mais rápidos."},
     "correta": "c"},
    {"pergunta": "Ao influenciar linguagens como o COBOL, Grace Hopper promoveu:",
     "opcoes": {"a": "O uso exclusivo da programação militar.",
                "b": "A popularização de linguagens mais acessíveis.",
                "c": "A redução do uso de computadores.",
                "d": "A limitação da programação a especialistas."},
     "correta": "b"},
    {"pergunta": "Antes das contribuições de Grace Hopper, a programação era caracterizada por:",
     "opcoes": {"a": "Linguagem simples e intuitiva.",
                "b": "Forte acessibilidade ao público geral.",
                "c": "Uso predominante de interfaces gráficas.",
                "d": "Alto nível de complexidade técnica."},
     "correta": "d"},
    {"pergunta": "A transformação promovida por Grace Hopper permitiu:",
     "opcoes": {"a": "A aproximação entre humanos e máquinas.",
                "b": "A substituição da lógica de programação.",
                "c": "O fim das linguagens de programação.",
                "d": "A automação total sem necessidade de código."},
     "correta": "a"},
    {"pergunta": "A transformação promovida por Grace Hopper permitiu:",
     "opcoes": {"a": "Apenas na área militar.",
                "b": "Apenas na construção de hardware.",
                "c": "Na evolução da tecnologia e dos computadores.",
                "d": "Exclusivamente na educação básica."},
     "correta": "c"},
    {"pergunta": "A criação de compiladores pode ser entendida como um avanço porque:",
     "opcoes": {"a": "Eliminou a necessidade de computadores.",
                "b": "Facilitou a comunicação entre humanos e máquinas.",
                "c": "Tornou a programação mais complexa.",
                "d": "Substituiu os programadores."},
     "correta": "b"},
    {"pergunta": "O papel de Grace Hopper na história da computação evidencia:",
     "opcoes": {"a": "A democratização do acesso à programação.",
                "b": "A dificuldade crescente da programação.",
                "c": "A centralização do conhecimento tecnológico.",
                "d": "A limitação da informática ao meio militar."},
     "correta": "a"},
    {"pergunta": "A expressão 'linguagens mais acessíveis' indica que:",
     "opcoes": {"a": "Apenas especialistas podiam utilizá-las.",
                "b": "Eram voltadas exclusivamente para máquinas.",
                "c": "Eram mais fáceis de compreender por humanos.",
                "d": "Não utilizavam código."},
     "correta": "c"},
    {"pergunta": "Pode-se concluir que as contribuições de Grace Hopper:",
     "opcoes": {"a": "Ajudaram a moldar a computação moderna.",
                "b": "Foram irrelevantes para a informática atual.",
                "c": "Reduziram o avanço tecnológico.",
                "d": "Tiveram impacto apenas temporário."},
     "correta": "a"}
]

# ---------------- TELA INICIAL ----------------
if st.session_state.pagina == "inicio":
    st.title("GRACE HOPPER: PIONEIRA DA PROGRAMAÇÃO MODERNA")
    st.write("Seja bem-vindo ao quiz!")
    st.write(
        "Grace Hopper foi uma das figuras mais importantes da história da informática, "
        "destacando-se como cientista da computação, oficial da Marinha dos Estados Unidos "
        "e uma das principais responsáveis por transformar a forma como os computadores passaram a ser programados. "
        "Seu trabalho teve grande impacto no avanço da tecnologia, especialmente ao defender que a programação deveria ser mais simples e acessível. "
        "Entre suas contribuições mais marcantes está a criação de um dos primeiros compiladores e a influência direta no desenvolvimento do COBOL."
    )

    if st.button("Iniciar Quiz"):
        st.session_state.pagina = "quiz"

# ---------------- QUIZ ----------------
elif st.session_state.pagina == "quiz":
    q = questoes[st.session_state.q_atual]
    
    st.subheader(f"Questão {st.session_state.q_atual + 1}")
    st.write(q["pergunta"])
    
    resposta = st.radio(
        "Escolha uma opção:", 
        list(q["opcoes"].keys()),
        format_func=lambda x: f"{x.upper()}) {q['opcoes'][x]}"
    )

    # Se o usuário ainda não respondeu, mostra o botão Responder
    if not st.session_state.mostrar_resultado:
        if st.button("Responder"):
            st.session_state.mostrar_resultado = True
            st.session_state.acertou = resposta == q["correta"]
            if st.session_state.acertou:
                st.session_state.total += 10

    # Exibe resultado após responder
    if st.session_state.mostrar_resultado:
        if st.session_state.acertou:
            st.success("Você acertou!")
        else:
            st.warning("Resposta errada.")
            st.info(f"A resposta correta é: {q['correta'].upper()}) {q['opcoes'][q['correta']]}")

        # Botão para avançar para a próxima questão
        if st.button("Próxima questão"):
            st.session_state.q_atual += 1
            st.session_state.mostrar_resultado = False
            st.session_state.acertou = False
            if st.session_state.q_atual >= len(questoes):
                st.session_state.pagina = "resultado"

# ---------------- RESULTADO FINAL ----------------
elif st.session_state.pagina == "resultado":
    st.title("Resultado Final")
    st.write(f"Pontuação total: {st.session_state.total}")

    if st.session_state.total >= 80:
        st.success("Parabéns! Excelente conhecimento sobre Grace Hopper!")
    elif st.session_state.total >= 50:
        st.info("Muito bem! Você conhece grande parte da trajetória de Grace Hopper.")
    elif st.session_state.total >= 20:
        st.warning("Você está no caminho certo! Continue estudando sobre Grace Hopper.")
    else:
        st.error("Não se preocupe! Estude mais e tente novamente.")

    if st.button("Reiniciar Quiz"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_rerun()
