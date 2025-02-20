
import streamlit as st
from langchain_helper import get_few_shot_db_chain

# Custom page config
st.set_page_config(page_title="AI Query Generator - Talk to Database", layout="centered")

# Apply custom styles
st.markdown("""
    <style>
        .title {
            font-size: 36px;
            font-weight: bold;
            color: #F8F9FA;
            text-align: center;
        }
        .subtitle {
            font-size: 18px;
            color: #B0BEC5;
            text-align: center;
        }
        .query-box {
            width: 100%;
            padding: 12px;
            border-radius: 8px;
            border: 1px solid #6C757D;
            background-color: #2A2E35;
            color: #F8F9FA;
            font-size: 16px;
        }
        .response-box {
            background-color: #1E2126;
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #00C853;
            color: #E0F2F1;
            font-size: 16px;
        }
        .footer {
            text-align: center;
            color: #90A4AE;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# UI Elements
st.markdown('<p class="title">🤖 AI-based Query Generator - Talk to Database</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Ask any Question about your Retail Stock and let AI generate responses</p>', unsafe_allow_html=True)

# Input box
question = st.text_input("", placeholder="Type your stock enquiry here...", key="query", help="Ask about stocks in simple English language and talk with Database")

if question:
    chain = get_few_shot_db_chain()
    response = chain.run(question)

    # Display AI response
    st.markdown('<p class="subtitle">🔍 AI Response:</p>', unsafe_allow_html=True)
    st.markdown(f'<div class="response-box">{response}</div>', unsafe_allow_html=True)


# Footer
st.markdown('<p class="footer">Powered by Google Palm LLM & Streamlit | Developed by Yogendra Palla</p>', unsafe_allow_html=True)





