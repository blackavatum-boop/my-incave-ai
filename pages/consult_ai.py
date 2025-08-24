# pages/consult_ai.py
import streamlit as st
import google.generativeai as genai
import os

# --- การตั้งค่า Gemini AI ---
try:
    # ดึง Key จาก Environment Group ที่เราตั้งค่าไว้บน Render
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
except Exception:
    GEMINI_API_KEY = ""

if not GEMINI_API_KEY:
    st.error("ไม่พบ GEMINI_API_KEY ในการตั้งค่า Environment ของ Render")
else:
    genai.configure(api_key=GEMINI_API_KEY)

# --- ข้อมูลสินค้า ---
all_products = [
    { "product_id": "P001", "name": "Am Good Nano Oil" },
    { "product_id": "P002", "name": "Am Good Coffee" },
    { "product_id": "P003", "name": "AM Knock (น้ำมัน CBD)"},
    { "product_id": "P004", "name": "Am Fine" },
    { "product_id": "S001", "name": "บริการอบสินแร่ภูเขาไฟญี่ปุ่น"}
]

# --- หน้าตาของแอปพลิเคชัน ---
st.title("🤖 ปรึกษาผู้เชี่ยวชาญ AI")

if not GEMINI_API_KEY:
    st.stop() # หยุดการทำงานถ้าไม่มี Key

st.write("พิมพ์คำถามเกี่ยวกับสุขภาพหรือผลิตภัณฑ์ของเราได้เลย")

# ใช้ session_state เพื่อเก็บประวัติการแชท
if "messages" not in st.session_state:
    st.session_state.messages = []

# แสดงข้อความแชทเก่า
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ช่องรับ input จากผู้ใช้
if user_question := st.chat_input("ถามอะไรดี?"):
    # เพิ่มคำถามของผู้ใช้ vào session state และแสดงผล
    st.session_state.messages.append({"role": "user", "content": user_question})
    with st.chat_message("user"):
        st.markdown(user_question)

    # เรียก AI มาตอบ
    try:
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        product_context = str(all_products)
        prompt = f"""คุณคือ "incave AI" ผู้เชี่ยวชาญสุขภาพที่เป็นมิตร ข้อมูลผลิตภัณฑ์ที่มี: {product_context}. 
        ตอบคำถามของผู้ใช้: "{user_question.strip()}" 
        หากเกี่ยวข้องกับสินค้าให้แนะนำได้ แต่อย่าพยายามวินิจฉัยโรค และแนะนำให้ปรึกษาแพทย์ผู้เชี่ยวชาญเสมอเมื่อเป็นเรื่องที่เกี่ยวข้องกับอาการเจ็บป่วย"""

        with st.spinner('AI กำลังคิด...'):
            response = model.generate_content(prompt)
            ai_answer = response.text

        # เพิ่มคำตอบของ AI vào session state และแสดงผล
        st.session_state.messages.append({"role": "assistant", "content": ai_answer})
        with st.chat_message("assistant"):
            st.markdown(ai_answer)

    except Exception as e:
        st.error(f"ขออภัยค่ะ เกิดข้อผิดพลาด: {e}")
