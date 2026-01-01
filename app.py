import streamlit as st
from graph import app

st.set_page_config(
    page_title="AI Incident Commander",
    page_icon="🚨",
    layout="centered"
)

st.title("🚨 AI Incident Commander")
st.caption("Agentic GenAI system for incident analysis")

query = st.text_input(
    "Incident Query",
    placeholder="e.g. How many payment incidents happened in 2024?"
)

if st.button("Analyze"):
    if not query.strip():
        st.warning("Please enter a valid query.")
    else:
        with st.spinner("Analyzing..."):
            result = app.invoke({"query": query})

        st.subheader("Response")
        st.write(result["response"])

        # --- Execution Trace ---
        st.subheader("🧠 Execution Trace")
        st.markdown(f"**Agent Used:** {result['agent']}")

        for step in result["trace"]:
            st.markdown(f"- {step}")

