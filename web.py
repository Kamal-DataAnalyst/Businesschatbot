import streamlit as st

st.image("imags.png")
st.title("AI ADVISOR BOt :robot_face:")

with st.chat_message("ai"):
    st.write("How may I adviced you today?")

user_input = st.chat_input("Ask your Questions")
if "user_input" not in st.session_state:
    st.session_state["user_input"] = user_input
if "conversation_history" not in st.session_state:
    st.session_state["conversation_history"] = []

conve_history = st.session_state["conversation_history"]

if user_input is not None:
    with st.chat_message("user"):
        conve_history.append(user_input)
        # st.write(user_input)
for message in conve_history:
    with st.chat_message("user"):
        st.write(message)
