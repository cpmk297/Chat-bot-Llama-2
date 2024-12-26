import streamlit as st

import langchain

import time 

import langchain_huggingface

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

llm = HuggingFaceEndpoint(
    repo_id = "microsoft/Phi-3.5-mini-instruct",
    temperature = 0.3,
    model_kwargs = {"max_length": 128}
)

chat = ChatHuggingFace(llm = llm, verbose = False)

def get_response(prompt) :

     resultat = chat.invoke(prompt)

     return resultat.content

st.title("Comment puis-je vous aider ?")

if "messages" not in st.session_state:

    st.session_state.messages = []

for messages in st.session_state.messages:

        with st.chat_message(messages['role']):

            st.markdown(messages['content'])

if prompt := st.chat_input("Quoi de neuf ?"):
     
     with st.chat_message('user'):
          
          st.markdown(prompt)
     with st.spinner('Patientez un instant...'):
       
          time.sleep(4)

     st.session_state.messages.append({"role": "user", "content": prompt})
    
     response = get_response(st.session_state.messages)

     with st.chat_message('assistant'):
    
           st.markdown(response) 

     st.session_state.messages.append({"role": "assistant", "content": response})

        
           


