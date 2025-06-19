import streamlit as st
import time
from service.feedback_generator import get_ai_feedback
from service.speech_to_text import transcribe_audio
from util.video_processing import extract_audio

# --- Development & Testing Switch ---
MOCKING_ENABLED = True
# mocking = True:  จะใช้ข้อมูลจำลอง (Fake data) เพื่อให้เทสได้เร็ว ไม่ต้องเรียก API จริง
# mocking = False: จะเรียกใช้ API ของจริงทั้งหมด เหมาะสำหรับตอนจะใช้งานจริง

#------- Interface -------#
st.title('LongSorn - Evaluate Your Teaching')
st.divider()

st.header('Upload Your Video')
uploaded_video = st.file_uploader(
    "Choose a video file", 
    type=["mp4", "mov", "avi"],
    label_visibility="collapsed"
    )

if uploaded_video is not None:
    st.video(uploaded_video)
    st.divider()
    
    st.header("get your feedback")
    
    if st.button("process"):
       
        with st.spinner("Processing..."):
            audio_path = extract_audio(uploaded_video, mocking=MOCKING_ENABLED)
            transcript = transcribe_audio(audio_path,mocking=MOCKING_ENABLED)
            feedback = get_ai_feedback(transcript,mocking=MOCKING_ENABLED)
            # Simulate processing
            time.sleep(2)

        st.success("Feedback generated successfully!")
        st.divider()    
    
        st.subheader("Transcript")
        st.text_area("", transcript, height=150)    
            
        st.subheader("AI Feedback")
        st.markdown(feedback)
        
        st.divider()