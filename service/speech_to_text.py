import time 

def transcribe_audio(audio_path, mocking=False):
    """_summary_

    Args:
        audio_path (str): path to the audio file to be transcribed.
        mocking (bool, optional): Defaults to False.
    """
    
    if mocking:
        """Simulate the transcription process for testing purposes."""
        time.sleep(1)  # Simulate processing
        print(f"กำลังส่งไฟล์ {audio_path} ไปแปลงเป็นข้อความ (ของปลอม)...")
        time.sleep(5) 
        transcript = "สวัสดีครับท่านผู้ชมทุกท่าน วันนี้เราจะมาเรียนเรื่อง...เอ่อ...การสร้างแอปพลิเคชันด้วย Streamlit กันนะครับ อย่างที่เห็นในตอนนี้นะครับ เราสามารถอัปโหลดวิดีโอเข้ามาได้แล้ว..."
        print("แปลงเป็นข้อความเสร็จแล้ว")
        return transcript