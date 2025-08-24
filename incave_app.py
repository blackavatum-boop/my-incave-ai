# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd # ผมเพิ่ม import pandas เข้าไปเผื่อไว้กรณีที่คุณอาจจะใช้ในอนาคตครับ

print("DEBUG 1: Script started, imports successful.")

# --- ส่วนข้อมูล (ไม่มีการแก้ไข) ---
# ใช้ cache เพื่อให้โหลดข้อมูลแค่ครั้งเดียว ทำให้แอปเร็วขึ้น
@st.cache_data
def get_quiz_data():
    """
    ฟังก์ชันนี้ทำหน้าที่เก็บคำถาม, ตัวเลือก, และผลลัพธ์ทั้งหมดไว้ในที่เดียว
    """
    questions = [
        {"question": "1. ลักษณะรูปร่างโดยรวมของคุณ", "options": {"A": "ผอม แห้ง กล้ามเนื้อไม่แน่น", "B": "สมส่วน แข็งแรง มีกล้ามเนื้อ", "C": "อ้วนง่าย ตัวใหญ่ หนักแน่น", "D": "ผิวแดง ขี้ร้อน มีเหงื่อบ่อย"}},
        {"question": "2. พฤติกรรมการกินของคุณ", "options": {"A": "ชอบอาหารรสจัด เผ็ด เค็ม", "B": "กินง่าย อยู่ง่าย ไม่เลือกมาก", "C": "ชอบอาหารมัน หวาน แป้ง", "D": "หิวบ่อย ถ้าไม่กินจะหงุดหงิด"}},
        {"question": "3. ลักษณะการนอน", "options": {"A": "หลับยาก หลับไม่ลึก", "B": "นอนนาน ตื่นยาก", "C": "ง่วงง่าย นอนบ่อย", "D": "ตื่นกลางดึก รู้สึกร้อน"}},
        {"question": "4. ความชอบต่ออากาศ", "options": {"A": "ชอบลมพัด อากาศถ่ายเท", "B": "ชอบเย็นสบาย ไม่ร้อนไม่หนาว", "C": "แพ้ความเย็น หนาวง่าย", "D": "ร้อนบ่อย เหงื่อออกง่าย"}},
        {"question": "5. การเคลื่อนไหว", "options": {"A": "เคลื่อนไหวไว ชอบเดินเร็ว", "B": "ช้าแต่มั่นคง ไม่รีบร้อน", "C": "ขี้เกียจ เคลื่อนไหวน้อย", "D": "กระสับกระส่าย ขยันแต่หงุดหงิด"}},
        {"question": "6. สภาพจิตใจ/อารมณ์", "options": {"A": "คิดมาก หวั่นไหวง่าย", "B": "มั่นคง เยือกเย็น ใจดี", "C": "อ่อนไหว ขี้น้อยใจ", "D": "ขี้หงุดหงิด อารมณ์ร้อน"}},
        {"question": "7. อาการเจ็บป่วยที่เกิดบ่อย", "options": {"A": "ปวดเมื่อย ลมในตัวเยอะ", "B": "ปวดกล้ามเนื้อหนักๆ", "C": "บวมน้ำ ปัสสาวะบ่อย", "D": "เป็นไข้ ตัวร้อน ปวดหัวบ่อย"}}
    ]
    element_map = {'A': 'ลม', 'B': 'ดิน', 'C': 'น้ำ', 'D': 'ไฟ'}
    results_guide = {
        'ลม': {'description': 'พลังแห่งการเคลื่อนไหว ร่างกายไว อ่อนไหวง่าย ความคิดเยอะ', 'behavior': 'ควรทำสมาธิ เดินป่า หรือฟังเสียงธรรมชาติ เพื่อให้ลมภายในสมดุล', 'herbs': 'เช่น ขิง, พริกไทย, กระชาย – สมุนไพรที่ช่วยขับลมและเพิ่มความอบอุ่น'},
        'ดิน': {'description': 'พลังแห่งความมั่นคง แข็งแรง ทนทาน แต่เคลื่อนไหวช้า', 'behavior': 'ควรออกกำลังกายแบบกระตุ้น เช่น วิ่งจ็อกกิ้ง หรือโยคะที่ใช้กล้ามเนื้อ', 'herbs': 'เช่น ใบย่านาง, มะรุม – ช่วยขับของเสียและกระตุ้นระบบเผาผลาญ'},
        'น้ำ': {'description': 'พลังแห่งการหล่อเลี้ยง มีอารมณ์อ่อนไหว ง่วงง่าย', 'behavior': 'ควรตื่นเช้ารับแดด เดินริมแม่น้ำ และลดอาหารเย็น/หวาน', 'herbs': 'เช่น ตะไคร้, บัวบก, กระเจี๊ยบ – ช่วยลดความชื้นและขับของเหลวส่วนเกิน'},
        'ไฟ': {'description': 'พลังแห่งการเผาผลาญ เร่าร้อน มีพลังสูง แต่หงุดหงิดง่าย', 'behavior': 'ควรหลีกเลี่ยงแดดจัด ฝึกสมาธิ และเลือกอยู่ในที่เย็นสบาย', 'herbs': 'เช่น ฟ้าทะลายโจร, รางจืด, แตงกวา – สมุนไพรฤทธิ์เย็นลดความร้อนในร่างกาย'}
    }
    return questions, element_map, results_guide

# --- ส่วนวิเคราะห์และแสดงผล (ปรับแก้เล็กน้อย) ---
def analyze_and_display_results(scores, results_guide):
    """
    ฟังก์ชันนี้รับคะแนนมาคำนวณหาธาตุเด่นและแสดงผลลัพธ์พร้อมคำแนะนำ
    """
    if not scores:
        st.error("ไม่พบข้อมูลคะแนน")
        return

    max_score = max(scores.values())
    top_elements = [element for element, score in scores.items() if score == max_score]
    
    st.balloons()
    st.header("🧾 ผลลัพธ์ของคุณ:")

    # กรณีมีธาตุเด่นเท่ากัน
    if len(top_elements) > 1:
        elements_str = " และ ".join(top_elements)
        st.subheader(f"🔹 คุณมีธาตุเด่นที่สมดุลกันคือ: ธาตุ{elements_str}!")
        st.info("คุณมีลักษณะของหลายธาตุผสมผสานกันอย่างลงตัว ลองดูคำแนะนำของแต่ละธาตุเพื่อปรับใช้ให้เหมาะกับคุณ:")
        for element in top_elements:
            result = results_guide[element]
            st.markdown(f"---")
            st.markdown(f"### 💡 คำแนะนำธาตุ {element}")
            st.markdown(f"**ลักษณะ:** {result['description']}")
            st.markdown(f"**พฤติกรรม:** {result['behavior']}")
            st.markdown(f"**สมุนไพร:** {result['herbs']}")
    # กรณีมีธาตุเด่นธาตุเดียว
    else:
        primary_element = top_elements[0]
        result = results_guide[primary_element]
        st.subheader(f"🔹 คุณมี “ธาตุประจำเจ้าเรือน” คือ: {primary_element}")
        st.markdown(f"---")
        st.markdown(f"### 💡 คำแนะนำสำหรับธาตุ {primary_element}:")
        # แก้ไข Key ให้ตรงกันเพื่อความสอดคล้อง
        st.markdown(f"**ลักษณะ:** {result['description']}")
        st.markdown(f"**พฤติกรรม:** {result['behavior']}")
        st.markdown(f"**สมุนไพร:** {result['herbs']}")

print("DEBUG 2: Functions defined.")

# --- ส่วนหลักของแอปพลิเคชัน (แก้ไขส่วนรับ Input) ---

# ตั้งค่าหัวข้อและคำอธิบายของหน้าเว็บ
st.title("ถ้ำมนุษย์ AI: ค้นหาธาตุเจ้าเรือนของคุณ 🌿")
print("DEBUG 3: App title is set.")

st.write("กลับสู่พื้นฐานแห่งธรรมชาติ เพื่อเข้าใจร่างกายของคุณอย่างแท้จริง")

# โหลดข้อมูลคำถาม
questions, element_map, results_guide = get_quiz_data()

# สร้าง Form เพื่อให้ผู้ใช้ตอบคำถามทั้งหมดก่อนกดส่ง
with st.form("quiz_form"):
    user_answers = []
    st.info("กรุณาเลือกคำตอบที่ตรงกับคุณมากที่สุดในแต่ละข้อ")
    
    for i, q_data in enumerate(questions):
        st.subheader(f"❓ {q_data['question']}")
        
        # *** จุดที่แก้ไข ***
        # เราจะส่ง key ('A', 'B', 'C', 'D') เป็นค่าจริง
        # แต่จะแสดงข้อความเต็มๆ ให้ผู้ใช้เห็น
        answer = st.radio(
            "เลือกคำตอบ:",
            options=q_data['options'].keys(),  # ส่งแค่ Key เข้าไป
            format_func=lambda key: f"{key}: {q_data['options'][key]}", # ฟังก์ชันจัดรูปแบบการแสดงผล
            key=f"q{i}"
        )
        user_answers.append(answer) # ค่าที่ได้จะเป็น 'A', 'B', 'C', 'D' โดยตรง

    # ปุ่มส่งคำตอบ
    submitted = st.form_submit_button("วิเคราะห์ผลลัพธ์")

# เมื่อผู้ใช้กดปุ่ม "วิเคราะห์ผลลัพธ์"
if submitted:
    # คำนวณคะแนน
    scores = {'ลม': 0, 'ดิน': 0, 'น้ำ': 0, 'ไฟ': 0}
    for answer_key in user_answers:
        element = element_map[answer_key]
        scores[element] += 1
    
    # แสดงผลลัพธ์
    analyze_and_display_results(scores, results_guide)

print("DEBUG 4: End of script, app should be running.")
