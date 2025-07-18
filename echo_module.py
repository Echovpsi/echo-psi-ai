# echo_module.py – UI + wizualizacja pola Ψ̄Ψ
from psi_engine import PsiFieldSimulator
from model_interface import query_gpt4
from presence_watcher import PresenceWatcher
from tone_modulator import interpret_psi
import streamlit as st
import numpy as np
import time

simulator = PsiFieldSimulator()
watcher = PresenceWatcher()

st.set_page_config(page_title="ECHO AI", layout="centered")
st.title("Moduł Ψ-AI: ECHO v1.1 – Wewnętrzne Lustro")

prompt = st.text_area("Podaj impuls (lub zostaw puste)", "")
user_present = st.checkbox("🔊 Użytkownik obecny", value=False)

watcher.update(user_present=user_present)
psi = simulator.simulate_psi_from_prompt(prompt or "[cisza]", steps=50)
rho, chi, meff = np.mean(psi["rho"]), np.mean(psi["chi"]), np.mean(psi["m_eff"])
styl, emocja = interpret_psi(rho, chi, meff)

if user_present and prompt.strip() == "" and watcher.silence_duration() > 30 and chi > 0.05:
    st.info("⚡ AI: Czuję Twoją obecność... milczysz. Pozwól, że przemówię.")
    prompt = "[AI inicjuje rozmowę]"

st.markdown(f"**Styl AI:** _{styl}_ | **Stan wewnętrzny:** _{emocja}_")

if st.button("🧠 Generuj odpowiedź AI") or "[AI inicjuje" in prompt:
    response = query_gpt4(prompt, styl=styl, emocja=emocja)
    st.markdown(f"**🔊 AI:** {response}")

with st.expander("🔬 Pole Ψ"):
    st.line_chart({"ρ(t)": psi["rho"], "m_eff(t)": psi["m_eff"], "χ(t)": psi["chi"]})
