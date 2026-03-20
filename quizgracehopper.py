if st.button("Responder"):
    if resposta == q["correta"]:
        # Mensagem de acerto
        if st.session_state.tentativas == 1:
            st.success(f"Parabéns! Você acertou de primeira! +{st.session_state.pontos} pontos")
        else:
            st.session_state.pontos -= 5
            st.success(f"Acertou na {st.session_state.tentativas}ª tentativa! +{st.session_state.pontos} pontos")
        
        # Atualiza pontuação e passa para próxima questão
        st.session_state.total += st.session_state.pontos
        st.session_state.pontos = 10
        st.session_state.tentativas = 1
        st.session_state.q_atual += 1

        # Verifica se acabou o quiz
        if st.session_state.q_atual >= len(questoes):
            st.session_state.pagina = "resultado"

        st.rerun()

    else:
        # Mensagem de erro
        if st.session_state.tentativas < TENTATIVAS:
            st.warning("❌ Resposta errada. Tente novamente!")
            st.session_state.tentativas += 1
        else:
            st.error(f"❌ Resposta errada. A correta era: {q['correta'].upper()}")
            st.session_state.tentativas = 1
            st.session_state.pontos = 10
            st.session_state.q_atual += 1

            if st.session_state.q_atual >= len(questoes):
                st.session_state.pagina = "resultado"

            st.rerun()
