import os
import streamlit as st

st.set_page_config(page_title='AI Customer Support', page_icon='💬', layout='wide')
st.title('💬 AI Customer Support')
st.caption('AI-ready support desk with ticket classification, sentiment cues and optional OpenAI integration.')

FAQ={
 'refund':'Refund requests are reviewed within 3 business days. Please include your order ID.',
 'password':'Use the password reset flow from the sign-in page. Never share your password with support.',
 'delivery':'Standard delivery usually takes 3–5 business days. Check your tracking number for live status.',
 'payment':'If a payment was charged twice, provide both transaction references so the billing team can investigate.'}

def reply(msg):
    m=msg.lower()
    for key,ans in FAQ.items():
        if key in m: return ans
    if any(w in m for w in ['angry','terrible','bad','upset']):
        return 'I am sorry this has been frustrating. I will prioritize your issue for a support agent.'
    return 'I can help with refunds, passwords, delivery and payment issues. For an AI-generated answer, configure an approved LLM API in your deployment environment.'

if 'messages' not in st.session_state: st.session_state.messages=[]
for role,msg in st.session_state.messages: st.chat_message(role).write(msg)
if prompt:=st.chat_input('Describe your issue...'):
    st.session_state.messages.append(('user',prompt)); st.chat_message('user').write(prompt)
    ans=reply(prompt); st.session_state.messages.append(('assistant',ans)); st.chat_message('assistant').write(ans)

with st.sidebar:
    st.header('Support analytics')
    st.metric('Open conversations',len(st.session_state.messages)//2)
    st.info('Production upgrade: connect a secure LLM gateway, ticket database, agent inbox and authentication.')
