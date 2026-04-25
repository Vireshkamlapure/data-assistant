import streamlit as st
import pandas as pd
from agent import get_agent

st.set_page_config(page_title="Data Assistant", layout="centered")
st.title("Data AI Assistant")
st.markdown("Upload your Excel Dataset and Ask me anything about it!!!! ")

uploaded_file = st.file_uploader("Upload your Excel Files ", type=["xlsx", "xls"])

if uploaded_file is not None:
    try:
        if "last_uploaded_file" not in st.session_state or st.session_state.last_uploaded_file != uploaded_file.name:
            with st.spinner("Reading Data and Initializing AI..."):
                df = pd.read_excel(uploaded_file)
                st.session_state.agent = get_agent(df)
                st.session_state.last_uploaded_file = uploaded_file.name

                st.session_state.messages = [
                    {"role": "assistant", "content": f"Successfully loaded **{uploaded_file.name}**! What would you like to know?"}
                ]
    except Exception as e:
        st.error(f"Error reading in file {e}")
        st.stop()

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
    if prompt := st.chat_input("E.g. What percentage claims were accepted?"):
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):
            with st.spinner("Analyzing data..."):
                try:
                    response = st.session_state.agent.invoke(prompt)
                    answer = response["output"]
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                except Exception as e:
                    st.error(f"An error occured as {e}")
else:
    st.info("Please upload an Excel Dataset above to get started.")