# -*- coding: utf-8 -*-
import streamlit as st

@st.cache_data
def get_quiz_data():
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
        'ลม': {'description': 'คุณเป็นคนธาตุลม – พลังแห่งการเคลื่อนไหว ร่างกายไว อ่อนไหวง่าย ความคิดเยอะ', 'behavior': 'ควรทำสมาธิ เดินป่า หรือฟังเสียงธรรมชาติ เพื่อให้ลมภายในสมดุล', 'herbs': 'เช่น ขิง, พริกไทย, กระชาย – สมุนไพรที่ช่วยขับลมและเพิ่มความอบอุ่น'},
        'ดิน': {'description': 'คุณเป็นคนธาตุดิน – พลังแห่งความมั่นคง แข็งแรง ทนทาน แต่เคลื่อนไหวช้า', 'behavior': 'ควรออกกำลังกายแบบกระตุ้น เช่น วิ่งจ็อกกิ้ง หรือโยคะที่ใช้กล้ามเนื้อ', 'herbs': 'เช่น ใบย่านาง, มะรุม – ช่วยขับของเสียและกระตุ้นระบบเผาผลาญ'},
        'น้ำ': {'description': 'คุณเป็นคนธาตุน้ำ – พลังแห่งการหล่อเลี้ยง มีอารมณ์อ่อนไหว ง่วงง่าย', 'behavior': 'ควรตื่นเช้ารับแดด เดินริมแม่น้ำ และลดอาหารเย็น/หวาน', 'herbs': 'เช่น ตะไคร้, บัวบก, กระเจี๊ยบ – ช่วยลดความชื้นและขับของเหลวส่วนเกิน'},
        'ไฟ': {'description': 'คุณเป็นคนธาตุไฟ – พลังแห่งการเผาผลาญ เร่าร้อน มีพลังสูง แต่หงุดหงิดง่าย', 'behavior': 'ควรหลีกเลี่ยงแดดจัด ฝึกสมาธิ และเลือกอยู่ในที่เย็นสบาย', 'herbs': 'เช่น ฟ้าทะลายโจร, รางจืด, แตงกวา – สมุนไพรฤทธิ์เย็นลดความร้อนใน'}
    }
    return questions, element_map, results_guide

def analyze_and_display_results(scores, results_guide):
    if not scores:
        st.error("ไม่พบข้อมูลคะแนน")
        return
    max_score = max(scores.values())
    top_elements = [element for element, score in scores.items() if score == max_score]
    st.balloons()
    st.header("🧾 ผลลัพธ์ของคุณ:")
    if len(top_elements) > 1:
        elements_str = " และ ".join(top_elements)
        st.subheader(f"🔹 คุณมีธาตุเด่นที่สมดุลกันคือ: ธาตุ{elements_str}!")
        st.info("คุณมีลักษณะของหลายธาตุผสมผสานกันอย่างลงตัว ลองดูคำแนะนำของแต่ละธาตุเพื่อปรับใช้ให้เหมาะกับคุณ:")
        for element in top_elements:
             st.markdown(f"---")
             st.markdown(f"### 💡 คำแนะนำธาตุ{element}")
             st.markdown(f"**ลักษณะ:** {results_guide[element]['description']}")
             st.markdown(f"**พฤติกรรม:** {results_guide[element]['behavior']}")
             st.markdown(f"**สมุนไพร:** {results_guide[element]['herbs']}")
    else:
        primary_element = top_elements[0]
        st.subheader(f"🔹 คุณมี “ธาตุประจำเจ้าเรือน” คือ: {primary_element}")
        st.markdown(f"---")
        st.markdown(f"### 💡 คำแนะนำสำหรับธาตุ{primary_element}:")
        st.markdown(f"**ลักษณะโดยรวม:** {results_guide[primary_element]['description']}")
        st.markdown(f"**พฤติกรรมที่แนะนำ:** {results_guide[primary_element]['behavior']}")
        st.markdown(f"**สมุนไพรช่วยปรับสมดุล:** {results_guide[primary_element]['herbs']}")

st.title("ถ้ำมนุษย์ AI: ค้นหาธาตุเจ้าเรือนของคุณ 🌿")
st.write("กลับสู่พื้นฐานแห่งธรรมชาติ เพื่อเข้าใจร่างกายของคุณอย่างแท้จริง")
questions, element_map, results_guide = get_quiz_data()
user_answers = []
with st.form("quiz_form"):
    for i, q_data in enumerate(questions):
        st.subheader(f"❓ {q_data['question']}")
        options = [f"{key}: {value}" for key, value in q_data['options'].items()]
        answer = st.radio("เลือกคำตอบ:", options, key=f"q{i}")
        user_answers.append(answer[0])
    submitted = st.form_submit_button("วิเคราะห์ผลลัพธ์")
if submitted:
    scores = {'ลม': 0, 'ดิน': 0, 'น้ำ': 0, 'ไฟ': 0}
    for answer in user_answers:
        element = element_map[answer]
        scores[element] += 1
    analyze_and_display_results(scores, results_guide)