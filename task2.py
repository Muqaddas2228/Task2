import streamlit as st
import time

# 🌟 Streamlit Page Config
st.set_page_config(page_title="AI Mission Bot 🤖", page_icon="🚀")

# 🎯 Title & Description
st.title("🤖 AI Mission Bot")
st.write("Welcome, Agent! Before we begin, please enter your name to access your secret mission. 🔐")

# 📝 User Input
name = st.text_input("🔹 Enter your name:")

# 🚀 AI Response Button
if st.button("🔍 Start Mission"):
    if name:
        with st.spinner("🔄 Processing..."):
            time.sleep(2)  # ہائی-ٹیک ایفیکٹ دینے کے لیے وقفہ

        st.success(f"🔹 Name detected: {name}")
        time.sleep(1)
        st.balloons()  # جشن کا ایفیکٹ
        st.success(f"🔹 Access Granted! Welcome, Agent {name}. Your mission awaits! 🚀")
    else:
        st.error("⚠️ Please enter your name to proceed!")
